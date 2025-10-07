# Interface gráfica com Flet II

Este README resume a Aula 10 (Interface gráfica com Flet II) e traz exemplos práticos de estilização, temas, responsividade, além de componentes de seleção (Dropdown/Radio) e tabela (DataTable).

## Sumário
- Fundamentos de estilização
- Cores e fontes
- Temas globais
- Estilização reutilizável (“CSS-like mindset”)
- Responsividade
- Exemplos práticos:
  - Dropdown estilizado
  - RadioGroup
  - DataTable com ações
  - DataTable com seleção de linhas

## Requisitos
- Python 3.9+
- Biblioteca Flet
```bash
pip install flet
```

## Fundamentos de Estilização
Aplique propriedades diretamente nos widgets:
- color (texto), bgcolor (fundo)
- size, weight (negrito), italic
- padding, margin

Exemplo:
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Estilização Básica"
    page.add(
        ft.Text("Texto azul", color="blue"),
        ft.ElevatedButton("Botão verde", bgcolor="green", color="white")
    )

ft.app(target=main)
```

## Cores e Fontes
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Cores e Fontes"
    page.add(
        ft.Text("Vermelho 20px", color="red", size=20),
        ft.Text("Azul negrito 24px", color="blue", weight="bold", size=24),
        ft.Text("Verde itálico 18px", color="green", italic=True, size=18),
    )

ft.app(target=main)
```

## Temas Globais
Use `ft.Theme` e `ft.ColorScheme` para consistência:
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Tema Personalizado"
    page.theme = ft.Theme(
        color_scheme = ft.ColorScheme(
            primary=ft.colors.BLUE,
            secondary=ft.colors.GREEN,
            background=ft.colors.WHITE,
            surface=ft.colors.GREY,
            on_primary=ft.colors.WHITE,
            on_secondary=ft.colors.WHITE,
            on_background=ft.colors.BLACK,
            on_surface=ft.colors.BLACK,
        )
    )
    page.add(
        ft.Text("Texto com tema"),
        ft.ElevatedButton("Botão com tema")
    )

ft.app(target=main)
```

## Estilização Reutilizável (“CSS-like mindset”)
Padronize estilos via funções utilitárias:
```python
import flet as ft

PRIMARY_BG = ft.colors.ORANGE
PRIMARY_FG = ft.colors.WHITE

def primary_button(text):
    return ft.ElevatedButton(text, bgcolor=PRIMARY_BG, color=PRIMARY_FG)

def main(page: ft.Page):
    page.title = "Estilo Reutilizável"
    page.add(
        ft.Text("Texto azul e negrito", color=ft.colors.BLUE, weight=ft.FontWeight.BOLD),
        primary_button("Botão Estilizado"),
    )

ft.app(target=main)
```

## Responsividade
```python
import flet as ft

def main(page: ft.Page):
    c = ft.Container(
        content=ft.Text("Texto responsivo"),
        padding=10,
        margin=ft.Margin(20, 5, 20, 5),
        width=page.width / 2,
        height=page.height / 4,
        bgcolor=ft.colors.BLUE_50
    )
    page.add(c)

ft.app(target=main)
```

## Exemplos de Seleção

### Dropdown estilizado
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Campo de Seleção Estilizado"

    def on_change(e):
        result.value = f"Selecionado: {e.control.value}"
        page.update()

    dropdown = ft.Dropdown(
        label="Escolha uma linguagem",
        options=[ft.dropdown.Option(x) for x in ["Python", "JavaScript", "Go", "Rust"]],
        value="Python",
        bgcolor=ft.colors.BLUE_50,
        color=ft.colors.BLUE_900,
        border_color=ft.colors.BLUE,
        focused_border_color=ft.colors.ORANGE,
        border_radius=8,
        on_change=on_change
    )

    result = ft.Text("Selecionado: Python", size=16, weight="bold", color=ft.colors.BLUE_GREY_900)
    page.add(ft.Text("Exemplo: Dropdown", size=20, weight="bold"), dropdown, result)

ft.app(target=main)
```

