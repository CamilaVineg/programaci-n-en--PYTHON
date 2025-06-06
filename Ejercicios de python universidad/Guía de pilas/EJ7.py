# 7. Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras.

from Stack_ import Stack


def eliminar(pila_de_flores, posicion):
    pila_aux = Stack()
    cont = 0

    while pila_de_flores.tamanio() > 0:
        elemento = pila_de_flores.desapilar()
        if cont == posicion:
            print(f"Se ha eliminado {elemento} de la lista")
        else:
            pila_aux.apilar(elemento)

        cont += 1

    while pila_aux.tamanio() > 0:
        pila_de_flores.apilar(pila_aux.desapilar())

    return pila_de_flores


pila_de_flores = Stack()

lista_de_flores = ["1. Tulipan", "2. Lirios", "3. Lavanda", "4. Dalia", "5. Orquídea",
                   "6. Peonía", "7. Camelia", "8. Hortensia", "9. Crisantemo", "10. Amapola", "11. Margarita"]

for flor in lista_de_flores:
    pila_de_flores.apilar(flor)

print("Esta es la pila original")
pila_de_flores.mostrar()

while True:

    posicion = int(input(
        "Ingrese la posicion del elemento que desea eliminar(esta tiene que estar por debajo del tope): "))

    if posicion >= pila_de_flores.tamanio():
        print("La posición no es válida. Vuelva a intentarlo.")
    else:
        print("Esta pila ha sido actualizada con el elemento que ha decidido eliminar:")

        eliminar(pila_de_flores, posicion)

        pila_de_flores.mostrar()
        break
