import streamlit as st
from agenda import Agenda

# Inicializa a agenda
agenda = Agenda()

# Carrega os dados da agenda
agenda.load_agenda()

st.title('Agenda de Contatos')

# Mostra o nome do arquivo e o ID único da agenda
st.write(f"Nome do arquivo: {agenda.file_path}")
#st.write(f"ID único da agenda: {agenda.agenda_id}")

# Mostra a quantidade de contatos
st.write(f"Quantidade de Contatos: {len(agenda.agenda_data)}")

# Mostra os contatos em ordem alfabética
st.write('Contatos:')
agenda_data_sorted = agenda.agenda_data.sort_values('Nome')  # Ordena por nome
st.write(agenda_data_sorted)

# Adiciona um novo contato
st.header('Adicionar Contato')
nome = st.text_input('Nome')
email = st.text_input('Email')
idade = st.number_input('Idade', min_value=0, max_value=120) #key='idade_add')  # Adiciona chave única
numero = st.number_input('Número', min_value=0, step=1)


# Remove as vírgulas do número (caso haja)
#numero_sem_virgulas = numero.replace(',', '')

if st.button('Adicionar Contato'):
    agenda.add_contact(nome, email, idade, numero)

# Editar um contato existente
st.header('Editar Contato')
edit_nome = st.selectbox('Selecione um contato para editar:', agenda_data_sorted['Nome'].tolist())
edit_email = st.text_input('Email', value=agenda_data_sorted.loc[agenda_data_sorted['Nome'] == edit_nome, 'Email'].values[0])
edit_idade = st.number_input('Idade', value=int(agenda_data_sorted.loc[agenda_data_sorted['Nome'] == edit_nome, 'Idade'].values[0]), min_value=0, max_value=120, key='idade_edit')  # Adiciona chave única
edit_numero = st.number_input('Número', value=agenda_data_sorted.loc[agenda_data_sorted['Nome'] == edit_nome, 'Numero'].values[0])

if st.button('Editar Contato'):
    if agenda.edit_contact(edit_nome, edit_email, edit_idade, edit_numero):
        st.success('Contato editado com sucesso.')
    else:
        st.warning('Contato não encontrado.')

# Excluir um contato
st.header('Excluir Contato')
delete_nome = st.selectbox('Selecione um contato para excluir:', agenda_data_sorted['Nome'].tolist())
if st.button('Excluir Contato'):
    if agenda.delete_contact(delete_nome):
        st.success('Contato excluído com sucesso.')
   
