# Introdução ao Docker

Docker é uma plataforma de contêineres que permite empacotar, distribuir e executar aplicações de forma isolada e portátil. Ele simplifica o desenvolvimento e a implantação de software ao garantir que os ambientes sejam consistentes em diferentes sistemas.

## Principais Conceitos
- **Imagem**: Um pacote imutável que contém tudo o que é necessário para rodar uma aplicação.
- **Contêiner**: Uma instância em execução de uma imagem.
- **Dockerfile**: Um arquivo que define a construção de uma imagem.
- **Docker Compose**: Ferramenta para definir e gerenciar aplicações multicontêiner.

## Instalando o Docker
Se você ainda não tem o Docker instalado, siga as instruções de instalação disponíveis no site oficial:

- [Docker para Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Docker para Mac](https://docs.docker.com/desktop/install/mac-install/)
- [Docker para Linux](https://docs.docker.com/engine/install/)

Após a instalação, verifique se o Docker está funcionando corretamente com o comando:
```sh
docker --version
```

## Clonando e Executando o Projeto
Para executar o projeto disponível no GitHub, siga os passos abaixo:

### 1. Clonar o Repositório
Abra o terminal e execute o seguinte comando:
```sh
git clone git@github.com:lvgalvao/workshop-docker-aovivo-.git
```
Entre no diretório do projeto:
```sh
cd workshop-docker-aovivo-
```

### 2. Construir a Imagem Docker
Se houver um `Dockerfile` no projeto, você pode construir a imagem com:
```sh
docker build -t meu-projeto .
```

### 3. Executar o Contêiner
Após a construção da imagem, execute o contêiner com:
```sh
docker run -d -p 8501:8501 meu-projeto
```
Isso fará com que o serviço esteja acessível na porta 8501 do seu navegador.

## Conclusão
O Docker facilita a execução de aplicações sem precisar configurar o ambiente manualmente. Seguindo os passos acima, você conseguirá rodar o projeto clonado de forma rápida e eficiente.
