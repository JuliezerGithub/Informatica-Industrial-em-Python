# Aula 03 - Introdução ao Python: Coleções, condicionais e loops

#Lista
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

# Dicionários
dicionario = {"curso":"informatica industrial", "número":4}
print(dicionario)

#Mudar elemento do dicionario

dicionario["curso"] = "Robótica Móvel"
print(dicionario)
