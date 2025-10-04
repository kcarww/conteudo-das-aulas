
# Aula 02 — Listas e Tuplas (Resumo + Exemplos)

Este README resume os principais conceitos de listas e tuplas em Python, com explicações em linguagem simples e exemplos próprios.

## 1) Listas (list)
- Estrutura mutável: você pode adicionar, remover e alterar elementos.
- Aceitam elementos de tipos variados (int, float, str, bool, etc.).
- Índices começam em 0; índices negativos contam a partir do fim.

### Exemplos rápidos
```python
# Lista mista
perfil = ["Patrícia", 27, True]

# Acesso por índice
print(perfil[0])    # "Patrícia"
print(perfil[-1])   # True (último elemento)

# Alterando valores (mutável)
perfil[1] = 28

# Adicionando itens
nums = [10, 20, 30]
nums.append(40)           # [10, 20, 30, 40]
nums.insert(1, 15)        # [10, 15, 20, 30, 40]

# Removendo itens
nums.remove(20)           # remove pelo valor -> [10, 15, 30, 40]
removido = nums.pop(2)    # remove por índice -> removido=30, lista=[10, 15, 40]
```

### Percorrendo listas com for
```python
compras = ["arroz", "feijão", "ovos"]
for item in compras:
    print("-", item)
```

## 2) Tuplas (tuple)
- Estrutura imutável: depois de criada, não dá para alterar, inserir ou remover.
- Úteis quando você quer proteger dados de mudanças acidentais ou usar como chaves em dicionários.
- Sintaxe: parênteses `( )` (ou apenas vírgulas em alguns casos).

### Exemplos rápidos
```python
# Tupla de coordenadas (imutável)
coordenada = (12.5, -3.2)
print(coordenada[0])  # 12.5

# Métodos úteis
frutas = ("maçã", "banana", "laranja", "banana")
print(frutas.index("laranja"))  # 2 (primeira ocorrência)
print(frutas.count("banana"))   # 2

# Desempacotamento
x, y = coordenada
print(x, y)  # 12.5 -3.2
```

## 3) Quando usar cada um?
- Use lista quando precisar mudar os dados (adicionar/remover/alterar) ou quando a ordem muda com frequência.
- Use tupla quando os dados são fixos, representam um registro estático (ex.: coordenadas, dimensões, configurações),
  ou quando quer evitar alterações acidentais.

## 4) Exercícios propostos (idéias)
1. Crie uma lista com as 5 primeiras consoantes e imprima a terceira.
2. Dada a lista de notas `[9.5, 7.8, 8.2, 10.0]`, use `append`, `insert`, `remove` e `pop` para praticar.
3. Crie uma tupla `palestrante = (nome, tema, instituicao)` e faça o desempacotamento.

## 5) Mini-desafio (médias e classificação)
Suponha `resultados = [("Time A", [10, 8, 9]), ("Time B", [7, 7, 8]), ("Time C", [9, 9, 10])]`.

Objetivo: calcular a média de cada time, ordenar em ordem decrescente e exibir a classificação.

Solução sugerida:
```python
resultados = [
    ("Time A", [10, 8, 9]),
    ("Time B", [7, 7, 8]),
    ("Time C", [9, 9, 10]),
]

# 1) Médias
medias = []
for nome, pontuacoes in resultados:
    media = sum(pontuacoes) / len(pontuacoes)
    medias.append((nome, media))

# 2) Ordenar por média (desc)
medias.sort(key=lambda x: x[1], reverse=True)

# 3) Exibir classificação
for pos, (nome, media) in enumerate(medias, start=1):
    print(f"{pos}º - {nome}: {media:.2f}")
```

## 6) Dicas finais
- Prefira `append` para adicionar ao fim e `insert` para posições específicas.
- Use `remove` quando souber o valor; `pop` quando souber o índice (e quiser o retorno do removido).
- Com tuplas, pense em "pacotes imutáveis" de dados (campos fixos).

---
Feito por GPT-5 (Abacus.AI) — Resumo autoral com exemplos próprios.
