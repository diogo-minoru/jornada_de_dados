import pandas as pd
import os
import glob

def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df = [pd.read_json(arquivo, typ="series") for arquivo in arquivos_json]
    df_concat = pd.concat(df, ignore_index = True)
    return df_concat

df_copia = 

if __name__ == "__main__":
    path = "data"
    print(extrair_dados(path))