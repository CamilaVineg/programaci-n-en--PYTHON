# 4. Implementar un algoritmo que inserte un nodo en la i-ésima posición de una lista.
from List import List


def insertar_en_posicion(lista_de_flores, nueva_flor, posicion):
    lista_de_flores.insert(posicion, nueva_flor)

    return lista_de_flores


def determinando_posicion(lista_de_flores, posicion):
    if posicion < 0:
        print("La posición es negativa, se insertará al inicio de la lista.")
        posicion = 0
        lista_de_flores = insertar_en_posicion(
            lista_de_flores, nueva_flor, posicion)
    elif posicion > len(lista_de_flores):
        print("La posición es mayor que la longitud de la lista, se insertará al final de la lista.")
        posicion = len(lista_de_flores)
        lista_de_flores = insertar_en_posicion(
            lista_de_flores, nueva_flor, posicion)
    else:
        lista_de_flores = insertar_en_posicion(
            lista_de_flores, nueva_flor, posicion)
    return posicion


lista_de_flores = List()

flores = ["🌸 Tulipan", "🌸 Lirios", "🌸 Lavanda", "🌸 Dalia", "🌸 Orquídea",
          "🌸 Peonía", "🌸 Camelia", "🌸 Hortensia", "🌸 Crisantemo", "🌸 Amapola",
          "🌸 Margarita"]

for flor in flores:
    lista_de_flores.append(flor)

print("Esta es la lista de flores original.")
lista_de_flores.mostrar()
print()
nueva_flor = ("🌸 ") + \
    input("Ingrese el nombre de la flor que desea insertar: ")
posicion = int(
    input("Ingrese la posición en la que desea insertar la flor(0 para el inicio): "))

determinando_posicion(lista_de_flores, posicion)
print()
print("🌸 Se está insertando la nueva flor en la lista. Espere un momento...🌸")
print("----")
print("🌼¡La flor ha sido insertada correctamente!🌼")
print("----")
print("🌼Esta es la lista de flores actualizada.")
print()
lista_de_flores.mostrar()
