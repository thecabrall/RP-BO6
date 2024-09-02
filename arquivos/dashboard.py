import streamlit as st
import requests
import pandas as pd
import numpy as np
import ranking as r

def inicio():
    nome = str(st.text_input('Insira seu nome abaixo:', key='username'))           
    return nome

# LISTA DE PONTO DO DIA #
daily = []

# INICIO DO DIA #
inicio()


# CONFIGURAÇÃO DO PRIMEIRO CONTEINER #

colu1,colu2 = st.columns([5,5])


# PRIMEIRA PERGUNTA #
with colu1:
    PI = int(st.number_input('Com quantos pontos você começou hoje?', key='PI'))

def add_ponto_inicial(pontos):
    daily.append(pontos)


# CONFIGURAÇÃO DO SEGUNDO CONTEINER #

col1,col2 = st.columns([1,1])


# CONFIGURAÇÃO DE BOTÃO #

with col1:
    add = st.button('Iniciar Dia',key='add_ponto_ini')
    if add:
        add_ponto_inicial(PI)

#=========================================================================#


# SEGUNDA PERGUNTA #

if 'pontuacao' not in st.session_state:
    st.session_state.pontuacao = []


def add_ponto_final(pontos):
    st.session_state.pontuacao.append(pontos)

with colu2:
    PF = int(st.number_input('Quantos pontos você tem atualmente?', key='PF'))


# CONFIGURAÇÃO DE BOTÃO #
with col2:
    add = st.button('Adicionar ao gráfico',key='add_ponto_fim')
    if add:
        add_ponto_final(PF)


# TESTE DE LISTAS #
# st.write(st.session_state.pontuacao)
# st.write(daily)

# SEPARAÇÃO DE COLUNAS DE PONTUAÇÃO #

tab1,tab2,tab3 = st.columns(3)

# CÁLCULO DE PONTUAÇÃO CALL OF DUTY #

DIF = PF - PI

progresso = pd.DataFrame(data=st.session_state.pontuacao)

patente, imagem_pat = r.rank(PF)

with tab1:
    st.image(imagem_pat)


with tab2:
    desempenho = st.metric(label=f'{patente}',value=PF,delta=DIF,)

st.area_chart(progresso,x=None)

