# 3. Reemplazar todas las ocurrencias de un determinado elemento en una pila.

from Stack_ import Stack


def remplazo_repetidos(pila_de_palabras):
    pila_aux = Stack()

    while not pila_de_palabras.esta_vacia():
        palabra = pila_de_palabras.desapilar()

        if palabra == "Hola":
            palabra = palabra.replace("Hola", "Python")

        pila_aux.apilar(palabra)

    while not pila_aux.esta_vacia():
        pila_de_palabras.apilar(pila_aux.desapilar())

    return pila_de_palabras


pila_de_palabras = Stack()

lista_palabras = ["Hola", "Adiós", "Camila", "Mundo", "Hola",
                  "Animales", "Hola", "Stack", "Código", "Programación"]

for palabra in lista_palabras:
    pila_de_palabras.apilar(palabra)

remplazo_repetidos(pila_de_palabras)

print("Sea la lista:")
for palabra in lista_palabras:
    print(f"{palabra}")

print("Se reemplazá la palabra Hola oie Python")
print("Lista actualizada")
pila_de_palabras.mostrar()
