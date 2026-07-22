# from os import system
# system("cls") # Limpa tela

import aforca
import adivinhe

def escolha_jogo():
    from os import system
    system('cls')

    print("*************************")
    print("-- Escolha o seu Game! --")
    print("*************************")

    print("(1) Forca \n(2) Adivinhe o número")
    jogo = int(input("Qual vai ser o game? "))

    if (jogo == 1):
        print("GG forca")
        aforca.gg()
    elif (jogo == 2):
        print("GG adivinhe")
        adivinhe.gg()
if(__name__ == "__main__"):
    escolha_jogo()


