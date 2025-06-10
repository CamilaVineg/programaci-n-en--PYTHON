# 2. Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de
# caracteres.

from List import List
import random


class Letra:
    def __init__(self, letr):
        self.letr = letr

    def __str__(self):
        return self.letr


def eliminar_vocales(lista_de_letras):
    cont = 0
    for letra in lista_de_letras[:]:  # Copia para evitar problemas al eliminar
        if letra.letr in 'aeiou':
            lista_de_letras.eliminar_elemento(letra.letr, 'letr')
            cont += 1
    return lista_de_letras, cont


lista_de_letras = List()
lista_de_letras.agregar_criterio('letr', lambda x: x.letr)

for i in range(20):
    letra = chr(random.randint(97, 122))
    lista_de_letras.append(Letra(letra))

print("Lista original de letras generada automáticamente:")
lista_de_letras.mostrar()

lista_de_letras, total_vocales = eliminar_vocales(lista_de_letras)
print(f"Se han eliminado {total_vocales} vocales de la lista.")
print("\nLista sin vocales:")
lista_de_letras.mostrar()
