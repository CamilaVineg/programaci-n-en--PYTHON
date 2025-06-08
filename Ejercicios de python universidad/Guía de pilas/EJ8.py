# 8. Dada una pila de cartas de las cuales se conoce su número y palo,–que representa un mazo de
# cartas de baraja española–,resolver las siguientes actividades:
# .a. generar las cartas del mazo de forma aleatoria;
# b. separar la pila mazo en cuatro pilas una por cada palo;
# c. ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente.

from Stack_ import Stack

import random

# b)))) separar la pila mazo en cuatro pilas una por cada palo


def separar_palos(mazo_español):
    pila_basto = Stack()
    pila_espada = Stack()
    pila_copa = Stack()
    pila_oro = Stack()

    while mazo_español.tamanio() > 0:
        carta = mazo_español.desapilar()
        if carta[1] == "Basto":
            pila_basto.apilar(carta)
        elif carta[1] == "Espada":
            pila_espada.apilar(carta)
        elif carta[1] == "Copa":
            pila_copa.apilar(carta)
        elif carta[1] == "Oro":
            pila_oro.apilar(carta)

    return pila_basto, pila_espada, pila_copa, pila_oro

# c))) ordenar una de las cuatro pilas (espada, basto, copa u oro) de manera creciente


def ordenar_pila(pila_basto):
    """
    Ordena una pila de cartas del palo de basto de manera creciente por su número."""
    pila_aux = Stack()
    while pila_basto.tamanio() > 0:
        carta = pila_basto.desapilar()
        while pila_aux.tamanio() > 0 and int(carta[0]) < int(pila_aux.ver_tope()[0]):
            pila_basto.apilar(pila_aux.desapilar())
        pila_aux.apilar(carta)

    while pila_aux.tamanio() > 0:
        pila_basto.apilar(pila_aux.desapilar())
    return pila_basto


# PROGRAMA PRINCIPAL
# a)))) creando listas del palo y los numeros de la baraja española
palos = ["Espada", "Basto", "Copa", "Oro"]

numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
# generando el mazo de cartas

mazo = [(numero, palo) for palo in palos for numero in numeros]

# mezclando el mazo de cartas
random.shuffle(mazo)

# creando una pila para el mazo de cartas y apilando las cartas
mazo_español = Stack()

for carta in mazo:
    mazo_español.apilar(carta)


print("Mazo de cartas español:")
mazo_español.mostrar()

pila_basto, pila_espada, pila_copa, pila_oro = separar_palos(mazo_español)

print("Pila de cartas del palo de espada")
pila_espada.mostrar()
print("Pila de cartas del palo de basto")
pila_basto.mostrar()
print("Pila de cartas del palo de copa")
pila_copa.mostrar()
print("Pila de cartas del palo de oro")
pila_oro.mostrar()
print("Pila de cartas del palo de basto ordenada")
pila_basto = ordenar_pila(pila_basto)
pila_basto.mostrar()
