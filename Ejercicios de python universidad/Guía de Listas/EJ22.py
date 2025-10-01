# 22. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

from List import List


class Jedi:
    def __init__(self, nombre, maestro, colores_sable, especie):
        self.nombre = nombre
        self.maestro = maestro
        self.colores_sable = colores_sable
        self.especie = especie

    def __str__(self):
        return f"Nombre: {self.nombre}, Maestro: {self.maestro}, Colores de Sable: {self.colores_sable}, Especie: {self.especie}"


def ordenar_por_nombre(item):
    return item.nombre


def ordenar_por_especie(item):
    return item.especie


lista_de_jedi = List()

Jedies = [
    Jedi(
        nombre="Ahsoka Tano",
        maestro="Anakin Skywalker",
        colores_sable=["Verde", "Azul"],
        especie="Togruta"
    ),
    Jedi(
        nombre="Kit Fisto",
        maestro="Yoda",
        colores_sable=["Verde"],
        especie="Nautolano"
    ),
    Jedi(
        nombre="Obi-Wan Kenobi",
        maestro="Qui-Gon Jin",
        colores_sable=["Azul"],
        especie="Humano"
    ),
    Jedi(
        nombre="Anakin Skywalker",
        maestro="Obi-Wan Kenobi",
        colores_sable=["Azul"],
        especie="Humano"
    ),
    Jedi(
        nombre="Yoda",
        maestro=None,
        colores_sable=["Verde"],
        especie="Desconocida"
    ),
    Jedi(
        nombre="Mace Windu",
        maestro=None,
        colores_sable=["Violeta"],
        especie="Humano"
    ),
    Jedi(
        nombre="Luke Skywalker",
        maestro="Obi-Wan Kenobi",
        colores_sable=["Verde"],
        especie="Humano"
    ),
    Jedi(
        nombre="Qui-Gon Jin",
        maestro=None,
        colores_sable=["Verde"],
        especie="Humano"
    ),
    Jedi(
        nombre="Luminara Unduli",
        maestro=None,
        colores_sable=["Verde"],
        especie="Mirialiano"
    ),
    Jedi(
        nombre="Barriss Offee",
        maestro="Luminara Unduli",
        colores_sable=["Azul"],
        especie="Mirialiano"
    ),
    Jedi(
        nombre="Aayla Secura",
        maestro=None,
        colores_sable=["Azul"],
        especie="Twi'lek"
    ),
    Jedi(
        nombre="Shaak Ti",
        maestro=None,
        colores_sable=["Rojo", "Azul"],
        especie="Togruta"
    )
]

for jedi in Jedies:
    lista_de_jedi.append(jedi)

lista_de_jedi.agregar_criterio('nombre', ordenar_por_nombre)
lista_de_jedi.agregar_criterio('especie', ordenar_por_especie)

# a) listado ordenado por nombre y por especie:
lista_de_jedi.ordenar_por_criterio('nombre')
print("Listado ordenado por nombre:")
lista_de_jedi.mostrar()
print()

lista_de_jedi.ordenar_por_criterio('especie')
print("Listado ordenado por especie:")
lista_de_jedi.mostrar()
print()

# b) mostrar toda la informacion de Ahsoka Tano y Kit Fisto.

print("Informacion de Ahsoka Tano y Kit Fisto:")
index_tano = lista_de_jedi.buscar("Ahsoka Tano", "nombre")
index_fisto = lista_de_jedi.buscar("Kit Fisto", "nombre")

if index_tano is not None:
    tano = lista_de_jedi[index_tano]
    print(tano)
else:
    print("Ahsoka Tano no se encuentra en la lista")

if index_fisto is not None:
    fisto = lista_de_jedi[index_fisto]
    print(fisto)
else:
    print("Kit Fisto no se encuentra en la lista")

print()
# c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices.

print("Padawan de Yoda y Luke Skywalker:")
print()
padawan_yoda = 0  # contador para saber si Yoda tuvo padawans
padawan_luke = 0  # contador para saber si Luke Skywalker tuvo padaw
for jedi in lista_de_jedi:
    if jedi.maestro == "Yoda":
        padawan_yoda += 1
        print(f"Padawan de Yoda: {jedi.nombre}")
    if jedi.maestro == "Luke Skywalker":
        print(f"Padawan de Luke Skywalker: {jedi.nombre}")
        padawan_luke += 1

if padawan_yoda == 0:
    print("Yoda no tuvo padawans")

if padawan_luke == 0:
    print("Luke Skywalker no tuvo padawans")

print()
# d) mostrar los Jedi de especie humana y twi'lek.
print("Jedi de especie humana y twi'lek:")
print("Especie Humana:")
esp_humana = 0  # contador para saber si hay jedies de especie humana
for jedi in lista_de_jedi:
    if jedi.especie == "Humano":
        esp_humana += 1
        print(jedi)

if esp_humana == 0:
    print("No hay jedies de especie humana")

print("Especie Twi'lek:")
esp_twi = 0  # contador para saber si hay jedies de especie twi'lek
for jedi in lista_de_jedi:
    if jedi.especie == "Twi'lek":
        esp_twi += 1
        print(jedi)

if esp_twi == 0:
    print("No hay jedies de especie twi'lek")

print()
# e) listar todos los Jedi que comienzan con A
print("Jedies que comienzan con A:")
jedies_con_a = 0  # contador para saber si existen jedies que comienzan con A
for jedi in lista_de_jedi:
    if jedi.nombre.startswith(('A', 'a')):
        jedies_con_a += 1
        print(jedi)

if jedies_con_a == 0:
    print("No hay jedies que comienzan con A")

print()
# f) mostrar los jedi que usaron sable de luz de más de un color
print("Jedi que usaron sable de luz de más de un color:")
# contador para saber si hay jedies que usaron sables de más de un color
más_de_un_color = 0
for jedi in lista_de_jedi:
    if len(jedi.colores_sable) > 1:
        más_de_un_color += 1
        print(jedi)

if más_de_un_color == 0:
    print("No hay jedies que usaron sable de luz de más de un color")
print()

# g) indicar los Jedi que utilizaron sable de luz amarillo o violeta.
print("Jedi que utilizaron sable de luz amarillo o violeta:")
ama_o_vio = 0  # contador para sabes si hay jedies que usaron sables de color amarillo  o violeta
for jedi in lista_de_jedi:
    colores = [c.lower() for c in jedi.colores_sable]
    if "amarillo" in colores or "violeta" in colores:
        ama_o_vio += 1
        print(jedi)

if ama_o_vio == 0:
    print("No hay jedies que utilizaron sable de luz amarillo o violeta")
print()
# h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
print("Padawans de Qui-Gon Jin y Mace Windu:")
index_qui_gon = lista_de_jedi.buscar("Qui-Gon Jin", "nombre")
index_mace = lista_de_jedi.buscar("Mace Windu", "nombre")
print()
if index_qui_gon is not None:
    qui_gon = lista_de_jedi[index_qui_gon]
    print(f"Padawans de Qui-Gon Jin:")
    for jedi in lista_de_jedi:
        if jedi.maestro == "Qui-Gon Jin":
            print(jedi.nombre)
else:
    print("Qui-Gon Jin no tuvo padawans")

if index_mace is not None:
    mace = lista_de_jedi[index_mace]
    print(f"Padawans de Mace Windu:")
    for jedi in lista_de_jedi:
        if jedi.maestro == "Mace Windu":
            print(jedi.nombre)
else:
    print("Mace Windu no tuvo padawans")
