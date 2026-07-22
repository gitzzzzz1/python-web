



palavra_secreta = "banana"
letras_acertadas = ["_", "_", "_", "_", "_", "_" ]

index = 0
for letra in palavra_secreta:
    if (tentativa.upper() == letra.upper()):
        letras_acertadas[index] = letra
    index += 1

    print(letras_acertadas)

    palavra_secreta = "banana".upper()

    tentativa.strip().upper()
    
    if (tentativa == letra):

    index = 0
    for letra in palavra_secreta:
        if (tentativa.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1
        else:
            erros += 1
            
            morreu = erros == 7
            acertou = "_" not in letras_acertadas

            print(letras_acertadas)

            if (acertou):
                print("Venceu!")
            else:
                print("Perdeu")

palavra_secreta = "jabuticaba".upper()
letras_acertadas = []

for letra in palavra_secreta:
    letras_acertadas.append("_")

letras_acertadas = ["_" for letra in palavra]

