# 11. Dada una pila de letras determinar cuántas vocales contiene.
from Stack_ import Stack
import random


def contar_vocales(pila_de_letras):
    cont = 0
    pila_aux = Stack()
    while pila_de_letras.tamanio() > 0:
        letra = pila_de_letras.desapilar()
        if letra in 'aeiou':
            cont += 1
        pila_aux.apilar(letra)

    while pila_aux.tamanio() > 0:
        pila_de_letras.apilar(pila_aux.desapilar())

    return cont


pila_de_letras = Stack()

for letra in range(20):
    letra_aleatoria = chr(random.randint(97, 122))
    pila_de_letras.apilar(letra_aleatoria)

print("Esta es la pila de letras generada automáticamente:")
pila_de_letras.mostrar()

total_vocales = contar_vocales(pila_de_letras)
print(f"Dentro de la pila hay {total_vocales} vocales.")
