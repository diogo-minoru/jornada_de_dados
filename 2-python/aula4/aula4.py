# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista = list(range(1, 11))

for i in lista:
    print(i)
# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista = ["Python", "Java", "C++", "JavaScript"]

lista.pop(lista.index("C++"))
lista.append("Ruby")
print(lista)
# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro = {
    "Título": "O Conde de Monte Cristo",
    "Autor": "Alexandre Dumas",
    "Ano": "1844"
}

for key, value in livro.items():
    print(f"{key}: {value}")

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(texto):
    contagem = {}
    for caractere in texto:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem


# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)

print(f"Preço total: {total}")