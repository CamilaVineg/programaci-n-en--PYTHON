# Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden orde-
# nados de forma creciente. Solo puede utilizar una pila auxiliar como estructura extra –no se
# pueden utilizar métodos de ordenamiento–.
from Stack_ import Stack
# cargando pila
pila_nombres = Stack()
while True:
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    pila_nombres.apilar(nombre)


def ordenar_de_menor_a_mayor(pila_nombres):
    pila_aux = Stack()
    while pila_nombres.tamanio() > 0:
        nom = pila_nombres.desapilar()
        if pila_aux.tamanio() == 0 or nom <= pila_aux.ver_tope():
            pila_aux.apilar(nom)
        else:
            while pila_aux.tamanio() > 0 and nom > pila_aux.ver_tope():
                pila_nombres.apilar(pila_aux.desapilar())
            pila_aux.apilar(nom)
    while pila_aux.tamanio() > 0:
        pila_nombres.apilar(pila_aux.desapilar())


ordenar_de_menor_a_mayor(pila_nombres)
# Mostrando pila ordenada
print("Pila ordenada de menor a mayor:")
pila_nombres.mostrar()
