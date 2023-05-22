<div align=center>
  <img src="./imagens/INFVertical.jpg">
</div>


<div align="center">SEDI - Secretaria de Estado de Desenvolvimento e Inovação</div>
<div align="center">STI - Subsecretaria de Tecnologia da Informação</div>

###### Nome do Sistema: NoteSync
###### Estória de Usuário: HU002
###### Sprint: a definir
###### Nome: Controlar o Acesso

## Histórico
|**Versão**|**Data**|**Alteração no Documento**|**Autor**|
|------|----|---------|-----|
|1.0|08/05/2023|<Criação do documento>|[PAVincius](https://github.com/PAVincius)|
|<Versão>|< data >|< descrição >|< autor >|

**Como:** usuário

**Eu quero:** controlar o acesso ao meu projeto

**Para:** permitir que eu tenha controle de quem participa dele.

**Cenário 1:** Adicionar usuário ao projeto

**Dado:** que estou logado no NoteSync

**E:** estou na página de gerenciamento do projeto

**Quando:** eu selecionar a opção "Adicionar Usuário"

**Então:** será exibido um campo de busca para digitar o nome de usuário ou e-mail do usuário que desejo adicionar ao projeto.

**E:** após digitar o nome ou e-mail, vou clicar no botão "Adicionar" para confirmar a ação.

**E:** o usuário será adicionado ao projeto com as permissões padrão.

**Cenário 2:** Definir permissões do usuário no projeto

**Dado:** que estou logado no NoteSync

**E:** estou na página de gerenciamento do projeto

**Quando:** eu selecionar a opção "Configurar Permissões" ao lado do nome de um usuário no projeto

**Então:** será exibido um painel com opções de permissões para o usuário selecionado.

**E:** poderei selecionar as permissões desejadas, como visualização, edição, exclusão, compartilhamento, etc.

**E:** após definir as permissões, vou clicar no botão "Salvar" para confirmar as alterações.

**Cenário 3:** Remover usuário do projeto

**Dado:** que estou logado no NoteSync

**E:** estou na página de gerenciamento do projeto

**Quando:** eu selecionar a opção "Remover Usuário" ao lado do nome de um usuário no projeto

**Então:** será exibida uma confirmação para garantir que desejo remover o usuário do projeto.

**E:** ao confirmar a remoção, o usuário será removido do projeto e perderá todas as permissões associadas a ele.

**Cenário 4:** Visualizar lista de usuários do projeto

**Dado:** que estou logado no NoteSync

**E:** estou na página de gerenciamento do projeto

**Quando:** eu selecionar a opção "Ver Usuários" ou "Gerenciar Usuários"

**Então:** será exibida uma lista de todos os usuários que têm acesso ao projeto.

**E:** a lista mostrará o nome do usuário e suas permissões associadas.

**E:** poderei visualizar os detalhes de cada usuário, como e-mail, data de adição ao projeto, etc.

</DIV>
