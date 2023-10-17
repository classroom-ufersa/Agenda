# Agenda de Contatos

Este é um programa para gerenciar uma agenda de contatos em Python, usando Streamlit para a interface de usuário e Pandas para o armazenamento e manipulação dos dados.

## Funcionalidades

- **Visualizar Contatos:** Veja todos os contatos na agenda, ordenados alfabeticamente por nome.
- **Adicionar Contato:** Adicione um novo contato com nome, email, idade e número de telefone.
- **Editar Contato:** Edite as informações de um contato existente.
- **Excluir Contato:** Remova um contato da agenda

## Problemática
- Criar um sistema de agendas  que armazene contatos em ordem alfabética
- Cada contato deve ter nome, email, idade, e contato

## Sobre o sistema
- Desenvolvido por Karllos Eduardo
- Linguagem utilizada
<div style="display: flex;">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40" height="40" style="margin-right: 10px;">
</div>

## Modulos
### main.py
- **Importações:**
Importa as bibliotecas necessárias, incluindo Streamlit para criar a interface e a classe Agenda do módulo agenda.
- **Inicialização da Agenda:**
Cria uma instância da classe Agenda para representar a agenda de contatos e carrega os dados da agenda.
- **Definição do Título:**
Define o título da aplicação como "Agenda de Contatos".
- **Mostrar Informações da Agenda:**
Mostra o nome do arquivo, o ID único da agenda e a quantidade de contatos.
- **Mostrar Contatos em Ordem Alfabética:**
Mostra os contatos ordenados por nome.
- **Adicionar Novo Contato:**
Permite ao usuário adicionar um novo contato inserindo informações como nome, email, idade e número.
- **Editar Contato Existente:**
Permite ao usuário editar informações de um contato existente selecionando o contato e inserindo novas informações.
- **Excluir Contato:**
Permite ao usuário excluir um contato existente selecionando o contato a ser excluído.

### agenda.py
- **Importações:**
Importa as bibliotecas necessárias, como pandas para manipulação de dados e os para operações relacionadas ao sistema operacional.
- **class Agenda:**
Define a classe Agenda que representa a agenda de contatos.
- **__init__(self, file_path='agenda.csv'):**
Método inicializador que é chamado ao criar uma instância da classe Agenda.
Inicializa os atributos da classe, incluindo o caminho do arquivo e o ID único da agenda, e carrega a agenda a partir do arquivo.
- **load_agenda(self):**
Método para carregar os dados da agenda a partir do arquivo CSV especificado no caminho.
Cria um DataFrame vazio se o arquivo não existir.
- **save_agenda(self):**
Método para ordenar os contatos por nome e salvar os dados da agenda no arquivo CSV.
- **add_contact(self, nome, email, idade, numero):**
Método para adicionar um novo contato à agenda.
Cria um novo contato no DataFrame e salva a agenda atualizada.
- **edit_contact(self, nome, email, idade, numero):**
Método para editar um contato existente na agenda com base no nome.
Atualiza as informações do contato e salva a agenda atualizada.
- **delete_contact(self, nome):**
Método para excluir um contato da agenda com base no nome.
Remove o contato e salva a agenda atualizada.
