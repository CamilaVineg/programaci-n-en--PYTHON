# 1. Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
from List import List


class Mascotas:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def __str__(self):
        return f"{self.nombre}, {self.edad} - {self.especie}"


# def order_by_name(item):
#     return item.nombre


def contar_elementos(lista_de_mascotas):
    contador = 0
    for mascota in lista_de_mascotas:
        contador += 1

    return contador


lista_de_mascotas = List()

mascotitas = [
    Mascotas(nombre="Martita", edad=3, especie="loro"),
    Mascotas(nombre="Baboso", edad=7, especie="gato"),
    Mascotas(nombre="Polenta", edad=1, especie="gato"),
    Mascotas(nombre="Milanesa", edad=13, especie="perro"),
    Mascotas(nombre="Blanca", edad=4, especie="cuyo"),
    Mascotas(nombre="Tostado", edad=5, especie="carpincho"),
    Mascotas(nombre="Tanque", edad=24, especie="tortuga"),
    Mascotas(nombre="Tinta", edad=6, especie="gato"),
    Mascotas(nombre="Aquilles", edad=10, especie="caballo"),
    Mascotas(nombre="Manzanita", edad=2, especie="cerdo")]

for masc in mascotitas:
    lista_de_mascotas.append(masc)

# Lista_de_mascotas.agregar_criterio('nombre', order_by_name)

total_elementos = contar_elementos(lista_de_mascotas)
print(f"Total de mascotas en la lista: {total_elementos}")

print("Lista de mascotas:")

lista_de_mascotas.mostrar()

# lista_de_mascotas.ordenar_por_criterio('nombre')
# print()
# print("Lista de mascotas ordenadas por nombre:")
# lista_de_mascotas.mostrar()
