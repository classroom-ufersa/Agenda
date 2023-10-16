import pandas as pd
import os
import hashlib

class Agenda:
    def __init__(self, file_path='agenda.csv'):
        self.file_path = file_path
        self.agenda_id = self.calculate_agenda_id(file_path)  # Calcula um ID único para a agenda
        self.load_agenda()

    def calculate_agenda_id(self, file_path):
        # Calcula um hash único do caminho do arquivo para servir como o ID da agenda
        hash_object = hashlib.md5(file_path.encode())
        return hash_object.hexdigest()

    def load_agenda(self):
        if os.path.exists(self.file_path):
            self.agenda_data = pd.read_csv(self.file_path)
        else:
            self.agenda_data = pd.DataFrame(columns=['Nome', 'Email', 'Idade', 'Numero'])

    def save_agenda(self):
        self.agenda_data = self.agenda_data.sort_values('Nome')  # Ordena por nome antes de salvar
        self.agenda_data.to_csv(self.file_path, index=False)

    def add_contact(self, nome, email, idade, numero):
        new_contact = pd.DataFrame([[nome, email, idade, numero]], columns=['Nome', 'Email', 'Idade', 'Numero'])
        self.agenda_data = pd.concat([self.agenda_data, new_contact], ignore_index=True)
        self.save_agenda()

    def edit_contact(self, nome, email, idade, numero):
        idx = self.agenda_data[self.agenda_data['Nome'] == nome].index
        if not idx.empty:
            idx = idx[0]
            self.agenda_data.at[idx, 'Email'] = email
            self.agenda_data.at[idx, 'Idade'] = idade
            self.agenda_data.at[idx, 'Numero'] = numero
            self.save_agenda()
            return True
        else:
            return False

    def delete_contact(self, nome):
        idx = self.agenda_data[self.agenda_data['Nome'] == nome].index
        if not idx.empty:
            self.agenda_data.drop(idx, inplace=True)
            self.agenda_data.reset_index(drop=True, inplace=True)
            self.save_agenda()
            return True
        else:
            return False
