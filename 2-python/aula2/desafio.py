### Desafio - Refatorar o projeto da aula 1 evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
nome = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
salario = float(input("Digite o seu salário atual: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
bonus = float(input("Digite o valor do bonus recebido: "))

# 4) Calcule o valor do bônus final
bonus_final = salario * bonus

# 5) Imprima cálculo do KPI para o usuário
print(f"Salario de {salario} + {bonus} = {bonus_final}")

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome} seu salario final será de {bonus_final}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
# Digitar texto no valor do salário
# Digitar porcentagem utilizando vírgula e não ponto
# Não digitar nenhum valor de salário ou bônus