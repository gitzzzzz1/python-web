# CAP 4 - Atividade 1 Palavras e Funções

def gg():
    print("*************************")
    print("----- Jogo da forca -----")
    print("*************************")
    print("GG forca")
    print('\nObrigado por participar!\n')
    palavra_secreta = "banana"

    morreu = False
    acertou = False

    while(not morreu and not acertou):
        tentativa = input("Qual a letra? ")
        tentativa = tentativa.strip()

        index = 0
        for letra in palavra_secreta:
            if (tentativa.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}"
                    .format(letra, index))  
                
            index +=1
        print("GG forca")
    print('\nObrigado por participar!\n')

if(__name__ == "__main__"):
        gg()