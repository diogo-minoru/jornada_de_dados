### Desafio - Refatorar o projeto da aula 1 evitando Bugs!

# 1) Solicita ao usuário o nome
def nome_usuario():
    while True:
        try:
            nome = input("Digite o seu nome: ")
            print(f"Olá {nome}.")
            solicitar_salario()
            break
        except ValueError:
            print("Não são permitidos números")

# 2) Solicita ao usuário que digite o valor do seu salário
def solicitar_salario():
    while True:
        try:
            salario = float(input("Informe o seu salário atual: "))
            solicitar_bonus()
            break
        except ValueError:
            print("Apenas números são permitidos.")

# 3) Solicita ao usuário que digite o valor do bônus recebido
def solicitar_bonus():
    while True:
        try:
            bonus = float(input("Digite o valor do bonus recebido: "))
            calculo_bonus_final()
        except ValueError:
            print("Apenas números são permitidos.")

# 4) Calcule o valor do bônus final
def calculo_bonus_final():
    bonus_final = salario * bonus

# 5) Imprima cálculo do KPI para o usuário
print(f"Salario de {salario} + {bonus} = {bonus_final}")

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome} seu salario final será de {bonus_final}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# Digitar texto no valor do salário
# Digitar porcentagem utilizando vírgula e não ponto
# Não digitar nenhum valor de salário ou bônus