# Atividade 4 Usando FOR para (repetições)

from os import system
system('cls') # limpa tela 
print("*******************")
print("Adivinhe qual é o Número!")
print("*******************")
numero_secreto = 82
total_de_tentativa = 3 

# Laço irá englobar o total de tentativa
for rodada in range(1, total_de_tentativa + 1):
    print("\nTentativa {:02d} de {:02d}" 
          .format(rodada, total_de_tentativa))
    
    tentativa = input("Tente acerta o número de 1 a 100: ")
    print("Você digitou: ", tentativa)

    # covertendo a string a int
    tentativa_int = int(tentativa)
    if(tentativa_int < 1 or tentativa_int > 100):
        print("Tentativa INVÁLIDA! Somente números de 1 a 100")
        
    acerto = tentativa_int == numero_secreto
    ehmaior = tentativa_int > numero_secreto
    ehmenor = tentativa_int < numero_secreto
    if (acerto):
        print("Boa tentativa, ACERTOU!\n")
        break
    else:
        print("Não foi dessa vez. ERROU!")
    if (ehmaior):
        print("Sua tentativa foi MAIOR que o número secreto.")
    if (ehmenor):
        print("Sua tentativa foi MENOR que o número secreto.")

    rodada = rodada + 1

print('\nObrigado por participar!\n')

