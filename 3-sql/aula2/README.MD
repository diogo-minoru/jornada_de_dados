# Aula 02 - SQL para Analytics: Nossas primeiras consultas

Realizar nossas primeiras consultas no banco Northwind

## Uma tangente antes de realizarmos nossas primeiras consultas

SQL, ou Structured Query Language, é uma linguagem de programação projetada para gerenciar dados armazenados em um sistema de gerenciamento de banco de dados relacional (RDBMS). SQL possui vários componentes, cada um responsável por diferentes tipos de tarefas e operações que podem ser executadas em um banco de dados. Esses componentes incluem DDL, DML, DCL, e DQL, entre outros. Aqui está um resumo de cada um deles:

Cada componente da linguagem SQL tem um papel fundamental na gestão e no uso de bancos de dados, e diferentes tipos de profissionais de tecnologia podem utilizar esses comandos para desempenhar suas funções específicas. Vamos detalhar quem geralmente é responsável por cada tipo de comando e qual o objetivo de cada um dos componentes mencionados (DDL, DML, DQL, DCL, TCL):

### 1. DDL (Data Definition Language)

O DDL ou Linguagem de Definição de Dados é usado para definir e modificar a estrutura do banco de dados e seus objetos, como tabelas, índices, restrições, esquemas, entre outros. Comandos DDL incluem:

* **CREATE**: Usado para criar novos objetos no banco de dados, como tabelas, índices, funções, vistas, triggers, etc.
* **ALTER**: Modifica a estrutura de um objeto existente no banco de dados, por exemplo, adicionando uma coluna a uma tabela ou alterando características de uma coluna existente.
* **DROP**: Remove objetos do banco de dados.
* **TRUNCATE**: Remove todos os registros de uma tabela, liberando o espaço ocupado por esses registros.

* **Responsável**: Administradores de banco de dados (DBAs) e desenvolvedores de banco de dados.
* **Objetivo**: O DDL é usado para criar e modificar a estrutura do banco de dados e de seus objetos. Esses comandos ajudam a definir como os dados são organizados, armazenados, e como as relações entre eles são estabelecidas. Eles são essenciais durante a fase de design do banco de dados e quando são necessárias mudanças na estrutura.

### 2. DML (Data Manipulation Language)

O DML ou Linguagem de Manipulação de Dados é usado para gerenciar dados dentro dos objetos (como tabelas). Inclui comandos para inserir, modificar e deletar dados:

* **INSERT**: Insere dados em uma tabela.
* **UPDATE**: Altera dados existentes em uma tabela.
* **DELETE**: Remove dados de uma tabela.
* **MERGE**: Uma operação que permite inserir, atualizar ou deletar registros em uma tabela com base em um conjunto de condições determinadas.

* **Responsável**: Desenvolvedores de software, analistas de dados e, ocasionalmente, usuários finais através de interfaces que executam comandos DML por trás dos panos.
* **Objetivo**: O DML é crucial para o gerenciamento dos dados dentro das tabelas. Ele é utilizado para inserir, atualizar, deletar e manipular dados armazenados. Analistas de dados podem usar DML para preparar conjuntos de dados para análise, enquanto os desenvolvedores o utilizam para implementar a lógica de negócios.

### 3. DQL (Data Query Language)

O DQL ou Linguagem de Consulta de Dados é fundamentalmente usado para realizar consultas nos dados. O comando mais conhecido na DQL é o **SELECT**, que é utilizado para recuperar dados de uma ou mais tabelas.

* **Responsável**: Analistas de dados, cientistas de dados, e qualquer usuário que necessite extrair informações do banco de dados.
* **Objetivo**: O DQL é usado para consultar e recuperar dados. É fundamental para gerar relatórios, realizar análises, e fornecer dados que ajudem na tomada de decisões. O comando `SELECT`, parte do DQL, é um dos mais usados e é essencial para qualquer tarefa que requer visualização ou análise de dados.

### 4. DCL (Data Control Language)

O DCL ou Linguagem de Controle de Dados inclui comandos relacionados à segurança na acessibilidade dos dados no banco de dados. Isso envolve comandos para conceder e revogar permissões de acesso:

* **GRANT**: Concede permissões de acesso aos usuários.
* **REVOKE**: Remove permissões de acesso.

* **Responsável**: Administradores de banco de dados.
* **Objetivo**: O DCL é usado para configurar permissões em um banco de dados, garantindo que apenas usuários autorizados possam acessar, modificar, ou administrar os dados. Isso é crucial para a segurança e a governança de dados, protegendo informações sensíveis e mantendo a integridade do sistema.

### 5. TCL (Transaction Control Language)

O TCL ou Linguagem de Controle de Transação é usado para gerenciar transações no banco de dados. Transações são importantes para manter a integridade dos dados e garantir que operações múltiplas sejam concluídas com sucesso ou não sejam realizadas de todo:

* **COMMIT**: Confirma uma transação, tornando todas as mudanças permanentes no banco de dados.
* **ROLLBACK**: Desfaz todas as mudanças feitas durante a transação atual.
* **SAVEPOINT**: Define um ponto na transação que pode ser usado para um rollback parcial.

* **Responsável**: Desenvolvedores de software e administradores de banco de dados.
* **Objetivo**: O TCL é usado para gerenciar transações no banco de dados, garantindo que as operações sejam completadas com sucesso ou revertidas em caso de erro. Isso é essencial para manter a consistência e integridade dos dados, especialmente em ambientes onde múltiplas transações ocorrem simultaneamente.

Essa separação de responsabilidades ajuda a manter a organização e eficiência das operações do banco de dados, além de garantir que as ações executadas em um ambiente de banco de dados sejam seguras e alinhadas com as necessidades da organização.

![SQL](https://assets.dio.me/sc9qapKI_QxsYul-hGd6uCgHLN6b3F8G6tGSxqaQKD0/f:webp/q:80/L2FydGljbGVzL2NvdmVyL2FlMjU3MmMzLTU0ZDUtNDVlOC1iMWI3LWE5MmM5MjEyNzU4ZS5qcGc)