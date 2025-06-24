# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from Stack_ import Stack

# A)))


def posicion_de_buscados(personajes_de_marvel):
    pila_aux = Stack()
    pos = 1
    posiciones = {}

    while not personajes_de_marvel.tamanio() > 0:
        pers = personajes_de_marvel.desapilar()
        if pers["nombre"] == "Rocket Raccoon":
            posiciones["Rocket Raccoon"] = pos
        elif pers["nombre"] == "Groot":
            posiciones["Groot"] = pos

        pila_aux.apilar(pers)
        pos += 1

    while not pila_aux.tamanio() > 0:
        personajes_de_marvel.apilar(pila_aux.desapilar())

    return posiciones

# B))))


def personajes_aparicion_mayor_a_5(personajes_de_marvel):
    pila_aux = Stack()
    personajes_mas_vistos = []

    while not personajes_de_marvel.tamanio() > 0:
        pers = personajes_de_marvel.desapilar()

        if pers["apariciones en películas"] > 5:
            personajes_mas_vistos.append(pers)

        pila_aux.apilar(pers)

    while not pila_aux.tamanio() > 0:
        personajes_de_marvel.apilar(pila_aux.desapilar())

    return personajes_mas_vistos

# C)))


def apariciones_viuda_negra(personajes_de_marvel):
    pila_aux = Stack()

    while not personajes_de_marvel.tamanio() > 0:

        pers = personajes_de_marvel.desapilar()

        if pers["nombre"] == "Black Widow":
            result = pers["apariciones en películas"]

        pila_aux.apilar(pers)

    while not pila_aux.tamanio() > 0:
        personajes_de_marvel.apilar(pila_aux.desapilar())

    return result

# D))))


def personajes_con_C_D_G(personajes_de_marvel):
    pila_aux = Stack()
    pers_C = []
    pers_D = []
    pers_G = []

    while not personajes_de_marvel.tamanio() > 0:

        pers = personajes_de_marvel.desapilar()
        nombre = pers["nombre"]

        if nombre.startswith("C"):
            pers_C.append(nombre)
        elif nombre.startswith("D"):
            pers_D.append(nombre)
        elif nombre.startswith("G"):
            pers_G.append(nombre)

        pila_aux.apilar(pers)

    while not pila_aux.tamanio() > 0:
        personajes_de_marvel.apilar(pila_aux.desapilar())

    return (pers_C, pers_D, pers_G)


# programa principal
personaje_1 = {"nombre": "Tony Stark",
               "apariciones en películas": 9}
personaje_2 = {"nombre": "Bruce Banner",
               "apariciones en películas": 9}
personaje_3 = {"nombre": "Capitán América",
               "apariciones en películas": 8}
personaje_4 = {"nombre": "Thor",
               "apariciones en películas": 8}
personaje_5 = {"nombre": "Groot",
               "apariciones en películas": 6}
personaje_6 = {"nombre": "Black Widow",
               "apariciones en películas": 9}
personaje_7 = {"nombre": "Rocket Raccoon",
               "apariciones en películas": 6}

personajes_de_marvel = Stack()
personajes_de_marvel.apilar(personaje_1)
personajes_de_marvel.apilar(personaje_2)
personajes_de_marvel.apilar(personaje_3)
personajes_de_marvel.apilar(personaje_4)
personajes_de_marvel.apilar(personaje_5)
personajes_de_marvel.apilar(personaje_6)
personajes_de_marvel.apilar(personaje_7)

# A)))

posiciones = posicion_de_buscados(personajes_de_marvel)


print("personajes buscados y sus posiciones:")
for nombre, posicion in posiciones.items():
    print(f"- {nombre} está en la posición {posicion}")

# B)))
mas_vistos = personajes_aparicion_mayor_a_5(personajes_de_marvel)
print("Lista de personajes con apariciones mayor a 5 y su total de apariciones actual:")
for personaje in mas_vistos:
    print(f"- {personaje}")

# C)))
cant_apariciones_blackwidow = apariciones_viuda_negra(personajes_de_marvel)

if cant_apariciones_blackwidow == 0:
    print("Black Widow no tuvo ninguna aparicion o no se encuentra entre las wikis")
else:
    print(f"Black Widow tuvo {cant_apariciones_blackwidow} apariciones")

# D))))
c, d, g = personajes_con_C_D_G(personajes_de_marvel)

print("Personajes que empiezan con C:")
if not c:
    print("No hay personajes con inicial C")
else:
    for nombre in c:
        print(f"- {nombre}")

print("Personajes que empiezan con D:")
if not d:
    print("No hay personajes con inicial D")
else:
    for nombre in d:
        print(f"- {nombre}")

print("Personajes que empiezan con G:")
if not g:
    print("No hay personajes con inicial G")
else:
    for nombre in g:
        print(f"- {nombre}")
