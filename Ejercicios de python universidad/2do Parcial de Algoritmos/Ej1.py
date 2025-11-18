# Ejercicio 1: Se tiene los datos de Pokémons de las 9 generaciones cargados de manera aleatoria (1025 en total) de los cuales se conoce su nombre,
# número, tipo/tipos, debilidades frente a tipo/tipos, si tiene mega evolucion (bool) y si tiene forma gigamax (bool)
# para el cual debemos construir tres árboles para acceder de manera eficiente a los datos contemplando lo siguiente:
# los índices de cada uno de los árboles deben ser nombre, número y tipo;
#   a. mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
#   b. mostrar todos los nombres de los Pokémons de un determinado tipo: fantasma, fuego, acero y eléctrico;
#   c. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
#   d. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
#   e. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
#   f. determinar cuantos Pokémons tienen megaevolucion.
#   g. determinar cuantos Pokémons tiene forma gigamax.

from pokemones_data import pokemones
from tree import BinaryTree

# a y b : construcción de los árboles con clave en número, tipo y nombre.
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()
arbol_nombre = BinaryTree()


class Pokemon:
    def __init__(self, numero, nombre, tipos, debilidades, mega, gigamax):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos
        self.debilidades = debilidades
        self.mega = mega
        self.gigamax = gigamax

    def __str__(self):
        tipos_str = ", ".join(self.tipos)
        debilidades_str = ", ".join(self.debilidades)

        return (
            f"#{self.numero} — {self.nombre}\n"
            f"  • Tipo: {tipos_str}\n"
            f"  • Débil a: {debilidades_str}\n"
            f"  • Mega: {'Sí' if self.mega else 'No'}\n"
            f"  • Gigamax: {'Sí' if self.gigamax else 'No'}"
        )

    def resumen(self):
        return f"{self.nombre} (# {self.numero}) — Tipo: {', '.join(self.tipos)}"


def imprimir_arbol_tipos(arbol_tipo):
    def _in_order(root):
        if root is not None:
            _in_order(root.left)

            print(f"Tipo: {root.value}")
            for poke in root.other_values:
                print("   -", poke.resumen())
            print()

            _in_order(root.right)

    if arbol_tipo.root:
        _in_order(arbol_tipo.root)


pokemones_list = []
for p in pokemones:
    pokemon = Pokemon(
        numero=p['numero'],
        nombre=p['nombre'],
        tipos=p['tipos'],
        debilidades=p['debilidades'],
        mega=p['mega'],
        gigamax=p['gigamax']
    )
    pokemones_list.append(pokemon)


for poke in pokemones_list:
    # Árbol por número
    arbol_numero.insert(poke.numero, poke)

    # Árbol por nombre
    arbol_nombre.insert(poke.nombre, poke)

    # Árbol por tipo
    for tipo in poke.tipos:
        nodo_tipo = arbol_tipo.search(tipo)

        if nodo_tipo is None:
            # Si el tipo NO existe → lo creamos con una lista que contiene 1 Pokémon
            arbol_tipo.insert(tipo, [poke])
        else:
            # Si el tipo existe → agregamos el Pokémon a la lista
            nodo_tipo.other_values.append(poke)


# c. realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
print()
print("--------------------------------------------")
print("Listado ascendente por número (in-order):")
print("--------------------------------------------")
print()
arbol_numero.in_order()
print()

print()
print("--------------------------------------------")
print("Listado ascendente por nombre (in-order):")
print("--------------------------------------------")
print()
arbol_nombre.in_order()
print()

print()
print("--------------------------------------------")
print("Listado ordenado por nivel por nombre (by-level):")
print("--------------------------------------------")
print()
arbol_nombre.by_level()
print()
# a. mostrar todos los datos de un Pokémon a partir de su número y nombre
# –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul”
# se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–;
print()
print("--------------------------------------------")
busc = input("Ingrese el nombre o número del pokémon a buscar: ")
print("--------------------------------------------")
print()

# Si el input es un número, convertir a int
if busc.isdigit():
    busc_num = int(busc)
else:
    busc_num = None

# --- búsqueda por número ---
if busc_num is not None:
    nodo_num = arbol_numero.search(busc_num)
    if nodo_num:
        print("Datos del Pokémon encontrado por número:")
        print(nodo_num.other_values)
    else:
        print("No se encontró ningún Pokémon con ese número.")
else:
    print("No se ingresó un número, se salta búsqueda por número.")


# --- búsqueda por proximidad ---
resultado_prox = arbol_nombre.proximity_search(busc)

if resultado_prox:
    print("\nDatos de los Pokémons encontrados por nombre:")
    for nodo in resultado_prox:
        print(nodo.other_values)
else:
    print("\nNo se encontró ningún Pokémon con ese nombre o coincidencia.")


