import flet as ft
import pymysql.cursors

# ----------------------------
# CONFIGURAÇÃO BANCO DE DADOS
# ----------------------------
def criar_conexao():
    try:
        conn = pymysql.connect(
            host="localhost",
            database="sistema_estoque",
            user="root",         
            password="1234",
            cursorclass=pymysql.cursors.DictCursor 
        )
        return conn
    except Exception as e:
        print("Erro ao conectar no MySQL:", e)
        return None


# ----------------------------
# FUNÇÕES DE BANCO
# ----------------------------
def autenticar_usuario(email, senha):
    conn = criar_conexao()
    if not conn:
        return None
    try:
        cursor = conn.cursor()
        query = """
            SELECT id, nome, email, tipo
            FROM usuarios
            WHERE email = %s AND senha = %s AND ativo = TRUE
        """
        cursor.execute(query, (email, senha))
        user = cursor.fetchone()
        return user
    except Exception as e:
        print("Erro ao autenticar:", e)
        return None
    finally:
        conn.close()


def listar_produtos():
    conn = criar_conexao()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        query = """
            SELECT p.id, p.nome, p.descricao, p.estoque_atual, 
                   p.preco_venda, p.estoque_minimo
            FROM produtos p
            WHERE p.ativo = TRUE
            ORDER BY p.nome
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print("Erro ao listar produtos:", e)
        return []
    finally:
        conn.close()


def cadastrar_produto(nome, descricao, preco_venda, estoque_minimo, estoque_inicial):
    conn = criar_conexao()
    if not conn:
        return False
    try:
        cursor = conn.cursor()
        query = """
            INSERT INTO produtos
            (nome, descricao, preco_venda, estoque_minimo, estoque_atual)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (nome, descricao, preco_venda, estoque_minimo, estoque_inicial))
        conn.commit()
        return True
    except Exception as e:
        print("Erro ao cadastrar produto:", e)
        return False
    finally:
        conn.close()


def buscar_produto_por_id(produto_id):
    conn = criar_conexao()
    if not conn:
        return None
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM produtos WHERE id = %s"
        cursor.execute(query, (produto_id,))
        return cursor.fetchone()
    except Exception as e:
        print("Erro ao buscar produto:", e)
        return None
    finally:
        conn.close()


