# Ejercicio 2: Dada una lista de personajes de marvel (la desarrollada en clases) debe tener 100 o mas, resolver:
# A)) Listado ordenado de manera ascendente por nombre de los personajes.
# B)) Determinar en que posicion esta The Thing y Rocket Raccoon.
# C)) Listar todos los villanos de la lista.
# D)) Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
# E)) Listar los superheores que comienzan con  Bl, G, My, y W.
# F)) Listado de personajes ordenado por nombre real de manera ascendente de los personajes.
# G)) Listado de superheroes ordenados por fecha de aparación.
# H)) Modificar el nombre real de Ant Man a Scott Lang.
# I)) Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.
# J)) Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

from List import List
from Queue_ import Cola
from super_heroes_data import superheroes


def order_by_name(item):
    return item.name


def order_by_real_name(item):
    return item.real_name if item.real_name is not None else ""


def order_by_first_appearance(item):
    return item.first_appearance

# Encolando a los villanos en una cola


def encolando_villanos(lista_de_superheroes):
    cola = Cola()
    for hero in lista_de_superheroes:
        if hero.is_villain:
            cola.encolar(hero)
    return cola


def determinando_villanos_antes_de_1980(cola_de_villanos):
    villanos_antes = List()
    aux = Cola()
    while cola_de_villanos.tamanio() > 0:
        villano = cola_de_villanos.desencolar()
        if villano.first_appearance < 1980:
            villanos_antes.append(villano)
        aux.encolar(villano)
    while not aux.tamanio() > 0:
        cola_de_villanos.encolar(aux.desencolar())
    return villanos_antes


# Creando el objeto Superhero para cada superheroe


class Superhero:

    def __init__(self, name, alias, real_name, short_bio, first_appearance, is_villain):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return f"{self.name}, {self.real_name}, {self.first_appearance} - {self.is_villain}"


# creando la lista de superheroes
lista_de_superheroes = List()
# creando la cola de villanos
cola_de_villanos = Cola()
# lista de los villanos que aparecieron antes de 1980
villanos_antes_de_1980 = List()
# Cargando la lista de superheroes

# Criterios
lista_de_superheroes.agregar_criterio(
    'name', order_by_name)
lista_de_superheroes.agregar_criterio('real_name', order_by_real_name)
lista_de_superheroes.agregar_criterio(
    'first_appearance', order_by_first_appearance)

for superheroe in superheroes:
    hero = Superhero(
        name=superheroe["name"],
        alias=superheroe["alias"],
        real_name=superheroe["real_name"],
        short_bio=superheroe["short_bio"],
        first_appearance=superheroe["first_appearance"],
        is_villain=superheroe["is_villain"],
    )
    lista_de_superheroes.append(hero)


lista_de_superheroes.ordenar_por_criterio('name')

# A)) Lista ordenada de manera ascendente por nombre de los personajes.
print("Esta es la lista de superheroes ordenada por nombre:")
lista_de_superheroes.mostrar()

# B)) Determinando en que posicion está the thing y rocket racoon.
print("---")
print("Posición de The Thing y Rocket Raccoon en la lista:")
result = lista_de_superheroes.buscar("The Thing", 'name')
if result is not None:
    print(f"The Thing está en la posición {result}")
else:
    print("The Thing no está en la lista")


result = lista_de_superheroes.buscar("Rocket Raccoon", 'name')
if result:
    print(f"Rocket Raccoon está en la posición {result}")
else:
    print("Rocket Raccoon no está en la lista")

# C) listando a todos los villanos de la lista.
print("---")
print("Esta es la lista de villanos:")
for hero in lista_de_superheroes:
    if hero.is_villain:
        print(
            f"Villano: {hero.name}, Alias: {hero.alias}, Nombre real: {hero.real_name}")

# D) Encolando a los villanos en una cola y determinando los que aparecieron antes de 1980.
print("---")
cola_de_villanos = encolando_villanos(lista_de_superheroes)
print("Villanos en la cola:")
cola_de_villanos.mostrar()
print()
print("Villanos que aparecieron antes de 1980:")
villanos_antes_de_1980 = determinando_villanos_antes_de_1980(cola_de_villanos)
if villanos_antes_de_1980:
    villanos_antes_de_1980.mostrar()
else:
    print("No hay villanos que hayan aparecido antes de 1980.")


# E)) Listado de los superheroes que comienzan con BL, G, My y W
print("---")
print("Listado de superhéroes que comienzan con Bl, G, My, y W:")
for superhero in lista_de_superheroes:
    if superhero.name.startswith(('Bl', 'G', 'My', 'W')):
        print(superhero)

# F) Listado de personajes ordenado por nombre real de manera ascendente.


print("---")
print("Este es el listado de personajes ordenado por nombre real:")
lista_de_superheroes.ordenar_por_criterio('real_name')
lista_de_superheroes.mostrar()

# G) Listado de superheroes ordenados por fecha de aparición.


print("---")
print("Este es el listado de personajes ordenado por año de aparición:")
lista_de_superheroes.ordenar_por_criterio('first_appearance')
lista_de_superheroes.mostrar()

# H) Modificando el nombre real de Ant
index = lista_de_superheroes.buscar('Ant Man', 'name')
if index:
    print(
        f"Nombre real de Ant antes de la modificación: {lista_de_superheroes[index].real_name}")
    lista_de_superheroes[index].real_name = 'Scott Lang'
    print(
        f"Nombre real de Ant después de la modificación: {lista_de_superheroes[index].real_name}")
else:
    print('el superheroe no esta en la lista')

# I) Mostrando los personajes que en su biografía incluyan la palabra time-traveling o suit.
print("---")
print("Personajes que en su biografía incluyen 'time-traveling' o 'suit':")
for superhero in lista_de_superheroes:
    if 'time-traveling' in superhero.short_bio or 'suit' in superhero.short_bio:
        print(superhero)

# J) Eliminando a Electro y Baron Zemo de la lista y mostrando su información si estaba en la lista.
print("---")
electro_index = lista_de_superheroes.eliminar_elemento('Electro', 'name')
if electro_index is not None:
    print(f"Se ha eliminado a Electro correctamente")
else:
    print("Electro no estaba en la lista")

baron_zemo_index = lista_de_superheroes.eliminar_elemento('Baron Zemo', 'name')
if baron_zemo_index is not None:
    print(f"Se ha eliminado a Baron Zemo de la lista correctamente.")
else:
    print("Baron Zemo no estaba en la lista")

print("Lista actualizada")
lista_de_superheroes.mostrar()
