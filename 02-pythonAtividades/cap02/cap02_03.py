# Atividade 3 trabalhando com While (repetições)
# 8. Código completo até aqui
from os import system
# importa biblioteca do sistema
system('cls') # limpa tela 
print("*******************")
print("Adivinhe qual é o Número!")
print("*******************")
# relembrando
numero_secreto = 82

# definindo a rodada inicial e o total de rodadas
rodada = 1
total_de_tentativa = 3 

# O Laço rá englobar todo o código a repetir 
while (rodada <= total_de_tentativa ):
    print("\nTentativa {:02d} de {:02d}" # a. utilização de {} , b.\n e c {:02d}.
          .format(rodada, total_de_tentativa))

# selecione, precionane tab e recue todo o código para identar dentro do while
    tentativa = input("Tente acerta o número: ")
    print("Você digitou: ", tentativa)

# é preciso converter a strin para int para haver compração correta no if
    tentativa_int = int(tentativa)
    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto
# compara as condições e sempre retorna true ou false

    if (acerto):
        print("Boa tentativa, ACERTOU!\n")
        break # 9.
    else:
        print("Não foi dessa vez. ERROU!")
    if (ehmaior):
        print("Sua tentativa foi MAIOR que o número secreto.")
    if (ehmenor):
        print("Sua tentativa foi MENOR que o número secreto.")

    rodada = rodada + 1

print('\nObrigado por participar!\n')

