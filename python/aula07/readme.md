# 📘 Aula 07 - Módulos e Bibliotecas (Python)

## 📌 O que você vai aprender
1. O que são **Módulos**
2. Como **importar módulos** no Python
3. O que são **Bibliotecas**
4. Exemplos práticos de uso
5. Atividades e desafios

---

## 🔹 Módulos
- Um **módulo** é um arquivo `.py` que pode conter funções, classes e variáveis.
- Eles ajudam a **organizar** o código e facilitar a **reutilização**.

### Exemplo: Criando e importando um módulo
**meu_modulo.py**
```python
def saudacao(nome):
    return f"Olá, {nome}!"
```

**main.py**
```python
import meu_modulo

mensagem = meu_modulo.saudacao("Alice")
print(mensagem)  # Olá, Alice!
```

---

## 🔹 Como importar módulos no Python
| Modo de Importação | Exemplo |
|--------------------|---------|
| Importando todo o módulo | `import modulo` |
| Importando função específica | `from modulo import funcao` |
| Importando várias funções | `from modulo import (func1, func2)` |
| Importando todas as funções | `from modulo import *` |
| Importando de pacote externo | `from pacote.modulo import funcao` |
| Usando apelido (alias) | `import modulo as apelido` |

---

## 🔹 Bibliotecas
- Coleções de módulos que oferecem **funcionalidades prontas**.
- Podem ser:
  - **Biblioteca padrão** (vem com Python, ex: `math`, `random`)
  - **Bibliotecas de terceiros** (instaladas com `pip`, ex: `numpy`, `pandas`, `requests`).

### Exemplo com `math`
```python
import math

num = 5.6
print(math.sqrt(9))         # Raiz quadrada => 3.0
print(math.ceil(num))       # Arredonda para cima => 6
print(math.floor(num))      # Arredonda para baixo => 5
```

### Exemplo com `random`
```python
import random

lista = ["maçã", "banana", "uva", "laranja"]
print(random.choice(lista))  # Escolhe elemento aleatório
```

---

## 🏋️‍♂️ Atividades Práticas
1. **Calculadora Modular**  
   - Criar um módulo com funções matemáticas e um arquivo principal que exibe um menu de operações.

2. **Manipulação de Strings**  
   - Criar um módulo com funções para inverter string, contar palavras e verificar palíndromos.

3. **Uso de Math**  
   - Programa para calcular área e perímetro de figuras geométricas usando `math`.

4. **Jogo da Adivinhação**  
   - Usar `random` para sortear um número que o usuário deve adivinhar.

5. **Conversor de Unidades**  
   - Criar funções em módulos para conversão (ex: metros ↔ pés, °C ↔ °F).

---

## 🚀 Desafio Final
**Gerenciador de Biblioteca de Livros**  
- Adicionar livros (título, autor, nº de cópias)  
- Listar livros disponíveis  
- Fazer empréstimos  
- Registrar devoluções  
- Verificar disponibilidade e listagem de empréstimos por usuário  

---

## 📚 Resumo
- **Módulos** ajudam a organizar o código.
- **Bibliotecas** aceleram o desenvolvimento com funções prontas.
- Importações podem ser feitas de várias formas, com otimizações para legibilidade.
- A prática é essencial para dominar módulos e bibliotecas.  
