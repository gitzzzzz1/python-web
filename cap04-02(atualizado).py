def gg(): 
# def nome_funcao(), cria uma função, basta identar o código para 

    print("****************************") 
    print("------ Jogo da forca ------ ") 
    print("****************************") 
 
    palavra_secreta = "banana" 
 
morreu = False 
acertou = False 
# enquanto não morreu E não acertou 
# enquanto não False 
# enquanto(true) 

while(not morreu and not acertou): 
 
    tentativa = input("Qual a letra? ")
    letras_acertadas = ["_", "_", "_", "_", "_", "_" ]

palavra_secreta = "banana".upper()

tentativa = tentativa.strip().upper()
    
if (tentativa == letra):

#palavra_secreta = "banana"

if(tentativa in palavra_secreta):

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

letras_acertadas = ["_" for letra in palavra_secreta]