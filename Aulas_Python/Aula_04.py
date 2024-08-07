# Aula 4 - Introdução ao Python: Variáveis e Objetos

# Objetos Imutáveis -  Recebem referencias diferentes
#nome (variável) | objeto

a = 3
b = a
b = 4

print("Valor: ", a)
print("Identificador a: ", id(a))
print("Identificador b: ", id(b))

a+= 3

print("Identificador a: ", id(a))
print("Valor: ", a)
print("Identificador a: ", id(a))

a = "informatica"

print("Valor: ", a)
print("Identificador a: ", id(a))

# Objetos Mutáveis - Recebem a mesma referência
#nome (variável) | objeto

a =  [1,2,3]
b = a
b.append(4)

print("Valor: ", a)
print("Identificador a: ", id(a))
print("Identificador b: ", id(b))