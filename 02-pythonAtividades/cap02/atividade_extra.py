# ==================================
# ------------ PROJETOS ------------
# ==================================
# # Cap. 1
print('Olá Aluno(a)!')
print('Olá {}' . format(input('Qual seu nome? ') + '!'))
print('Seja bem-vindo a aula de' , 'Python II')

# Cap. 2
print("-" * 35)
print("Adivinhe qual é o número secreto!")
print("-" * 35)
numero_secreto = 82
tentativa = input("Tente acertar o número secreto: ")
print("Você digitou: ", tentativa)
tentativa_int = int(tentativa)
if (numero_secreto == tentativa_int):
    print("Boa tentativa. ACERTOU!")
else:
    print("Não foi dessa vez. ERROU!")
print('Obrigado por participar!')

# Ex.: 3 e 4
from os import system
system('cls')
numero_secreto = 82
total_de_tentativa = 3 
for rodada in range(1, total_de_tentativa + 1):
    print("\nTentativa {:02d} de {:02d}" 
          .format(rodada, total_de_tentativa))
    tentativa = input("Tente acerta o número de 1 a 100: ")
    print("Você digitou: ", tentativa)
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
        print("Não foi dessa vez. TENTE NOVAMENTE!")
    if (ehmaior):
        print("Sua tentativa foi MAIOR que o número secreto.")
    if (ehmenor):
        print("Que pena, sua tentativa foi MENOR que o número secreto.")
    rodada = rodada + 1
print('\nObrigado por participar!\n')