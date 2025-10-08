
# Aula 09 – Interface gráfica com Flet (Resumo + Exemplos)

Este documento resume, em palavras simples, os principais conceitos da biblioteca Flet para criar interfaces gráficas com Python e traz exemplos inéditos de código para você praticar.

## Visão geral
- Flet é uma biblioteca Python para construir interfaces gráficas modernas que rodam como apps de desktop ou na web.
- A ideia é escrever UI com componentes (widgets) de alto nível, organizar com layouts e reagir a eventos, tudo em Python.
- Diferente de toolkits tradicionais, o Flet facilita publicar sua UI como app web com o mesmo código.

Observação importante: você pode encontrar na internet afirmações imprecisas sobre a origem do Flet. O Flet é um projeto recente (da última década), não é de 1991.

## Por que usar Flet?
- Produtividade: poucos conceitos, curva de aprendizagem curta.
- Componentes prontos: textos, botões, campos, listas, diálogos, ícones, etc.
- Web e desktop: um único código que pode ser servido no navegador ou rodar de forma nativa (via runtime do Flet).
- Estilização: suporte a temas, cores e propriedades visuais de forma consistente.

## Instalação
```bash
pip install flet
```

## Conceitos essenciais
- Page: representa a “janela” da aplicação; onde você configura título, tema e adiciona os widgets.
- Widget: todo elemento visual (Text, ElevatedButton, TextField, etc.).
- Layout: organiza widgets em linha (Row), coluna (Column) e outros contêineres.
- Evento: interação do usuário (clique, digitação, mudança de valor) que dispara funções Python.
- Tema: define aparência global (modo claro/escuro, cores, tipografia).

## Estrutura típica
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Minha App Flet"
    # adicionar widgets e lógica aqui

ft.app(target=main)
```

---

# Exemplos práticos (originais)

Os exemplos abaixo são independentes. Salve cada um em um arquivo .py e execute com `python nome_do_arquivo.py`.

## 1) Contador com estado e layout responsivo
Mostra como manter estado, reagir a eventos e organizar a UI.
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Contador"
    page.theme_mode = "light"

    valor = ft.Text("0", size=32, weight=ft.FontWeight.BOLD)

    def incrementar(e):
        valor.value = str(int(valor.value) + 1)
        page.update()

    def decrementar(e):
        valor.value = str(int(valor.value) - 1)
        page.update()

    botoes = ft.Row([
        ft.ElevatedButton("-1", on_click=decrementar),
        ft.ElevatedButton("+1", on_click=incrementar),
    ], alignment=ft.MainAxisAlignment.CENTER)

    page.add(
        ft.Column([
            ft.Text("Contador simples", size=20),
            valor,
            botoes,
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
           expand=True)
    )

ft.app(target=main)
```

## 2) Formulário com validação básica
Demonstra campos de texto, validação e mensagens de feedback.
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Cadastro"

    nome = ft.TextField(label="Nome", autofocus=True)
    email = ft.TextField(label="Email")
    aviso = ft.Text(color=ft.colors.RED_400)

    def enviar(e):
        erros = []
        if not nome.value or len(nome.value.strip()) < 2:
            erros.append("Nome inválido")
        if not email.value or "@" not in email.value:
            erros.append("Email inválido")

        if erros:
            aviso.value = ", ".join(erros)
        else:
            aviso.value = "Cadastro enviado com sucesso!"
            aviso.color = ft.colors.GREEN_500
        page.update()

    page.add(
        ft.Column([
            ft.Text("Preencha seus dados", size=18, weight=ft.FontWeight.W_600),
            nome,
            email,
            ft.ElevatedButton("Enviar", icon=ft.icons.SEND, on_click=enviar),
            aviso,
        ], width=400)
    )

ft.app(target=main)
```

## 3) Lista de tarefas minimalista
Exemplo de manipulação de listas e eventos.
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Minhas Tarefas"

    entrada = ft.TextField(hint_text="Nova tarefa", expand=True)
    lista = ft.Column()

    def adicionar(e):
        if not entrada.value.strip():
            return
        chk = ft.Checkbox(label=entrada.value.strip())
        btn_remover = ft.IconButton(ft.icons.DELETE, tooltip="Remover")

        def remover(_):
            lista.controls.remove(linha)
            page.update()

        btn_remover.on_click = remover
        linha = ft.Row([chk, btn_remover], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
        lista.controls.append(linha)
        entrada.value = ""
        page.update()

    page.add(
        ft.Column([
            ft.Text("To‑do simples", size=20),
            ft.Row([entrada, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=adicionar)]),
            ft.Divider(),
            lista,
        ], width=500)
    )

ft.app(target=main)
```

