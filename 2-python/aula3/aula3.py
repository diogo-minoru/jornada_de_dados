### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

def qualidade_de_dados(quantidade, preco):
    if quantidade > 0 and preco > 0:
        print("Valores corretos!")
    else:
        print("Valores incorretos!")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

def sensor_temperatura(temperatura):
    if temperatura < 18:
        print("Baixa")
    elif temperatura < 25:
        print("Normal")
    else:
        print("Alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

registro = [{'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão hahaha'}, {'timestamp': '2022-06-23 10:00:00', 'level': 'NORMAL', 'message': 'Conexão Normal'}]

def severidade_log(logs):
    for log in logs:
        if log["level"] == "ERROR":
            print(log["message"])
            pass

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

import re

def validar_usuario(idade, email):
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not (18 <= idade <= 65):
        return print("Erro: Idade fora do intervalo permitido (18-65 anos).")
    elif not re.match(padrao_email, email):
        return print("Erro: E-mail inválido.")

"""
idade = int(input("Digite a idade: "))
email = input("Digite o e-mail: ")
validar_usuario(idade, email)    
"""
### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

def anomalias(transacoes):
    for transacao in transacoes:
        if transacao["valor"] > 10000 or (transacao["hora"] > 20 and transacao["hora"] < 9):
            print("Transacao Suspeita.")
        else:
            print("Transacao normal.")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

import re
from collections import Counter

def contar_palavras(texto):
    texto_formatado = re.sub(r"[^a-zA-Z0-9\s]", "", texto, 0, re.IGNORECASE)
    palavras = texto_formatado.split()
    contagem = Counter(palavras)
    print(contagem)
    for palavra, quantidade in contagem.items():
        print(palavra, quantidade)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

def normalizar(lista):
    lista_normalizada = list()
    for i in lista:
        lista_normalizada.append(i/lista[0])
    return print(lista_normalizada)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando



### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

def retornar_pares(lista):
    pares = list()
    for n in lista:
        if n % 2 == 0:
            pares.append(n)
    print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
"""
compras = {
    1: {"Item": "Queijo", "Categoria": "Laticínios", "Quantidade": 4},
    2: {"Item": "Banana", "Categoria": "Hortifruti", "Quantidade": 1},
    3: {"Item": "Frango", "Categoria": "Carnes", "Quantidade": 3},
    4: {"Item": "Refrigerante", "Categoria": "Bebidas", "Quantidade": 4},
    5: {"Item": "Cenoura", "Categoria": "Hortifruti", "Quantidade": 3},
    6: {"Item": "Água", "Categoria": "Bebidas", "Quantidade": 1},
    7: {"Item": "Sabão em pó", "Categoria": "Limpeza", "Quantidade": 4},
    8: {"Item": "Peixe", "Categoria": "Carnes", "Quantidade": 1},
    9: {"Item": "Alface", "Categoria": "Hortifruti", "Quantidade": 3},
    10: {"Item": "Manteiga", "Categoria": "Laticínios", "Quantidade": 4}
}

soma_categorias = {}

for i in compras.values():
    categoria = i["Categoria"]
    quantidade = i["Quantidade"]
    soma_categorias[categoria] = soma_categorias.get(categoria, 0) + quantidade

print(soma_categorias)
"""
### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

def funcao_sair():
    while True:
        entrada = input("Digite 'Sair' para sair do loop.: ")
        if entrada.lower() == "sair":
            print("Você saiu do loop!!")
            break
        else:
            pass

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

def numero_intervalo():
    while True:
        entrada = float(input("Digite um número entre 1 e 100: "))
        if 1 <= entrada <= 100:
            print(f"Você digitou o número {entrada}, portanto sairá do loop.")
            break
        else:
            print("Você digitou um número fora do intervalo, digite novamente.")
            
### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

def consumir_paginas(paginas):
    while True:
        for pagina in range(paginas + 1):
            entrada = input("Deseja ir para a próxima página? (s/n): ")
            if entrada.lower() == "s" and pagina <= paginas + 1:
                print(f"Você está na página {pagina}")
                print(f"Você irá para a página {pagina + 1}")
            elif entrada.lower() == "n":
                print("Você cancelou a operação.")
                break
            else:
                print("Você já consumiu todas as páginas.")
                break
            pagina += 1

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

import random

def conexao_servidor():
    numero_tentativas = 1
    while numero_tentativas <= 10:
        numero_aleatorio = random.randint(1, 20)
        if numero_aleatorio == 10:
            print("Conexão realizada com sucesso!")
            break
        else:
            print("Conexão falhou, tentando novamente.")
            print(f"Número de tentativas {numero_tentativas}")
            if numero_tentativas == 10:
                print("Tentativas máximas alcançadas, tente novamente mais tarde.")
        
        numero_tentativas += 1

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

import random

numeros_aleatorios = [random.randint(1, 100) for _ in range(20)]

def encontrar_numero(numero):
    for i in numeros_aleatorios:
        if numero not in numeros_aleatorios:
            print(numeros_aleatorios)
            print(f"O número desejado {numero} não está na lista.")
            break
        elif i == numero:
            print(numeros_aleatorios)
            print(f"Você encontrou o número desejado {numero} na posição {numeros_aleatorios.index(i)}")
