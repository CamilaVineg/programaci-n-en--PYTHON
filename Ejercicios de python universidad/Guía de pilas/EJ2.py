# 2. Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden nú-
# meros pares.

from Stack_ import Stack


def eliminar_impares(pila_de_numeros):
    pila_aux = Stack()

    while not pila_de_numeros.esta_vacia():

        num = pila_de_numeros.desapilar()
        if num % 2 == 0:
            pila_aux.apilar(num)

    while not pila_aux.esta_vacia():
        pila_de_numeros.apilar(pila_aux.desapilar())

    return pila_de_numeros


pila_de_numeros = Stack()

Lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for numero in Lista_numeros:
    pila_de_numeros.apilar(numero)

eliminar_impares(pila_de_numeros)
print("Según una lista de números del 1 al 20, se eliminarán los números impares.")
print("Lista actualizada")
pila_de_numeros.mostrar()