## 4) Tema claro/escuro com alternância
Mostra como trocar o tema em tempo real.
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Tema Dinâmico"
    page.theme_mode = "light"

    status = ft.Text("Tema atual: Claro")

    def alternar_tema(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        status.value = f"Tema atual: {'Escuro' if page.theme_mode=='dark' else 'Claro'}"
        page.update()

    page.add(
        ft.Column([
            status,
            ft.Switch(label="Escuro", on_change=alternar_tema),
            ft.Text("Experimente alternar e ver as cores mudarem."),
        ], width=400)
    )

ft.app(target=main)
```

## 5) Diálogo modal e snackbar
Feedback ao usuário com componentes nativos de UI.
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Diálogo e Snackbar"

    dlg = ft.AlertDialog(title=ft.Text("Confirmação"), content=ft.Text("Deseja prosseguir?"))

    def abrir_dialogo(e):
        def on_result(r):
            page.snack_bar = ft.SnackBar(ft.Text(f"Resultado: {r}"))
            page.snack_bar.open = True
            page.update()

        dlg.actions = [
            ft.TextButton("Cancelar", on_click=lambda _: (setattr(dlg, 'open', False), on_result('cancelar'))),
            ft.ElevatedButton("OK", on_click=lambda _: (setattr(dlg, 'open', False), on_result('ok'))),
        ]
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.add(ft.ElevatedButton("Abrir diálogo", on_click= abrir_dialogo))

ft.app(target=main)
```
---

## Como fazer uma calculadora básica (Extra)

```
import flet as ft


def main(page: ft.Page):
    page.title = "Calculadora"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campos de texto para os valores
    valor1 = ft.TextField(label="Valor 1", width=300,
                          keyboard_type=ft.KeyboardType.NUMBER)
    valor2 = ft.TextField(label="Valor 2", width=300,
                          keyboard_type=ft.KeyboardType.NUMBER)

    # Dropdown para operação
    operacao = ft.Dropdown(
        label="Operação",
        width=300,
        options=[
            ft.dropdown.Option("soma", "Soma (+)"),
            ft.dropdown.Option("subtracao", "Subtração (-)"),
            ft.dropdown.Option("multiplicacao", "Multiplicação (×)"),
            ft.dropdown.Option("divisao", "Divisão (÷)"),
        ],
        value="soma",
    )

    resultado_txt = ft.Text("", size=20, visible=False)

    # Função para calcular
    def calcular(e):
        try:
            v1 = float(valor1.value)
            v2 = float(valor2.value)

            if operacao.value == "soma":
                resultado = v1 + v2
                op_simbolo = "+"
            elif operacao.value == "subtracao":
                resultado = v1 - v2
                op_simbolo = "-"
            elif operacao.value == "multiplicacao":
                resultado = v1 * v2
                op_simbolo = "×"
            elif operacao.value == "divisao":
                if v2 == 0:
                    mostrar_msg("Não é possível dividir por zero!", erro=True)
                    return
                resultado = v1 / v2
                op_simbolo = "÷"
            else:
                mostrar_msg("Selecione uma operação válida.", erro=True)
                return

            mostrar_msg(f"{v1} {op_simbolo} {v2} = {resultado}")
        except ValueError:
            mostrar_msg(
                "Por favor, insira valores numéricos válidos!", erro=True)

    def mostrar_msg(texto, erro=False):
        resultado_txt.value = texto
        resultado_txt.color = ft.Colors.RED if erro else ft.Colors.GREEN
        resultado_txt.visible = True
        page.update()

    btn_calcular = ft.ElevatedButton(
        text="Calcular", width=300, on_click=calcular)

    page.add(
        ft.Column(
            [
                ft.Text("Calculadora", size=30, weight=ft.FontWeight.BOLD),
                valor1,
                valor2,
                operacao,
                btn_calcular,
                resultado_txt,  # fica abaixo do botão
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


ft.app(target=main)


```
---

## Dicas finais
- Comece simples: uma página, poucos widgets, e evolua iterativamente.
- Nomeie funções de eventos de forma clara (ex.: `enviar`, `incrementar`).
- Use `page.update()` sempre que mudar valores de widgets para refletir na UI.
- Consulte a documentação oficial para ver a lista de widgets e propriedades.

## Ideias de prática
- Formulário de cadastro com máscara/validação extra e persistência em arquivo JSON.
- To‑do com filtros (todas, ativas, concluídas) e contagem de tarefas.
- Calculadora com histórico de operações.
- Bloco de notas com salvar/abrir arquivo.

Boa prática e divirta‑se construindo UIs com Flet!
