## Bootcamp Cloud: Aula 02
### S3: Armazenamento de Dados na AWS
Objetivo: Explorar as diversas aplicações do Amazon S3 no contexto de engenharia, ciência e análise de dados, com um foco prático em como configurar e utilizar o serviço via script Python usando o boto3. Além disso, abordaremos a criação de um IAM exclusivo e um grupo de recursos para gerenciar acesso e segurança.

## 4. Exemplo de Uso do S3 via Python (boto3)

### 4.1 Instalando o boto3

1. **Instalação do boto3:**
   - Para interagir com o S3 via Python, é necessário instalar o boto3, o SDK da AWS para Python:

   ```bash
   pip install boto3
   ```

### 4.2 Configurando Credenciais AWS

1. **Configuração das Credenciais:**
   - Antes de utilizar o boto3, é necessário configurar as credenciais da AWS. Isso pode ser feito através do `aws configure` ou definindo variáveis de ambiente.

   ```bash
   aws configure
   ```

2. **Configuração Manual (Opcional):**
   - As credenciais também podem ser configuradas manualmente:

   ```python
   import boto3

   session = boto3.Session(
       aws_access_key_id='YOUR_ACCESS_KEY',
       aws_secret_access_key='YOUR_SECRET_KEY',
       region_name='us-west-2'
   )
   s3 = session.resource('s3')
   ```

### 4.3 Criando e Gerenciando Buckets

1. **Criando um Bucket:**
   - Use o boto3 para criar um novo bucket S3:

   ```python
   import boto3

   s3 = boto3.client('s3')
   bucket_name = 'meu-novo-bucket'

   s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
       'LocationConstraint': 'us-west-2'})
   ```

2. **Listando Buckets:**
   - Verifique todos os buckets existentes:

   ```python
   response = s3.list_buckets()

   for bucket in response['Buckets']:
       print(bucket['Name'])
   ```

### 4.4 Upload e Download de Arquivos

1. **Upload de Arquivos:**
   - Carregue um arquivo local para o S3:

   ```python
   s3.upload_file('local-file.txt', bucket_name, 's3-file.txt')
   ```

2. **Download de Arquivos:**
   - Baixe um arquivo do S3 para o sistema local:

   ```python
   s3.download_file(bucket_name, 's3-file.txt', 'local-file.txt')
   ```

### 4.5 Configurando ACLs e Políticas de Bucket

1. **Definindo Permissões de Acesso:**
   - Use boto3 para definir permissões de leitura/escrita:

   ```python
   s3.put_object_acl(Bucket=bucket_name, Key='s3-file.txt', ACL='public-read')
   ```

2. **Políticas de Bucket:**
   - Configure uma política de bucket para permitir acesso público:

   ```python
   bucket_policy = {
       'Version': '2012-10-17',
       'Statement': [{
           'Sid': 'PublicReadGetObject',
           'Effect': 'Allow',
           'Principal': '*',
           'Action': 's3:GetObject',
           'Resource': f'arn:aws:s3:::{bucket_name}/*'
       }]
   }

   s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))
   ```