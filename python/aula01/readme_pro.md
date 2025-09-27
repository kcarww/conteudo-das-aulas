# Aula 01 – Revisão de Condicionais e Estruturas de Repetição (Python)

## 📌 Conteúdo Revisado
1. **Condicionais (if, elif, else)**  
2. **Laço de repetição – while**  
3. **Laço de repetição – for**  
4. **Break e Continue**  
5. **Atividades práticas**  
6. **Introdução à Aula 02: Listas e Tuplas**

---

## 🔹 Condicionais (if / elif / else)
As condicionais permitem **tomar decisões** no código com base em comparações lógicas.

```python
idade = 19

if idade < 18:
    print("Você é menor de idade")
elif idade <= 19:
    print("Você tem 18 ou 19 anos")
else:
    print("Você é maior de 19 anos")
```

➡️ **Exemplo adicional:**  

```python
nota = 7
if nota >= 6:
    print("Aprovado ✅")
else:
    print("Reprovado ❌")
```

---

## 🔹 Laço de Repetição – while
Executa instruções **enquanto uma condição for verdadeira**.

```python
contador = 0
while contador < 5:
    print(f"Contador vale {contador}")
    contador += 1
```

➡️ **Observação importante:** loops `while True` rodam infinitamente até um `break` ou interrupção manual (`Ctrl+C`).

---

## 🔹 Laço de Repetição – for
O `for` percorre sequências ou intervalos, automatizando repetições.

```python
for i in range(5):  # de 0 até 4
    print(i)
```

➡️ **Exemplo com passo personalizado:**  
```python
for i in range(0, 11, 2):  # de 0 até 10, de 2 em 2
    print(i)
```

---

## 🔹 Break e Continue
- **break** → encerra o loop.  
- **continue** → pula a iteração atual e passa para a próxima.  

```python
# Usando break
for i in range(10):
    if i == 5:
        break
    print(i)

# Usando continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # imprime apenas ímpares
```

---

## 📝 Atividades Práticas
1. Classificar pessoa pela idade (criança, adolescente, adulto, idoso).  
2. Ler três números e informar o maior e o menor.  
3. Pedir 10 números e contar pares vs ímpares.  
4. Calcular média de idades de uma turma e classificar como jovem, adulta ou idosa.  
5. Ler N números e determinar menor, maior e soma.

➡️ **Desafio:** criar um gerenciador de compras que calcule:
- Total gasto,  
- Quantos produtos custam mais de R$1000,  
- Nome do produto mais barato.  

---

## 📚 Dicas de Aprendizado
- Explore e teste livremente seu código.  
- Pergunte “por quê?” para entender a lógica.  
- Revise e ensine a alguém (ótima forma de aprender).  
- Pratique! Quanto mais exercícios, mais natural será programar.  

---

## 🚀 Próxima Aula (Aula 02)
- **Listas e Tuplas** → estruturas para armazenar múltiplos valores.  
Exemplo:
```python
lista_de_numeros = [1, 2, 3, 4, 5]
lista_de_letras = ['a', 'b', 'c']
lista_de_booleanos = [True, False, True]
```
