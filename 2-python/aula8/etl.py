import pandas as pd
import os
import glob

def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_concat = pd.concat(df, ignore_index = True)
    return df_concat

def calcular_total(dataframe: pd.DataFrame) -> pd.DataFrame:
    dataframe["Total"] = dataframe["Quantidade"] * dataframe["Venda"]
    return dataframe

def carregar_dados(dataframe: pd.DataFrame, formato_saida = 1):
    formato_saida = int(input("Escolha o formato de saída do arquivo: \n 1: .csv \n 2: .parquet \n 3: ambos \n"))
    if formato_saida == 1:
        dataframe.to_csv("dados.csv", index = False)
        print("Dados foram salvos com sucesso no formato .csv")
    elif formato_saida == 2:
        dataframe.to_parquet("dados.parquet", index = False)
        print("Dados foram salvos com sucesso no formato .parquet")
    else:
        dataframe.to_csv("dados.csv", index = False)
        dataframe.to_parquet("dados.parquet", index = False)
        print("Dados foram salvos com sucesso no formato .parquet e .csv")

def pipeline_calculo_vendas(pasta):
    dataframe_extraido = extrair_dados(pasta)
    dataframe_resultado = calcular_total(dataframe_extraido)
    dataframe_saida = carregar_dados(dataframe_resultado)