def registrar_movimentacao_bd(produto_id, usuario_id, tipo, quantidade, valor_unitario, observacao):
    """
    Registra movimentação na tabela movimentacoes_estoque
    e atualiza o estoque do produto.
    """
    # 1) Busca produto
    produto = buscar_produto_por_id(produto_id)
    if not produto:
        return False, "Produto não encontrado."

    estoque_atual = produto["estoque_atual"]

    # 2) Calcula novo estoque
    if tipo == "ENTRADA":
        novo_estoque = estoque_atual + quantidade
    else:  # SAIDA
        if quantidade > estoque_atual:
            return False, "Estoque insuficiente para saída."
        novo_estoque = estoque_atual - quantidade

    valor_total = None
    if valor_unitario is not None:
        valor_total = quantidade * valor_unitario

    conn = criar_conexao()
    if not conn:
        return False, "Falha na conexão com o banco."

    try:
        cursor = conn.cursor()
        # Insere movimentação
        query_mov = """
            INSERT INTO movimentacoes_estoque
            (produto_id, usuario_id, tipo, quantidade, valor_unitario, valor_total, observacao)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query_mov,
            (produto_id, usuario_id, tipo, quantidade, valor_unitario, valor_total, observacao)
        )

        # Atualiza estoque
        query_upd = "UPDATE produtos SET estoque_atual = %s WHERE id = %s"
        cursor.execute(query_upd, (novo_estoque, produto_id))

        conn.commit()
        return True, "Movimentação registrada com sucesso."
    except Exception as e:
        print("Erro ao registrar movimentação:", e)
        return False, f"Erro ao registrar movimentação: {str(e)}"
    finally:
        conn.close()


def listar_movimentacoes(limit=50):
    conn = criar_conexao()
    if not conn:
        return []
    try:
        cursor = conn.cursor()
        query = """
            SELECT m.id, m.data_movimentacao, m.tipo, m.quantidade,
                   m.valor_unitario, m.valor_total, m.observacao,
                   p.nome AS produto_nome,
                   u.nome AS usuario_nome
            FROM movimentacoes_estoque m
            JOIN produtos p ON m.produto_id = p.id
            JOIN usuarios u ON m.usuario_id = u.id
            ORDER BY m.data_movimentacao DESC
            LIMIT %s
        """
        cursor.execute(query, (limit,))
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        print("Erro ao listar movimentações:", e)
        return []
    finally:
        conn.close()


# ----------------------------
# INTERFACE FLET
# ----------------------------
def main(page: ft.Page):
    page.title = "Sistema de Estoque - Flet + MySQL"
    page.window_width = 1100
    page.window_height = 700

    # ------------- TELA LOGIN -------------

    email_input = ft.TextField(label="Email", width=300)
    senha_input = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)
    login_msg = ft.Text(color="red")

    def efetuar_login(e):
        email = email_input.value.strip()
        senha = senha_input.value.strip()
        if not email or not senha:
            login_msg.value = "Preencha email e senha."
            page.update()
            return

        usuario = autenticar_usuario(email, senha)
        if usuario:
            page.session.set("usuario", usuario)
            carregar_tela_principal()
        else:
            login_msg.value = "Usuário ou senha inválidos."
            page.update()

    btn_login = ft.ElevatedButton("Entrar", on_click=efetuar_login, width=300)

    login_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Sistema de Estoque", size=30, weight="bold"),
                ft.Text("Login", size=20),
                email_input,
                senha_input,
                btn_login,
                login_msg,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )

    # ------------- TELA PRINCIPAL -------------

    # ---- ABA PRODUTOS ----
    tabela_produtos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Descrição")),
            ft.DataColumn(ft.Text("Estoque Atual")),
            ft.DataColumn(ft.Text("Estoque Mínimo")),
            ft.DataColumn(ft.Text("Preço Venda")),
        ],
        rows=[],
    )

    def atualizar_tabela_produtos():
        produtos = listar_produtos()
        tabela_produtos.rows.clear()
        for p in produtos:
            tabela_produtos.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(p["id"]))),
                        ft.DataCell(ft.Text(p["nome"])),
                        ft.DataCell(ft.Text(p["descricao"] or "")),
                        ft.DataCell(ft.Text(str(p["estoque_atual"]))),
                        ft.DataCell(ft.Text(str(p["estoque_minimo"]))),
                        ft.DataCell(ft.Text(f'R$ {p["preco_venda"]:.2f}' if p["preco_venda"] is not None else "-")),
                    ]
                )
            )
        page.update()

    nome_prod_input = ft.TextField(label="Nome do produto", width=400)
    desc_prod_input = ft.TextField(label="Descrição", width=400, multiline=True, max_lines=3)
    preco_venda_input = ft.TextField(label="Preço de venda (R$)", width=200)
    estoque_minimo_input = ft.TextField(label="Estoque mínimo", width=200)
    estoque_inicial_input = ft.TextField(label="Estoque inicial", width=200)
    msg_produto = ft.Text(color="green")

    def salvar_produto(e):
        nome = nome_prod_input.value.strip()
        desc = desc_prod_input.value.strip()
        preco_venda_str = preco_venda_input.value.strip()
        estoque_minimo_str = estoque_minimo_input.value.strip()
        estoque_inicial_str = estoque_inicial_input.value.strip()

        if not nome:
            msg_produto.value = "Nome é obrigatório."
            msg_produto.color = "red"
            page.update()
            return

        try:
            preco_venda = float(preco_venda_str) if preco_venda_str else 0.0
            estoque_minimo = int(estoque_minimo_str) if estoque_minimo_str else 0
            estoque_inicial = int(estoque_inicial_str) if estoque_inicial_str else 0
        except ValueError:
            msg_produto.value = "Preencha números válidos para preço e estoques."
            msg_produto.color = "red"
            page.update()
            return

        ok = cadastrar_produto(nome, desc, preco_venda, estoque_minimo, estoque_inicial)
        if ok:
            msg_produto.value = "Produto cadastrado com sucesso!"
            msg_produto.color = "green"
            nome_prod_input.value = ""
            desc_prod_input.value = ""
            preco_venda_input.value = ""
            estoque_minimo_input.value = ""
            estoque_inicial_input.value = ""
            atualizar_tabela_produtos()
            carregar_produtos_combo() 
        else:
            msg_produto.value = "Erro ao cadastrar produto."
            msg_produto.color = "red"
        page.update()

    btn_salvar_prod = ft.ElevatedButton("Salvar produto", on_click=salvar_produto)

    cadastro_produtos_view = ft.Column(
        [
            ft.Text("Cadastro de Produtos", size=20, weight="bold"),
            ft.Row([nome_prod_input]),
            ft.Row([desc_prod_input]),
            ft.Row([preco_venda_input, estoque_minimo_input, estoque_inicial_input]),
            btn_salvar_prod,
            msg_produto,
            ft.Divider(),
            ft.Text("Lista de Produtos", size=18, weight="bold"),
            ft.Container(
                content=tabela_produtos,
                border=ft.border.all(1, ft.Colors.GREY_400),
                border_radius=5,
                padding=10,
            ),
        ],
        scroll="auto",
        expand=True,
    )

    # ---- ABA MOVIMENTAÇÕES ----
    
    produtos_combo = ft.Dropdown(label="Selecione o Produto", width=400)
    tipo_combo = ft.Dropdown(
        label="Tipo de Movimentação",
        options=[
            ft.dropdown.Option("ENTRADA"),
            ft.dropdown.Option("SAIDA"),
        ],
        width=200,
    )
    qtd_input = ft.TextField(label="Quantidade", width=150)
    valor_unit_input = ft.TextField(label="Valor unitário (R$) - opcional", width=200)
    obs_input = ft.TextField(label="Observação", width=400, multiline=True, max_lines=3)
    msg_mov = ft.Text(color="green")

    tabela_mov = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Data")),
            ft.DataColumn(ft.Text("Produto")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Qtd")),
            ft.DataColumn(ft.Text("Vlr Unit")),
            ft.DataColumn(ft.Text("Vlr Total")),
            ft.DataColumn(ft.Text("Usuário")),
            ft.DataColumn(ft.Text("Obs")),
        ],
        rows=[],
    )

    def carregar_produtos_combo():
        produtos = listar_produtos()
        produtos_combo.options.clear()
        for p in produtos:
            produtos_combo.options.append(
                ft.dropdown.Option(key=str(p["id"]), text=p["nome"])
            )
        page.update()

    def atualizar_tabela_mov():
        movs = listar_movimentacoes(limit=50)
        tabela_mov.rows.clear()
        for m in movs:
            tabela_mov.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(m["id"]))),
                        ft.DataCell(ft.Text(str(m["data_movimentacao"]))),
                        ft.DataCell(ft.Text(m["produto_nome"])),
                        ft.DataCell(ft.Text(m["tipo"])),
                        ft.DataCell(ft.Text(str(m["quantidade"]))),
                        ft.DataCell(
                            ft.Text(
                                f'R$ {m["valor_unitario"]:.2f}'
                                if m["valor_unitario"] is not None
                                else "-"
                            )
                        ),
                        ft.DataCell(
                            ft.Text(
                                f'R$ {m["valor_total"]:.2f}'
                                if m["valor_total"] is not None
                                else "-"
                            )
                        ),
                        ft.DataCell(ft.Text(m["usuario_nome"])),
                        ft.DataCell(ft.Text(m["observacao"] or "")),
                    ]
                )
            )
        page.update()

    def registrar_movimentacao(e):
        msg_mov.color = "red"
        msg_mov.value = ""

        if not produtos_combo.value:
            msg_mov.value = "Selecione um produto."
            page.update()
            return

        if not tipo_combo.value:
            msg_mov.value = "Selecione o tipo de movimentação (ENTRADA ou SAIDA)."
            page.update()
            return

        if not qtd_input.value.strip():
            msg_mov.value = "Informe a quantidade."
            page.update()
            return

        try:
            qtd = int(qtd_input.value.strip())
            if qtd <= 0:
                raise ValueError
        except ValueError:
            msg_mov.value = "Quantidade deve ser um número inteiro maior que zero."
            page.update()
            return

        valor_unitario = None
        if valor_unit_input.value.strip():
            try:
                valor_unitario = float(valor_unit_input.value.strip())
            except ValueError:
                msg_mov.value = "Valor unitário inválido."
                page.update()
                return

        obs = obs_input.value.strip() or None

        usuario = page.session.get("usuario")
        if not usuario:
            msg_mov.value = "Usuário não autenticado."
            page.update()
            return

        produto_id = int(produtos_combo.value)
        ok, mensagem = registrar_movimentacao_bd(
            produto_id=produto_id,
            usuario_id=usuario["id"],
            tipo=tipo_combo.value,
            quantidade=qtd,
            valor_unitario=valor_unitario,
            observacao=obs,
        )

        if ok:
            msg_mov.color = "green"
            msg_mov.value = mensagem
            qtd_input.value = ""
            valor_unit_input.value = ""
            obs_input.value = ""
            atualizar_tabela_produtos()
            atualizar_tabela_mov()
        else:
            msg_mov.color = "red"
            msg_mov.value = mensagem

        page.update()

    btn_registrar_mov = ft.ElevatedButton("Registrar Movimentação", on_click=registrar_movimentacao)

    movimentacoes_view = ft.Column(
        [
            ft.Text("Movimentações de Estoque", size=20, weight="bold"),
            ft.Row([produtos_combo, tipo_combo]),
            ft.Row([qtd_input, valor_unit_input]),
            ft.Row([obs_input]),
            btn_registrar_mov,
            msg_mov,
            ft.Divider(),
            ft.Text("Últimas Movimentações", size=18, weight="bold"),
            ft.Container(
                content=tabela_mov,
                border=ft.border.all(1, ft.Colors.GREY_400),
                border_radius=5,
                padding=10,
            ),
        ],
        scroll="auto",
        expand=True,
    )

    # ---- MONTAGEM TELA PRINCIPAL ----
    
    def carregar_tela_principal():
        usuario = page.session.get("usuario")
        if not usuario:
            return

        user_info = ft.Text(f'Usuário: {usuario["nome"]} ({usuario["tipo"]})')

        def logout(e):
            page.session.set("usuario", None)
            page.clean()
            page.add(login_container)
            page.update()

        btn_logout = ft.ElevatedButton("Sair", on_click=logout)

        abas = ft.Tabs(
            tabs=[
                ft.Tab(text="Produtos", content=cadastro_produtos_view),
                ft.Tab(text="Movimentações", content=movimentacoes_view),
            ],
            expand=True,
        )

        page.clean()
        page.add(
            ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Sistema de Estoque", size=24, weight="bold"),
                            ft.Row([user_info, btn_logout]),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(),
                    abas,
                ],
                expand=True,
            )
        )
        
        atualizar_tabela_produtos()
        carregar_produtos_combo()
        atualizar_tabela_mov()
        page.update()

    page.add(login_container)


if __name__ == "__main__":
    ft.app(target=main)
