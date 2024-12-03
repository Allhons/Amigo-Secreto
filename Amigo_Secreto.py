import random
import streamlit as st

# Inicializando o Firebase Admin SDK
cred = credentials.Certificate('amigo-secreto-allyson-firebase-adminsdk-6om81-0a783864d5.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://amigo-secreto-allyson-default-rtdb.firebaseio.com'
})

# Função para sortear um nome que não seja o seu e remover o sorteado da lista
def sortear_nome(participantes, meu_nome):
    # Remover o seu nome da lista de opções para o sorteio
    participantes_sem_o_seu_nome = [nome for nome in participantes if nome != meu_nome]
    
    # Sortear um nome aleatório da lista filtrada
    nome_sorteado = random.choice(participantes_sem_o_seu_nome)
    
    # Remover o nome sorteado da lista de participantes
    participantes.remove(nome_sorteado)
    
    return nome_sorteado, participantes

# Função para obter a lista de participantes do Firebase
def obter_participantes():
    ref = db.reference('participantes')
    participantes = ref.get()
    if not participantes:
        return []
    return participantes

# Função para atualizar a lista de participantes no Firebase
def atualizar_participantes(participantes):
    ref = db.reference('participantes')
    ref.set(participantes)

# Interface com Streamlit
def app():
    st.title("Sorteio de Amigo Secreto")

    # Obtendo e mostrando a lista de participantes armazenada no Firebase
    participantes = obter_participantes()
    
    if not participantes:
        st.warning("Nenhum participante foi adicionado ainda.")
    
    # Entrada do nome do usuário
    meu_nome = st.text_input("Qual o seu nome?")

    # Entrada da lista de participantes, se necessário
    lista_participantes = st.text_area("Lista de participantes (separados por vírgula)", ", ".join(participantes))

    if lista_participantes:
        participantes = [p.strip() for p in lista_participantes.split(",")]
        atualizar_participantes(participantes)  # Atualiza a lista no Firebase

    if meu_nome:
        if meu_nome not in participantes:
            st.error(f"Seu nome ({meu_nome}) não está na lista de participantes!")
        else:
            # Botão para realizar o sorteio
            if st.button("Sortear Amigo Secreto"):
                if len(participantes) > 1:
                    # Sorteando o nome
                    nome_sorteado, participantes = sortear_nome(participantes, meu_nome)

                    # Atualizando a lista de participantes no Firebase
                    atualizar_participantes(participantes)
                    
                    st.success(f"O nome sorteado para você ({meu_nome}) é: {nome_sorteado}")
                    st.write(f"Participantes restantes: {', '.join(participantes)}")
                else:
                    st.warning("Não há participantes suficientes para sortear!")

# Rodando a aplicação
if __name__ == "__main__":
    app()
