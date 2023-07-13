## TESTE DEPLOY ##

### cs_20236
Repositório definido para a manutenção do controle de versão dos artefatos do projeto de construção de uma API Rest para:

- Gerenciar projetos.

### Nome
NoteSync

### Descrição
Um gerenciador de tarefas sincronizado com uma equipe de trabalho.

### Problema
A falta de organização das tarefas em um equipe de trabalho pode gerar atrasos e conflitos entre os membros da equipe.

### Objetivos da Solução
- Organizar as tarefas de uma equipe de trabalho em estados de andamento.
- Cada membro da equipe pode visualizar de forma remota e em tempo real o andamento das tarefas.
- Atribuir prazos e responsáveis a tarefas específicas.
- Manter um histórico de tarefas realizadas.

### Grupo
Esta API será construída pelos componentes do grupo 6:

|Matrícula|Nome|Usuário Git|
|---|---|---|
|202105024|Daniel Nogueira da Costa|[nogueiralegacy](https://github.com/nogueiralegacy)|
|202105027|Felipe Moreira Moreira da Silva|[soft-felipe](https://github.com/soft-felipe)|
|202204198|Lucas Bernardes Feitosa|[lucas-bernardes03](https://github.com/lucas-bernardes03)|
|202105048|Matheus Geraldino de Melo|[kalheeso](https://github.com/kalheeso)|
201910912|Vinicius Prates Araujo|[PAVincius](https://github.com/PAVincius)|

### Requisitos Funcionais

1. RF001 - Funcionalidade: Criar um novo projeto.

**COMO usuário, QUERO criar um novo projeto no NoteSync PARA poder gerenciar meu projeto de forma organizada.**

2. RF002 - Funcionalidade: Controlar o acesso. 

**COMO usuário, QUERO controlar o acesso ao meu projeto, PARA permitir que eu tenho controle de quem participa dele.**

4. RF003 - Funcionalidade: Configurar fluxos de trabalho personalizados.

**COMO usuário, QUERO configurar fluxos de trabalho personalizados, PARA adequar o processo de trabalho ao meu projeto.**

5. RF004 - Funcionalidade: Criar tarefas.

**COMO usuário, QUERO criar tarefas, PARA declarar as atividades que devem ser realizadas.**

6. RF005 - Funcionalidade: Atualizar status de tarefas.

**COMO usuário, QUERO atualizar o status das tarefas do meu projeto, PARA acompanhar o progresso das atividades e ter uma visão geral do projeto.**

7. RF006 - Funcionalidade: Visualizar tarefas.

**COMO usuário, QUERO visualizar as tarefas em seus respectivos estados mais recentes, PARA ter uma visão geral do projeto.**

### Requisitos Não Funcionais

1. RNF001 - Usabilidade: A aplicação deve ser intuitiva e de fácil utilização.

2. RNF002 - Segurança: A aplicação deve garantir a privacidade dos usuários, não permitindo que usuários não autorizados acessem o projeto.

3. RNF003 - Desempenho: A aplicação deve apresentar os dados em tempo real para todos os usuários.

4. RNF004 - Confiabilidade: A aplicação deve se comportar conforme o esperado e estar disponível para todos os usuários.

5. RNF005 - Manutenibilidade: A aplicação deve ser fácil de manter e evoluir.

6. RNF006 - Portabilidade: A aplicação deve ser acessível por dispositivos móveis.

7. RNF007 - Conectividade: A aplicação deve implementar uma API Rest.

### Regras de Negócio
1. RN01 - Atribuição de tarefas: o usuário deve poder atribuir tarefas a outros usuários e a si mesmo.

2. RN02 - Definição de prazos: o usuário deve poder definir prazos para as tarefas.

### Tecnologia de _Front-end_
Flutter.

### Tecnologia de _Back-end_
API Rest construída em Python. (FastAPI)

### Tecnologia de Persistência de Dados
Banco de dados relacional PostgreSQL.

### Local do _Deploy_
O nosso planejamento inicial é hospedar nossa aplicação no Heroku ou no Firebase do Google, sendo crucial para nossa escolha a facilidade de configuração e também os recursos ofertados na versão gratuita.

### Cronograma de Desenvolvimento

|Iteração|Tarefa|Data Início|Data Fim|Responsável|Situação|
|---|---|---|---|---|---|
|1|Estudar e definir o SGBD do projeto|28/04/2023|05/05/2023|Grupo|Programada|
|2|Estudar e definir o serviço para deploy do projeto|28/04/2023|05/05/2023|Grupo|Programada|
|3| Definir os modelos de classes|06/05/2023|19/05/2023|Grupo|Programada|
|5| Definir os modelos de dados (ORM)|20/05/2023|02/06/2023|Grupo|Programada|
|6| Implementação do código |03/06/2023|16/06/2023|Grupo|Programada|
|7| Testes |22/07/2023|11/08/2023|Grupo|Programada|
