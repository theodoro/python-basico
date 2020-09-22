import random

lista = [] # Declara um lista vazia
k = 0

while k <= 5: # repete até a posição 5

    #Alimenta a lista com os nomes
    lista.append(input('Informe um nome: '))
    k = k + 1
#Imprime um nome aleatório
print(random.choice(lista))
