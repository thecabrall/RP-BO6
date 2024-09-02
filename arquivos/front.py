import rp
import streamlit as st

titu = print("||:::> RANKED PRO <:::||")
print(":"*24)
print('1 - MATCH POINTS\n2 - STATS MATCH\n3 - HISTÓRICO\n4 - SAIR')
print(":"*24)
opcao = int(input('Escolha uma das opções para prosseguir: '))

if opcao == 1:
    nome = input("Informe seu nome: ")
    rp.rankeada(nome)
    exit()
elif opcao == 2:
    print('STATS MATCH')
    exit()
elif opcao == 3:
    print('HISTÓRICO')
    exit()
elif opcao == 4:
    exit()

#print("||:::> AGORA COMEÇA A 2° PARTE <:::||")