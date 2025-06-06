# 10. Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una
# pila con nombres de dioses griegos.

from Stack_ import Stack


def insertar_atenea(dioses_del_olimpo, posicion_deseada, dios_insertada):
    pila_aux = Stack()
    contador = 0

    while dioses_del_olimpo.tamanio() > 0 and contador < posicion_deseada:
        pila_aux.apilar(dioses_del_olimpo.desapilar())
        contador += 1

    dioses_del_olimpo.apilar(dios_insertada)

    while pila_aux.tamanio() > 0:
        dioses_del_olimpo.apilar(pila_aux.desapilar())

    return dioses_del_olimpo


def preguntar_posicion(posicion_deseada, dioses_del_olimpo):
    posicion_deseada = int(
        input("Ingrese la posicion en que quiera agregar a la diosa Atenea: "))
    return posicion_deseada


# programa principal
dioses_del_olimpo = Stack()

lista_de_dioses = ["Zeus", "Hera", "Poseidón", "Deméter", "Apolo", "Artemisa",
                   "Ares", "Afrodita", "Hefesto", "Hermes", "Dionisio"]

for dios in lista_de_dioses:
    dioses_del_olimpo.apilar(dios)

dios_insertada = "Atenea"
posicion_deseada = -1

while True:
    posicion_deseada = preguntar_posicion(posicion_deseada, dioses_del_olimpo)

    if posicion_deseada >= dioses_del_olimpo.tamanio():
        print(
            "❌ La posicion deseada debe estar por debajo de la cima. Intentelo nuevamente.")
    else:
        insertar_atenea(dioses_del_olimpo, posicion_deseada, dios_insertada)
        print(
            f"✅ La diosa Atenea se ha insertado con éxito en la pila en la posición {posicion_deseada}.")
        print("📌 Pila actualizada:")
        dioses_del_olimpo.mostrar()
        break
