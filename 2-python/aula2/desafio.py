### Desafio - Refatorar o projeto da aula 1 evitando Bugs!

# 1) Solicita ao usuário o nome
def nome_usuario():
    while True:
        nome = input("Digite o seu nome: ")
        if nome.replace(" ", "").isalpha():
            print(f"Olá {nome}.")
            break
        else:
            print("Não são permitidos números")

# 2) Solicita ao usuário que digite o valor do seu salário
def solicitar_salario():
    while True:
        salario = input("Informe o seu salário atual: ")
        if salario.isdigit():
            print(f"Salário informado: {salario}")
            return float(salario)
        else:
            print("Apenas números são permitidos para o salário.")
        

# 3) Solicita ao usuário que digite o valor do bônus recebido
def solicitar_bonus():
    while True:
        bonus = input("Digite o valor do bonus recebido (%): ")
        if bonus.isdigit():
            print(f"Bônus informado: {bonus}")
            return float(bonus)
        else:
            print("Apenas números são permitidos para o bônus.")
        

# 4) Calcule o valor do bônus final
def calculo_bonus_final():
    nome = nome_usuario()
    salario = solicitar_salario()
    bonus = solicitar_bonus()
    bonus_final = salario * (bonus/100)
    print(f"{nome} considerando o salário de R${salario} e o bônus de {bonus} %, o seu bônus final será de R$ {bonus_final}, resultando um total de R$ {salario + bonus_final}")

calculo_bonus_final()