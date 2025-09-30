# Resumo Aula 08 - Revisão Geral

Nesta aula foram revisados os principais conceitos de **listas, tuplas,
dicionários, conjuntos, funções, módulos, bibliotecas** e **funções
agregadoras** no Python.

## Listas e Tuplas

-   **Listas**: Estruturas ordenadas e mutáveis. Podemos adicionar,
    remover e modificar elementos.
    -   Exemplo:

        ``` python
        lista = [1, 2, 3]
        lista.append(4)  # [1, 2, 3, 4]
        lista.remove(2)  # [1, 3, 4]
        ```
-   **Tuplas**: Estruturas ordenadas e **imutáveis**.
    -   Exemplo:

        ``` python
        tupla = (1, 2, 3)
        print(tupla[0])  # 1
        ```

## Dicionários e Conjuntos

-   **Dicionários**: Pares chave-valor únicos.
    -   Exemplo:

        ``` python
        produto = {"nome": "Teclado", "preco": 100, "estoque": 20}
        print(produto["nome"])  # Teclado
        ```
-   **Conjuntos (set)**: Elementos únicos, sem ordem, permitem operações
    como união e interseção.
    -   Exemplo:

        ``` python
        cores = {"azul", "verde", "vermelho"}
        cores.add("amarelo")
        ```

## Funções

-   Blocos de código reutilizáveis definidos com `def`.
-   Podem receber **args** (argumentos posicionais) e **kwargs**
    (argumentos nomeados).
    -   Exemplo:

        ``` python
        def saudacao(nome, mensagem="Olá"):
            return f"{mensagem}, {nome}!"
        print(saudacao("Carlos"))  # Olá, Carlos!
        ```

## Módulos e Bibliotecas

-   **Módulo**: arquivo `.py` com funções reutilizáveis.
-   **Biblioteca**: conjunto de módulos prontos.
    -   Exemplo:

        ``` python
        import math
        print(math.sqrt(16))  # 4.0
        ```

## Funções Agregadoras

Usadas para resumir informações de coleções de dados. - `sum(lista)` →
soma - `max(lista)` e `min(lista)` → maior e menor valor - `len(lista)`
→ quantidade de elementos - `any(lista)` → True se algum elemento for
verdadeiro - `all(lista)` → True se todos forem verdadeiros -
`sorted(lista)` → retorna lista ordenada

Exemplo:

``` python
vendas = [100, 200, 150, 300]
print(sum(vendas))   # 750
print(max(vendas))   # 300
print(min(vendas))   # 100
```

------------------------------------------------------------------------

# Dicas finais

-   **Explorar** diferentes códigos.
-   **Perguntar** sempre o porquê.
-   **Revisar** ensinando a alguém.
-   **Praticar** constantemente.
