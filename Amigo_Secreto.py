import pandas as pd
import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit.logger import get_logger
import random
import time

LOGGER = get_logger(__name__)


Participantes = [
    'Allyson',
    'Luana',
    'Veronica',
    'Adilson',
    'Lara Ohana',
    'Clarice',
    'Cecilia',
    'Maura',
    'Tuca',
    'Matheus',
    'Marina',
    'Lara',
    'Kaio',
    'Eloa'
]
    
# Função para sortear um nome que não seja o seu e remover o sorteado da lista
def sortear_nome(participantes, meu_nome):
    # Remover o seu nome da lista de opções para o sorteio
    participantes_sem_o_seu_nome = [nome for nome in participantes if nome != meu_nome]
    
    # Sortear um nome aleatório da lista filtrada
    nome_sorteado = random.choice(participantes_sem_o_seu_nome)
    
    # Remover o nome sorteado da lista de participantes
    participantes.remove(nome_sorteado)
    
    return nome_sorteado, participantes

# Interface com Streamlit
def app():
    st.title("Sorteio de Amigo Secreto")
    
    # Entrada do nome do usuário
    meu_nome = st.text_input("Qual o seu nome?")
    
    # Entrada da lista de participantes
    lista_participantes = st.text_area("Lista de participantes (separados por vírgula)", "Allyson, Luana, Veronica, Adilson, Lara Ohana, Clarice, Cecilia, Maura, Tuca,Matheus, Marina, Lara, Kaio, Eloa")
    
    # Convertendo a lista de participantes em uma lista Python
    participantes = [p.strip() for p in lista_participantes.split(",")]

    if meu_nome:
        if meu_nome not in participantes:
            st.error(f"Seu nome ({meu_nome}) não está na lista de participantes!")
        else:
            # Botão para realizar o sorteio
            if st.button("Sortear Amigo Secreto"):
                # Sorteando o nome
                nome_sorteado, participantes = sortear_nome(participantes, meu_nome)
                st.success(f"O nome sorteado para você ({meu_nome}) é: {nome_sorteado}")
                st.write(f"Participantes restantes: {', '.join(participantes)}")

# Rodando a aplicação
if __name__ == "__main__":
    app()