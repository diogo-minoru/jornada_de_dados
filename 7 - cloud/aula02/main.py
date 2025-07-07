import boto3
from dotenv import load_dotenv
from typing import List
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações da AWS a partir do .env
AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION: str = os.getenv('AWS_REGION')
BUCKET_NAME: str = os.getenv('BUCKET_NAME')

# Print para verificar se as variáveis de ambiente foram carregadas corretamente
print(f"AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID}")
print(f"AWS_SECRET_ACCESS_KEY: {AWS_SECRET_ACCESS_KEY}")
print(f"AWS_REGION: {AWS_REGION}")
print(f"BUCKET_NAME: {BUCKET_NAME}")

# Instanciar client s3
try:
    s3_client = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )
    print("Cliente S3 configurado com sucesso.")
except Exception as e:
    print("Não foi possível inicializar o cliente.")
    raise

# Ler Arquivos
def ler_arquivos(pasta: str) -> List[str]:
    try:
        arquivos: List[str] = []
        for arquivo in os.listdir(pasta):
            caminho_completo = os.path.join(pasta, arquivo)
            if os.path.isfile(caminho_completo):
                arquivos.append(caminho_completo)
        print("Arquivos lidos com sucesso.")
    except Exception as e:
        raise
    return arquivos

# Upload arquivos para bucket
def upload_arquivos(arquivos: List[str]) -> None:
    try:
        for arquivo in arquivos:
            nome_arquivo = str = os.path.basename(arquivo)
            s3_client.upload_file(arquivo, BUCKET_NAME, nome_arquivo)
            print(f"Arquivo {nome_arquivo}, upado para o bucket")
    except Exception as e:
        print(f"Não foi possível realizar o upload do arquivo {arquivo} no bucket {BUCKET_NAME}: {e}")
        raise

# Deletar arquivos na pasta local
def deletar_arquivos(arquivos: List[str]) -> None:
    try:
        for arquivo in arquivos:
            os.remove(arquivo)
            print(f"Arquivo {arquivo} deletado da pasta")
    except Exception as e:
        print("Não foi possível deletar o arquivo")
        raise

# Pipeline
def executar_backup(pasta: str) -> None:
    try:
        arquivos: List[str] = ler_arquivos(pasta)
        if arquivos:
            upload_arquivos(arquivos)
            # deletar_arquivos(arquivos)
        else:
            print("Nenhum arquivo encontrado.")
    except Exception as e:
        print("Erro ao processar realizar o backup dos arquivos para o S3: {e}")
        raise

if __name__ == "__main__":
    PASTA_LOCAL = 'dados'
    executar_backup(PASTA_LOCAL)