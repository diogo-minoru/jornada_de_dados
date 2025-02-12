import csv

path = "arquivo.csv"
arquivo_csv = []

with open(file = path, mode = "r", encoding = "UTF-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)