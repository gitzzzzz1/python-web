# Atividade 1 - Variáveis e Estrutura de decisão
print("*******************")
print("Adivinhe qual é o Número!")
print("*******************")
# Aproveitamos para relembrar constantes e variaveis
numero_secreto = 82

tentativa = input("Tente acertar o número: ")
print("Você digitou: ", tentativa)

tentativa_int = int(tentativa)

# Aproveitamos para falar de identação (4 espaços ou tab)
# Identação é parte do código Pyhton e faz diferenças e, código
if (numero_secreto == tentativa_int):
    print("Boa tentativa. ACERTOU!")
else:
    print("Não foi dessa vez. ERROU!")

print("GAME OVER!")
print('Obrigado por participar!')