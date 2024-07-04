# Aula 03 - Introdução ao Python: Coleções, condicionais e loops

#Lista -  Serie de elementos que pode ser alterado
lista = [1, 2, "Juliezer", 5.5, True, 'a'] # Fracamente tipada

for x in lista:
    print(x)

lista.append("Soares")
lista[0] = 55
print('\n')
for x in range(0,len(lista)):
    if x == 2:
        continue # Vai pular a posição na lista
    print(lista[x])

# Dicionários - Os elementos de um dicionário recebem uma chave para associar seus valores
dicionario = {"curso":"informatica industrial", "número":4}
print(dicionario)

#Mudar elemento do dicionario

dicionario["curso"] = "Robótica Móvel"
dicionario["NumeroHoras"] = 60

print(dicionario)

# Tuplas - Elementos de uma Tupla não podem ser alterados

tupla = (1, 2, "Juliezer", 5.5, True, 'a')
print()
for x in tupla:
    print(x)

# Coleções Ordenadas:

pilha = []

for i in range(0,10):
    pilha.append(i)

for i in range(0,10):
    print(pilha.pop(), end=" ")

print()

from collections import deque

fila = deque()

for i in range(0,10):
    fila.append(i)

for i in range(0,10):
    print(fila.popleft(), end=" ")