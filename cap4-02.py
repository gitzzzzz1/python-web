def gg():

    print("****************************")
    print("------ Jogo da Forca ------")
    print("****************************")

    palavra_secreta = "BANANA"

    letras_acertadas = ["_" for letra in palavra_secreta]

    erros = 0
    morreu = False
    acertou = False

    while not morreu and not acertou:

        print(letras_acertadas)

        tentativa = input("Qual a letra? ")
        tentativa = tentativa.strip().upper()

        if tentativa in palavra_secreta:

            index = 0

            for letra in palavra_secreta:

                if tentativa == letra:
                    letras_acertadas[index] = letra

                index += 1

        else:
            erros += 1

        morreu = erros == 7
        acertou = "_" not in letras_acertadas

    print(letras_acertadas)

    if acertou:
        print("Venceu!")
    else:
        print("Perdeu!")

palavra_secreta = "jabuticaba".upper()
letras_acertadas = []

for letra in palavra_secreta:
    letras_acertadas.append("_")

letras_acertadas = ["_" for letra in palavra]


gg()