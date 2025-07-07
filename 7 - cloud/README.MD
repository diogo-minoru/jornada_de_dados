# Bootcamp Cloud: Aula 01

## Introdução à AWS e Cloud Computing

**Objetivo:** Fornecer uma introdução prática ao uso da AWS, abordando a criação de contas, controle de custos e navegação na interface gráfica, com foco em aplicações na área de dados.

---

## 1. Por que Utilizar Cloud?

1. **Escalabilidade:** A cloud permite escalar recursos conforme necessário, sem a necessidade de grandes investimentos iniciais.
2. **Custo-eficiência:** Com a cloud, você paga apenas pelo que utiliza, reduzindo custos operacionais.
3. **Acessibilidade:** Serviços de cloud podem ser acessados de qualquer lugar, facilitando a colaboração e o trabalho remoto.
4. **Segurança:** Provedores de cloud como AWS oferecem robustos recursos de segurança, incluindo criptografia e autenticação multifator.

## 2. O que Não é Cloud

1. **Não é um Data Center On-Premise:** Embora a cloud envolva servidores, não é o mesmo que ter um data center físico na empresa.
2. **Não é apenas armazenamento:** Cloud envolve muito mais do que apenas guardar dados. É um ecossistema completo de serviços.
3. **Não é sempre barato:** Se mal gerido, o uso da cloud pode resultar em custos inesperados.

**Serviços Comuns:**
- **S3 (Simple Storage Service):** Armazenamento escalável de objetos, ideal para dados brutos, backups e arquivos de grande volume.
- **EC2 (Elastic Compute Cloud):** Serviço que permite criar e gerenciar instâncias de máquinas virtuais na nuvem, altamente configuráveis.
- **RDS (Relational Database Service):** Serviço gerenciado de banco de dados relacional, que suporta mecanismos como MySQL, PostgreSQL, e SQL Server.

### 3.1 Criando o Bucket S3

1. **Nome do Bucket:**
   - Escolha um nome único para o seu bucket. Lembre-se que o nome deve ser globalmente único dentro da AWS.
  
2. **Zona (Region):**
   - Selecione a região onde o bucket será criado. É recomendável escolher a região mais próxima dos seus usuários para reduzir latência.

3. **ACLs (Access Control Lists):**
   - Configure as listas de controle de acesso (ACLs) para definir permissões de leitura e escrita. Por padrão, é melhor manter o controle de acesso restrito.

4. **Bucket Público:**
   - Inicialmente, o bucket deve ser privado por questões de segurança. Se for necessário torná-lo público, isso pode ser feito posteriormente.

5. **Bucket Versioning:**
   - Habilite o versionamento do bucket para manter várias versões de um objeto. Isso pode ser útil para recuperação de dados e auditoria.

6. **Tags:**
   - Adicione tags para identificar e organizar seu bucket. Tags podem incluir informações como ambiente (produção, desenvolvimento), proprietário, e finalidade.

7. **Default Encryption:**
   - Configure a criptografia padrão para garantir que todos os objetos armazenados no bucket sejam criptografados automaticamente.

### 3.2 Acessando o Bucket

- Depois de criar o bucket, acesse-o através do console da AWS. Na interface do bucket, você pode ver e gerenciar todos os objetos armazenados.

### 3.3 Colocando uma Imagem no Bucket

1. **Upload de Arquivo:**
   - Faça upload de uma imagem ou qualquer outro arquivo no bucket.
  
2. **Verificando o Arquivo:**
   - Após o upload, tente acessar o arquivo diretamente. Você notará que, por padrão, o arquivo não será acessível publicamente.

### 3.4 Configurando Permissões: Tornando o Arquivo Público

1. **Padrão Privado:**
   - Por padrão, todos os arquivos em um bucket S3 são privados, ou seja, somente você pode acessá-los.
  
2. **Tornar o Arquivo Público:**
   - Para tornar o arquivo acessível publicamente, você pode modificar as permissões do arquivo ou configurar uma política de bucket.

### 3.5 Bucket Policy: Exemplo de Permissão de Leitura para Usuário Anônimo

- **Bucket Policy:**
   - Adicione uma política ao bucket para permitir que usuários anônimos leiam os arquivos. Um exemplo de política de leitura pública para um bucket S3 pode ser adicionado através do editor de políticas no console da AWS.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::nome-do-bucket/*"
        }
    ]
}
```

### 3.6 Adicionando um Arquivo `index.html`

- **Upload do Arquivo `index.html`:**
   - Adicione um arquivo `index.html` ao seu bucket. Esse arquivo servirá como a página principal do seu site estático.

## 12. Criando e Configurando uma Instância EC2

Nesta seção, vamos aprender a configurar uma instância EC2, obter acesso root, definir uma senha para o root, e depois configurar o ambiente com Python e Streamlit para rodar um aplicativo básico de "Hello World", incluindo a renderização de uma imagem armazenada no S3.

### 4.1 Conectando-se à Instância EC2 e Obtendo Acesso Root

1. **Obter Acesso Root:**
   - Assim que estiver conectado, troque para o usuário root usando o comando:

   ```bash
   sudo su
   ```

3. **Definir uma Senha para o Root (se necessário):**
   - Se você ainda não configurou uma senha para o root, ou deseja alterá-la, execute:

   ```bash
   passwd
   ```

   - Você será solicitado a digitar a nova senha para o root e confirmá-la.

### 12.2 Instalando Python, `pip3`, e Streamlit

1. **Atualizar Pacotes e Instalar Python:**
   - Primeiro, atualize os pacotes e instale Python 3 com os seguintes comandos:

   ```bash
   yum update -y
   yum install python3 -y
   ```

2. **Instalando o `pip3`:**
   - Instale o `pip3`, que é o gerenciador de pacotes para Python 3:

   ```bash
   yum install python3-pip -y
   ```

3. **Verificando a Instalação do `pip3`:**
   - Verifique se o `pip3` foi instalado corretamente:

   ```bash
   pip3 --version
   ```

4. **Instalando o Streamlit:**
   - Agora que o `pip3` está instalado, você pode instalar o Streamlit com o comando:

   ```bash
   pip3 install streamlit
   ```

### 12.3 Criando o Código do Streamlit com a Imagem

1. **Criar um Arquivo Python para o Streamlit:**
   - Use o editor de texto `nano` para criar e editar o arquivo `app.py`. No terminal, execute:

   ```bash
   nano app.py
   ```

2. **Inserir o Código para Renderizar a Imagem:**
   - Insira o seguinte código no arquivo `app.py`:

   ```python
   import streamlit as st

   # Título do aplicativo
   st.title("Hello, World!")

   # Descrição
   st.write("Este é um simples aplicativo Streamlit rodando em uma instância EC2 na AWS.")
   ```

3. **Salvar o Arquivo e Sair do Editor:**
   - Para salvar o arquivo, pressione `Ctrl + O` e depois `Enter`.
   - Para sair do editor `nano`, pressione `Ctrl + X`.

### 12.4 Executando o Streamlit na Porta 80

1. **Executar o Streamlit na Porta 80:**
   - Agora que você está logado como root, execute o Streamlit na porta 80:

   ```bash
   streamlit run app.py --server.port 80 --server.enableCORS false
   ```

2. **Acessar a Aplicação:**
   - Acesse o aplicativo no navegador através do endereço IP público da sua instância EC2:

   ```http
   http://seu-endereco-publico-ec2
   ```

### Resultado Esperado

Ao acessar o aplicativo, você verá o título "Hello, World!", uma descrição, e a imagem "fotodaturma.png" renderizada diretamente do S3, com a legenda "Foto da Turma - Primeiro Dia".