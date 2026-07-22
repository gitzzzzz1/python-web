# 2 - a. Biblioteca
'''from os import system
# importa biblioteca do sistema
system('cls')''' # limpa tela

# 3. Executar
# Atividade Anterior (1)
'''print("*******************")
print("Adivinhe qual é o Número!")
print("*******************")'''

# 4.
'''numero_secreto = 82
tentativa = input("Tente acertar o número: ")
print("Você digitou: ", tentativa)
tentativa_int = int(tentativa)
if (numero_secreto == tentativa_int):
    print("Boa tentativa. ACERTOU!")
else:
    print("Não foi dessa vez. ERROU!")
print("GAME OVER!")
print('Obrigado por participar!')'''

# Atividade 2 - Mais estruturas de decisão

# Aproveitando para falar de identação (4 espaços ou tab).
# identação é parte do código Python e faz diferenças em código.
'''if (numero_secreto == tentativa_int):
    print("Boa tentativa. ACERTOU!")
    else:
    print("Não foi dessa vez. ERROU!")
    # Clocamos novas condições, lembrando que a identação definirá a inserção
    if (tentativa_int > numero_secreto):
        print("Sua tentativa foi MAIOR que o número secreto.")
    if (tentativa_int < numero_secreto):
        print("Sua tentativa foi MENOR que o número secreto.")
    print("GAME OVER!")
print('Obrigado por participar!')'''

# 3. 
'''acerto =  tentativa_int == numero_secreto
ehmaior = tentativa_int > numero_secreto
ehmenor = tentativa_int < numero_secreto
# Compara as condições e sempre retorna true ou false

# Aproveitamos para falar de identação (4 espaços ou tab)
# Identação é parte do código Pyhton e faz diferenças em código
if (acerto):
    print("Boa tentativa. ACERTOU!")
else:
    print("Não foi dessa vez. ERROU!")
    # Colocamos novas condições, Lembrando que a identação definira a iserção.
    if (ehmaior):
        print("Sua tentativa foi MAIOR que o número secreto.")
        if (ehmenor):
            print("Sua tentativa foi MENOR que o número secreto.")
        print("GAME OVER!")
    print('Obrigado por participar!')
# 4.
total_de_tentativas = 3'''
# enquanto ainda há  total_de_tentativas:
#    executa o código

# 5. numero_secreto = 82
# Vamos definir a rodada inicial e o total de rodadas
'''rodada = 1
total_de_tentativa = 3

# O Laço rá englobar todo o código a repetir
# 6.
while (rodada <= total_de_tentativa ):
    print("\Tentativa {:02d} de {:02d}"
    .format(rodada, total_de_tentativa))'''

# 7.
'''rodada = rodada + 1'''
