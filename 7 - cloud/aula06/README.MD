### **Projeto**
**Proteção e Processamento Seguro de Dados Sensíveis em Ambientes Regulatórios**

![image](https://github.com/lvgalvao/data-engineering-roadmap/blob/main/Bootcamp%20-%20Cloud%20para%20dados/Aula_06/1_C2EJ15gGamMmbWGAt7I0Rg.png?raw=true)

Em muitas indústrias, como a financeira, de saúde ou de tecnologia, as empresas lidam com grandes volumes de dados altamente sensíveis que devem ser protegidos rigorosamente para cumprir regulamentações como GDPR, HIPAA, ou normas internas de segurança. Um desafio comum é garantir que esses dados sejam processados de forma segura, sem exposição a ameaças externas, ao mesmo tempo em que permitem o acesso controlado para manutenção e monitoramento.

### **Cenário**

Uma empresa de serviços financeiros precisa processar dados de transações bancárias que são armazenados em um ambiente de armazenamento seguro (S3). Esses dados são altamente sensíveis e sujeitos a rigorosas regulamentações de proteção de dados. A empresa enfrenta o desafio de processar esses dados de forma eficiente e segura, garantindo que nenhum dado seja exposto à internet durante o processamento.

### **Motivação para Montar a Arquitetura**

1. **Segurança e Conformidade**: A principal motivação é proteger os dados sensíveis e cumprir as exigências regulatórias. Ao isolar o processamento de dados em uma subrede privada, a arquitetura garante que os dados não sejam expostos à internet. A conexão ao bucket S3 é feita exclusivamente através de um VPC Endpoint, mantendo o tráfego de dados dentro da infraestrutura segura da AWS.

2. **Acesso Controlado e Seguro**: Para manutenção e monitoramento, é necessário acesso à instância que processa os dados. No entanto, para evitar riscos, o acesso direto à instância privada não é permitido. Em vez disso, uma instância pública (Bastion Host) na subrede pública atua como um ponto de entrada seguro. Isso permite que apenas usuários autorizados, através de conexões seguras, possam acessar a instância privada, minimizando os riscos de ataques externos.

3. **Gerenciamento Eficiente de Recursos**: A arquitetura permite separar responsabilidades, com a instância privada focada exclusivamente no processamento seguro dos dados, enquanto a instância pública gerencia o acesso e monitoramento. Isso facilita a manutenção, escalabilidade e otimização de recursos, garantindo que cada componente esteja configurado para desempenhar sua função da forma mais eficiente possível.

### **Benefício para o Negócio**

Implementar essa arquitetura permite à empresa processar dados sensíveis em conformidade com regulamentações rigorosas, ao mesmo tempo em que assegura que os dados permanecem seguros e acessíveis apenas por usuários autorizados. Isso não só reduz o risco de violações de dados, como também garante que a empresa esteja em total conformidade com normas de proteção de dados, evitando penalidades e mantendo a confiança dos clientes e parceiros.

### **Estimativa de Custo para Implementação da Arquitetura**

Os custos de implementação de uma arquitetura como a descrita podem variar dependendo de vários fatores, como o tamanho e o uso dos recursos, a região da AWS em que o projeto é implementado, e o nível de utilização dos serviços. 

### **Considerações Finais**

- **Custos Variáveis:** O custo final pode variar dependendo do uso efetivo dos recursos, como o tráfego de dados e o armazenamento adicional no S3.
- **Reduções Potenciais:** Usar instâncias spot ou reservar instâncias EC2 para contratos de longo prazo pode reduzir significativamente os custos.
- **Testes e Desenvolvimento:** Durante a fase de desenvolvimento e teste, você pode utilizar instâncias menores e reduzir a quantidade de dados processados para minimizar os custos.

Essas estimativas fornecem uma visão geral dos custos mensais associados a manter essa arquitetura AWS em produção. Ajustes específicos podem ser feitos com base nas necessidades e no uso real do projeto.

O custo de desenvolvimento de um projeto como esse pode variar amplamente dependendo de vários fatores, como a complexidade do projeto, a experiência e localização dos desenvolvedores, o tempo necessário para implementação, e se você contratará uma equipe interna, freelancers ou uma empresa especializada.

#### **1. Requisitos do Projeto**

**1.1. Infraestrutura de Rede (VPC)**
- **VPC**: Criar uma Virtual Private Cloud (VPC) que incluirá subredes públicas e privadas.
- **Subrede Pública**:
  - Deve conter uma instância EC2 pública que atuará como um bastion host, permitindo o acesso SSH à instância privada na subrede privada.
  - Deve ser conectada a um Internet Gateway para permitir o tráfego de entrada e saída da internet.
- **Subrede Privada**:
  - Deve conter uma instância EC2 privada, responsável por acessar e processar dados nos buckets S3.
  - Não deve ter acesso direto à internet, garantindo que todo o tráfego externo seja gerenciado através da instância pública.
- **Gateway Endpoint**:
  - Criar um Gateway Endpoint para S3, associado à tabela de rotas da subrede privada, permitindo que a instância EC2 privada acesse os buckets S3 sem passar pela internet.

**1.2. EC2 Instances**
- **Instância EC2 Pública (Bastion Host)**:
  - Deve ser configurada na subrede pública para permitir o acesso SSH à instância EC2 privada.
  - Esta instância terá acesso à internet para downloads de pacotes e outras operações de manutenção.
- **Instância EC2 Privada**:
  - Localizada na subrede privada, será responsável por processar os dados nos buckets S3.
  - Deve ser configurada para acessar os buckets S3 via o Gateway Endpoint.
  - O acesso SSH à instância privada deve ser feito exclusivamente através do bastion host, garantindo que a instância permaneça isolada da internet.

**1.3. S3 Buckets**
- **Buckets S3**:
  - Criar e configurar os buckets S3 necessários para o projeto.
  - Garantir que o acesso a esses buckets seja feito exclusivamente via o Gateway Endpoint a partir da instância privada, mantendo os dados seguros dentro da VPC.

**1.4. IAM Roles e Políticas**
- **IAM Role para Instância EC2 Privada**:
  - Criar uma IAM Role que conceda à instância EC2 privada as permissões necessárias para acessar os buckets S3 via o Gateway Endpoint.
  - Esta role deve ser restrita apenas às ações necessárias, seguindo o princípio do menor privilégio.
- **IAM User com Permissões Restritas**:
  - Criar um usuário IAM com permissões específicas para gerenciar os recursos do projeto (EC2, VPC, S3).
  - Este usuário deve ter permissões limitadas ao escopo do projeto e não deve ser capaz de criar outros usuários IAM ou modificar configurações globais de segurança.