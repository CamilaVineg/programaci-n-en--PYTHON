# 3. Dada una lista de números enteros, implementar un algoritmo para dividir dicha lista en dos,
# una que contenga los números pares y otra para los números impares.

from List import List
import random


def separando_pares_impares(lista_de_numeros):
    lista_pares = List()
    lista_impares = List()

    for numero in lista_de_numeros:
        if numero % 2 == 0:
            lista_pares.append(numero)
        else:
            lista_impares.append(numero)

    return lista_pares, lista_impares


lista_de_numeros = List()

for i in range(20):
    numero_aleatorio = random.randint(1, 15)
    lista_de_numeros.append(numero_aleatorio)

print("Esta es la lista de números generada automáticamente:")
lista_de_numeros.mostrar()

pares, impares = separando_pares_impares(lista_de_numeros)
print("Esta es la lista de números pares:")
pares.mostrar()
print("Esta es la lista de números impares:")
impares.mostrar()
