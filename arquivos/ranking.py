
import streamlit as st

def rank(pontos):    
    if pontos <= 299:
        divisao = "Bronze I"
        pat = 'bronze.png'
    elif 300 <= pontos <= 599:
        divisao = "Bronze II"
        pat = 'bronze.png'
    elif 600 <= pontos <= 899:
        divisao = "Bronze III"
        pat = 'bronze.png'
    elif 900 <= pontos <= 1299:
        divisao = "Prata I"
        pat = 'prata.png'
    elif 1300 <= pontos <= 1699:
        divisao = "Prata II"
        pat = 'prata.png'
    elif 1700 <= pontos <= 2099:
        divisao = "Prata III"
        pat = 'prata.png'
    elif 2100 <= pontos <= 2599:
        divisao = "Ouro I"
        pat = 'ouro.png'
    elif 2600 <= pontos <= 3099:
        divisao = "Ouro II"
        pat = 'ouro.png'
    elif 3100 <= pontos <= 3599:
        divisao = "Ouro III"
        pat = 'ouro.png'
    elif 3600 <= pontos <= 4199:
        divisao = "Platina I"
        pat = 'platina.png'
    elif 4200 <= pontos <= 4799:
        divisao = "Platina II"
        pat = 'platina.png'
    elif 4800 <= pontos <= 5399:
        divisao = "Platina III"
        pat = 'platina.png'
    elif 5400 <= pontos <= 6099:
        divisao = "Diamante I"
        pat = 'diamante.png'
    elif 6100 <= pontos <= 6799:
        divisao = "Diamante II"
        pat = 'diamante.png'
    elif 6800 <= pontos <= 7499:
        divisao = "Diamante III"
        pat = 'diamante.png'
    elif 7500 <= pontos <= 8199:
        divisao = "Carmesim I"
        pat = 'carmesim.png'
    elif 8200 <= pontos <= 8899:
        divisao = "Carmesim II"
        pat = 'carmesim.png'
    elif 9600 <= pontos <= 9999:
        divisao = "Iridescent"
        pat = 'iridescente.png'
    elif pontos >= 10000:
        divisao = "TOP 250"
        pat = 'top_250.png'
    return divisao,pat


