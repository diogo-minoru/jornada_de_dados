# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
"""
def retornar_soma():
    resultado = int(input("Digite o primeiro número: ")) + int(input("Digite o segundo número: "))
    return print(resultado)
"""

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
"""
def resto_divisao():
    numero = int(input("Digite o valor que deseja dividir por 5: "))
    resultado = numero % 5
    return print(resultado)
"""

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
"""
def multiplicador():
    resultado = int(input("Digite o primeiro número que deseja multiplicar: ")) * int(input("Digite o segundo número que deseja multiplicar: "))
    return print(resultado)
"""

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
"""
def divisao_inteira():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    resultado = int(n1 // n2)
    return print(f"A divisão inteira de {n1} por {n2} é: {resultado}")
"""

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
"""
def retorna_quadrado():
    resultado = int(input("Digite o valor que deseja elevar ao quadrado: "))
    return print(resultado ** 2)
"""

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
"""
def retornar_soma():
    resultado = float(input("Digite o primeiro número: ")) + float(input("Digite o segundo número: "))
    return print(resultado)
"""

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
"""
def retornar_media():
    resultado = float(input("Digite o primeiro número: ")) + float(input("Digite o segundo número: "))
    return print(resultado/2)
"""

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
"""
def retorna_potencia():
    resultado = float(input("Digite o número base: ")) ** float(input("Digite o número da potência: "))
    return print(resultado)
"""

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
"""
def conversao_temperatura():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * (9/5)) + 32
    return print(fahrenheit)

conversao_temperatura()
"""

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
"""
import math

def raio_circulo():
    raio = float(input("Digite o raio do círculo: "))
    resultado = math.pi * raio ** 2
    print(f"A área do círculo é de: {resultado}")
"""

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
