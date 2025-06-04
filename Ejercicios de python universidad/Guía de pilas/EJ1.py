# 1. Determinar el número de ocurrencias de un determinado elemento en una pila.

from Stack_ import Stack


def conteo_apariciones(pila_de_elementos):
    pila_aux = Stack()
    cont = 0

    while not pila_de_elementos.esta_vacia():

        nom = pila_de_elementos.desapilar()

        if nom == "María":
            cont += 1

        pila_aux.apilar(nom)

    while not pila_aux.esta_vacia():
        pila_de_elementos.apilar(pila_aux.desapilar())

    return cont


pila_de_elementos = Stack()

Lista_nombres = ["Camila", "Lautaro", "Roberto", "Vannessa", "Gabriel", "María",
                 "Maxxivia", "Olivia", "María", "Hugo", "Martina", "María"]


for nombre in Lista_nombres:
    pila_de_elementos.apilar(nombre)

resultado = conteo_apariciones(pila_de_elementos)
print("Contar cuántas veces el nombre María se repite en la lista.")
print(f"El nombre María se repite {resultado} veces.")