### RadioGroup
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Seleção com RadioGroup"

    def changed(e):
        info.value = f"Tema: {rg.value}"
        page.update()

    rg = ft.RadioGroup(
        content=ft.Column([ft.Radio(value=v, label=v) for v in ["Claro", "Escuro", "Sistema"]]),
        value="Claro",
        on_change=changed
    )
    info = ft.Text("Tema: Claro", color=ft.colors.BLACK, weight="bold")

    page.add(ft.Text("Escolha o tema:", size=18), rg, info)

ft.app(target=main)
```

## Exemplos de Tabela (DataTable)

### Tabela com ação “Ver”
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Tabela com Estilo e Ações"

    dados = [
        {"id": 1, "nome": "Alice", "email": "alice@example.com"},
        {"id": 2, "nome": "Bruno", "email": "bruno@example.com"},
        {"id": 3, "nome": "Clara", "email": "clara@example.com"},
    ]

    info = ft.Text("", size=14, color=ft.colors.BLUE_GREY_800)

    def ver_detalhes(e):
        row = e.control.data
        info.value = f"Detalhes -> ID: {row['id']} | {row['nome']} | {row['email']}"
        page.update()

    tabela = ft.DataTable(
        bgcolor=ft.colors.GREY_50,
        heading_row_color=ft.colors.BLUE_100,
        heading_text_style=ft.TextStyle(weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900),
        border=ft.border.all(1, ft.colors.GREY_300),
        columns=[ft.DataColumn(ft.Text(c)) for c in ["ID", "Nome", "E-mail", "Ação"]],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Text(str(item["id"]))),
                ft.DataCell(ft.Text(item["nome"])),
                ft.DataCell(ft.Text(item["email"])),
                ft.DataCell(ft.TextButton(
                    "Ver",
                    icon=ft.icons.VISIBILITY,
                    style=ft.ButtonStyle(color=ft.colors.BLUE_700, overlay_color=ft.colors.BLUE_50),
                    data=item,
                    on_click=ver_detalhes
                )),
            ])
            for item in dados
        ],
    )

    page.add(
        ft.Text("Exemplo: DataTable", size=20, weight="bold"),
        tabela,
        ft.Divider(),
        info,
    )

ft.app(target=main)
```

### Tabela com seleção de linhas e totalização
```python
import flet as ft

def main(page: ft.Page):
    page.title = "Tabela com Seleção de Linhas"

    dados = [
        {"id": 1, "produto": "Notebook", "preco": 4500.00},
        {"id": 2, "produto": "Mouse", "preco": 120.90},
        {"id": 3, "produto": "Teclado", "preco": 299.50},
    ]

    selecionados = set()
    total = ft.Text("Total selecionado: R$ 0,00", weight="bold")

    def toggle_row(e):
        item = e.control.data
        if e.control.value:
            selecionados.add(item["id"])
        else:
            selecionados.discard(item["id"])
        soma = sum(i["preco"] for i in dados if i["id"] in selecionados)
        total.value = f"Total selecionado: R$ {soma:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        page.update()

    tabela = ft.DataTable(
        heading_row_color=ft.colors.GREEN_100,
        columns=[ft.DataColumn(ft.Text(c)) for c in ["Sel.", "ID", "Produto", "Preço (R$)"]],
        rows=[
            ft.DataRow(cells=[
                ft.DataCell(ft.Checkbox(value=False, on_change=toggle_row, data=item)),
                ft.DataCell(ft.Text(str(item["id"]))),
                ft.DataCell(ft.Text(item["produto"])),
                ft.DataCell(ft.Text(f"{item['preco']:.2f}".replace(".", ","))),
            ])
            for item in dados
        ],
    )

    page.add(
        ft.Text("Carrinho (seleção por linha)", size=20, weight="bold"),
        tabela,
        ft.Container(padding=10),
        total,
    )

ft.app(target=main)
```

## Atividades sugeridas
- Três textos com estilos diferentes.
- Três botões com estilos variados.
- Formulário estilizado (nome, e-mail e botão).
- Tela com tema personalizado aplicado.

## Licença
Defina a licença do seu projeto (ex.: MIT).

## Autor
Seu nome aqui.
