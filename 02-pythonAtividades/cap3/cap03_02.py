# Atividade 2
''' 
Objetivo criar um sistema de dificuldade e pontuação 
Utilizar condições e cálculos relacionados
'''
''' Números e funções
importar módulos e usar funções 
utilizar um número aleaório, condições e cálculos relacionados
Carregar arquivos externos como módulos
Criar e/definir funções
Carregar corretamente módulose e funções interna e extenamente.'''

import random
from os import system
system("cls")
print("*************************")
print("Adivinhe qual é o Número!")
print("*************************")
numero_secreto=random.randrange(0,101)
#aqui usamos a randrange, gera um numero aleatório entre 0 e 100
total_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade ?")
print("(1) Padawan \n(2) Cavalheiro \n(3) Meste Jedi")
nivel = int(input("\nDefina o nível: "))


if (nivel == 1):
    total_de_tentativas = 20
elif(nivel== 2):
    #elif é usado quando temos mais critérios e escolhas dentro de um if
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
pontos_a_perder = int(pontos / total_de_tentativas)
print("Sua pontuação atual: ", pontos)

for rodada in range(1,total_de_tentativas + 1):
    print("\nTentativa {:02d} de {:02d}"
          .format(rodada,total_de_tentativas))
    tentativa = input("Tente acertar o número de 1 a 100: ")
    print("Você digitou: ", tentativa)
    tentativa_int = int(tentativa)

    if(tentativa_int < 1 or tentativa_int >100):
        print("Tentativa INVÁLIDA! Somente números de 1 a 100!")
        continue
    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto

    if (acerto):
        print("Boa tentativa. ACERTOU! fez {} pontos!"
              .format(pontos))
        break
    else:
        pontos_proximidade = 50 - abs(numero_secreto - tentativa_int)
        pontos = (pontos - pontos_a_perder + pontos_proximidade)
        print("Não foi dessa vez. ERROU!")
        if (ehmaior):
            print("Sua tentativa foi MAIOR que o número secreto.")
        elif (ehmenor):
            print("Sua tentativa foi MENOR que o número secreto.")
        if (rodada <total_de_tentativas):
            print("Sua pontuação atual: ",pontos)
        else:
            print("\n -----------------------")
            print("O número secreto era {}.".format(numero_secreto))
            print("Sua pontuação FINAL: ",pontos)
            print("GAME OVER")
            print("\n -----------------------")
print("\n Obrigado por participar! \n")
