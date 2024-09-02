import rp
from rp import inicio


def points():
    pontuacao = True
    while pontuacao:
        pontos_str = input("Quantos pontos você tem agora?   ")
        if pontos_str.isdigit():
            pontos = int(pontos_str)
            if pontos > inicio:
                print("Você inseriu um valor maior do que começou.")
            else:
                derrota = (inicio - pontos)
                msg_derrota = (f"  Você perdeu {derrota} pontos  ")
                print("-"*len(msg_derrota))
                print(msg_derrota)
                print("-"*len(msg_derrota))
                if pontos <= 299:
                    divisao = "Bronze I"
                elif 300 <= pontos <= 599:
                    divisao = "Bronze II"
                elif 600 <= pontos <= 899:
                    divisao = "Bronze III"
                elif 900 <= pontos <= 1299:
                    divisao = "Prata I"
                elif 1300 <= pontos <= 1699:
                    divisao = "Prata II"
                elif 1700 <= pontos <= 2099:
                    divisao = "Prata III"
                elif 2100 <= pontos <= 2599:
                    divisao = "Ouro I"
                elif 2600 <= pontos <= 3099:
                    divisao = "Ouro II"
                elif 3100 <= pontos <= 3599:
                    divisao = "Ouro III"
                elif 3600 <= pontos <= 4199:
                    divisao = "Platina I"
                elif 4200 <= pontos <= 4799:
                    divisao = "Platina II"
                elif 4800 <= pontos <= 5399:
                    divisao = "Platina III"
                elif 5400 <= pontos <= 6099:
                    divisao = "Diamante I"
                elif 6100 <= pontos <= 6799:
                    divisao = "Diamante II"
                elif 6800 <= pontos <= 7499:
                    divisao = "Diamante III"
                elif 7500 <= pontos <= 8199:
                    divisao = "Carmesim I"
                elif 8200 <= pontos <= 8899:
                    divisao = "Carmesim II"
                elif 9600 <= pontos <= 9999:
                    divisao = "Iridescent"
                elif pontos >= 10000:
                    divisao = "TOP 250"