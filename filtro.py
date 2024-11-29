# import pandas as pd
# import streamlit as st
# import time
# import requests
# import json
# from datetime import datetime,date
# url3 = "https://docs.google.com/spreadsheets/d/1n22edpE9NSH31uixN04yuqKWvSjbstqE8gy8-QZXV-k/export?format=csv"
# nomes = pd.read_csv(url3)
# lista = ['']

# def formatandoData(data):
    
#     data_formatada = data.strftime("%d/%m/%Y")
#     return data_formatada


# def barra(valores):
#     progress_bar = st.progress(0)
#     for i in range(valores.size()):
#         time.sleep(0.01)  # Espera 50ms
#         progress_bar.progress(i)

# def get():
#     dados = pd.read_csv("https://docs.google.com/spreadsheets/d/1n22edpE9NSH31uixN04yuqKWvSjbstqE8gy8-QZXV-k/export?format=csv")
#     todos_dados = dados[['APARELHOS','CALCULOS']].head(31).dropna(axis=0)
#     for data in todos_dados:
#         st.markdown(data['APARELHOS'].values())
#         barra(todos_dados['CALCULOS'].values())
# st.set_page_config(layout="wide")

# style = '''
# <style>

# .st-emotion-cache-1xfnpov{
#     display: flex;
#     flex-direction: row;
# }
# .st-af{
# width: 250px;
# }







# </style>

# '''
# animacao = '''

# '''
# st.markdown(style, unsafe_allow_html=True)
# st.html('''
# ''')
# with st.container():
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         inicio = st.date_input(label="INICIO",format="DD/MM/YYYY")
#         fim  = st.date_input(label="FIM",format="DD/MM/YYYY")
#         nomes = pd.read_csv(url3)

#         lista = ['']
#         for nome in nomes.values.tolist():
#             lista.append(nome[0])
        

#         lista_nomes = st.selectbox(label="Nomes",options=lista, placeholder="Nome")



#     with col2:
        

        
#         if lista_nomes != '':
#             get()



        
        
        


import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import time
import requests
import json
from datetime import datetime
# URL do Google Sheets
url3 = "https://docs.google.com/spreadsheets/d/1n22edpE9NSH31uixN04yuqKWvSjbstqE8gy8-QZXV-k/export?format=csv"

# Função para exibir a barra de progresso

def barra(valores):
    progress_bar = st.progress(0)
    for i in range(1, valores + 1):
        time.sleep(0.01)
        progress_bar.progress(int((i / valores) * 100))  # Atualiza em porcentagem

# Função para obter os dados e processar
def get():
    dados = pd.read_csv(url3)
    # Seleciona colunas de interesse e remove valores ausentes
    todos_dados = dados[['APARELHOS', 'CALCULOS']].head(31).dropna()
    
    # Loop para processar cada linha
    with st.sidebar:
        st.sidebar.header("")
        for _, row in todos_dados.iterrows():
            aparelho = row['APARELHOS']
            calculos = int(row['CALCULOS'])  # Garante que seja inteiro
            
            # Exibe o nome do aparelho
            st.markdown(f"### {aparelho}")
            
            # Executa a barra de progresso
            barra(calculos)
            st.header(calculos, divider=True)


def post(nome,inicio,fim):

    api_url = "https://script.google.com/macros/s/AKfycbwQVS7rA4PtgEfo5u87_wYWQcz-3m6GES8qh1RZxxISae_JY4Zw2zHP7B-Z2ZyqLn3tvQ/exec"

    # Dados que você deseja enviar para a API
    data = {
        "value1": str(nome),
        "value2": str(inicio),
        "value3": str(fim)
    }

    try:
        # Envia os dados usando POST
        response = requests.post(api_url, headers={"Content-Type": "application/json"}, data=json.dumps(data))

        # Verifica a resposta
        if response.status_code == 200:
            print("Resposta da API:")
            print(response.json())
        else:
            print(f"Erro: {response.status_code}")
            print(response.text)

    except Exception as e:
        print("Erro ao enviar os dados:", str(e))

# Configuração da página
st.set_page_config(layout="wide")
post('','','')
time.sleep(3)
# Estilo customizado
style = '''
<style>


.st-emotion-cache-6qob1r{
width: 100hv;
}

</style>
'''
st.markdown(style, unsafe_allow_html=True)

# Interface do usuário




col1, col2, col3 = st.columns(3)

# Inputs de data
with col1:
    inicio = st.date_input(label="INÍCIO", format="DD/MM/YYYY")
with col2:
    fim = st.date_input(label="FIM", format="DD/MM/YYYY")

# Obtendo os nomes do Google Sheets
nomes = pd.read_csv(url3)
lista = [''] + [nome[0] for nome in nomes.values.tolist()]

# Dropdown para selecionar o nome
with col3:
    lista_nomes = st.selectbox(label="NOMES", options=lista)


# Executa o processamento apenas se um nome for selecionado
if lista_nomes:
    novo_inicio = datetime.strftime(inicio, "%d/%m/%Y")
    novo_fim =  datetime.strftime(fim, "%d/%m/%Y")

    
    post(lista_nomes,novo_inicio,novo_fim)
    time.sleep(11)
    get()
                