# b) búsqueda por tipo
print()
print("--------------------------------------------")
tipo_buscado = input(
    "Ingrese el tipo de Pokémon a buscar (ejemplo: fantasma, fuego, acero y eléctrico): ")
print("--------------------------------------------")
print()

tipo_buscado = tipo_buscado.capitalize()

nodo_tipo = arbol_tipo.search(tipo_buscado)

if nodo_tipo:
    print(f"Pokémons del tipo '{tipo_buscado}':")
    for poke in nodo_tipo.other_values:
        print(poke.resumen())
else:
    print(f"No se encontraron Pokémons del tipo '{tipo_buscado}'.")

# d. mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;

# 1. Buscar nodos
nodo_jol = arbol_nombre.search("Jolteon")
nodo_lyc = arbol_nombre.search("Lycanroc")
nodo_tyr = arbol_nombre.search("Tyrantrum")

# 2. Obtener objetos Pokémon
jolteon = nodo_jol.other_values
lycanroc = nodo_lyc.other_values
tyrantrum = nodo_tyr.other_values

# 3. Tipos de ataque (los tipos de estos Pokémon son sus ataques)
tipos_jol = jolteon.tipos
tipos_lyc = lycanroc.tipos
tipos_tyr = tyrantrum.tipos

# 4. Generar listas separadas
debiles_a_jol = []
debiles_a_lyc = []
debiles_a_tyr = []

# 5. Buscar pokémons que tengan debilidad a esos tipos
print()
for poke in pokemones_list:
    # Verificar si algún tipo de Jolteon está en las debilidades del pokémon
    for tipo in tipos_jol:
        if tipo in poke.debilidades:
            debiles_a_jol.append(poke)
            break  # Evitar duplicados

    # Verificar si algún tipo de Lycanroc está en las debilidades del pokémon
    for tipo in tipos_lyc:
        if tipo in poke.debilidades:
            debiles_a_lyc.append(poke)
            break

    # Verificar si algún tipo de Tyrantrum está en las debilidades del pokémon
    for tipo in tipos_tyr:
        if tipo in poke.debilidades:
            debiles_a_tyr.append(poke)
            break

print("--------------------------------------------")
print("Débiles frente a Jolteon:")
print("--------------------------------------------")

if debiles_a_jol:
    for poke in debiles_a_jol:
        print(" -", poke.resumen())
    print()
else:
    print("No se encontraron Pokémons débiles frente a Jolteon.")
    print()

print()
print("--------------------------------------------")
print("Débiles frente a Lycanroc:")
print("--------------------------------------------")
print()

if debiles_a_lyc:
    for poke in debiles_a_lyc:
        print(" -", poke.resumen())
    print()
else:
    print("No se encontraron Pokémons débiles frente a Lycanroc.")
    print()

print()
print("--------------------------------------------")
print("Débiles frente a Tyrantrum:")
print("--------------------------------------------")
print()

if debiles_a_tyr:
    for poke in debiles_a_tyr:
        print(" -", poke.resumen())
    print()
else:
    print("No se encontraron Pokémons débiles frente a Tyrantrum.")
    print()


# e. mostrar todos los tipos de Pokémons y cuántos hay de cada tipo;
print()
print("--------------------------------------------")
print("Tipos de Pókemon y cantidad:")
print("--------------------------------------------")
print()


def contar_por_tipo(root, tipos_dict):
    if root is not None:
        contar_por_tipo(root.left, tipos_dict)

        tipo = root.value
        cantidad = len(root.other_values)
        tipos_dict[tipo] = cantidad

        contar_por_tipo(root.right, tipos_dict)


tipos_dict = {}
contar_por_tipo(arbol_tipo.root, tipos_dict)

# Mostrar ordenado alfabéticamente
for tipo in sorted(tipos_dict.keys()):
    print(f"  • {tipo}: {tipos_dict[tipo]} Pokémon(s)")

print()
print(f"Total de tipos diferentes: {len(tipos_dict)}")
print()

# f. determinar cuantos Pokémons tienen megaevolucion.
print()
print("--------------------------------------------")
print("Pokemón con megaevolución:")
print("--------------------------------------------")
print()

mega_count = 0
for poke in pokemones_list:
    if poke.mega:
        mega_count += 1

print(f"Cantidad de Pokémon con Megaevolución: {mega_count}")
print()

# g. determinar cuantos Pokémons tiene forma gigamax.
print()
print("--------------------------------------------")
print("Pokemón con forma Gigamax:")
print("--------------------------------------------")
print()

gigamax_count = 0
for poke in pokemones_list:
    if poke.gigamax:
        gigamax_count += 1

print(f"Cantidad de Pokémon con forma Gigamax: {gigamax_count}")
print()
