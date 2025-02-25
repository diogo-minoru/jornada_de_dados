def retornar_soma(valor1: float, valor2: float) -> float:
    """
    Função para retornar a soma de dois valores float
    """
    return valor1 + valor2

# 1. Calcular Média de Valores em uma Lista
def retornar_media():
    lista_numeros = []
    while True:
        numero = input("Digite o número para adicionar na lista: ")
        if numero.isdigit():
            lista_numeros.append(float(numero))
        else:
            return print(sum(lista_numeros)/len(lista_numeros))

# 2. Filtrar Dados Acima de um Limite
def filtrar_dados(lista_valores: list, limite: float) -> list:
    lista_filtrada = []
    for valor in lista_valores:
        if valor <= limite:
            lista_filtrada.append(valor)
        else:
            pass
    return print(lista_filtrada)

# 3. Contar Valores Únicos em uma Lista
def contar_distintos(lista_valores: list):
    return print(len(set(lista_valores)))

# 4. Converter Celsius para Fahrenheit em uma Lista
def converter_temperatura(celcius: list[float]):
    return print([(temperatura * 9/5) + 32 for temperatura in celcius])

# 5. Calcular Desvio Padrão de uma Lista
def calcular_desvio_padrao(valores: list[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

# 6. Encontrar Valores Ausentes em uma Sequência
def encontrar_valores_ausentes(sequencia: list[int]) -> list[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))