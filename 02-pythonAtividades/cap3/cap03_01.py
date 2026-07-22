# Atividade 1 Variáveis e Estruturas de decisão
''' Números e funções

importar módulos e usar funções 
utilizar um número aleaório, condições e cálculos relacionados
Carregar arquivos externos como módulos
Criar e/definir funções
Carregar corretamente módulose e funções interna e extenamente.'''

import random
numero_secreto = int(93.9065044957198)
print('Int: ',numero_secreto)
# int retira a parte decimal.

numero_secreto = round(93.9065044957198)
print('Round: ',numero_secreto)
# round arredonda

numero_secreto=round(random.random()*100)
print('Random: ',numero_secreto)
#Agora inserindo um número randomico (decimal entre 1 e 10, por isso * 100)

numero_secreto=random.randrange(0,101)
print('Randrange: ',numero_secreto)
#aqui usamos a randrange, gera um numero aleatório entre 0 e 100
