# Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver las siguientes actividades:
# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
# además mostrar el nombre de dichas películas;
# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
# c. eliminar los modelos de los trajes destruidos mostrando su nombre;
# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
# más de un modelo de traje, estos deben cargarse por separado;
# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
# repetidos en una misma película;
# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
# “Capitan America: Civil War”.

from Stack_ import Stack

# A)))


def modelo_utilizado(trajes_de_ironman):
    peliculas_con_Hulkbuster = []
    pila_aux = Stack()

    while trajes_de_ironman.tamanio() > 0:
        traje = trajes_de_ironman.desapilar()
        if traje["modelo"] == "Mark XLIV":
            peliculas_con_Hulkbuster.append(traje["pelicula"])
        pila_aux.apilar(traje)

    while pila_aux.tamanio() > 0:
        trajes_de_ironman.apilar(pila_aux.desapilar())

    return peliculas_con_Hulkbuster

# B)))


def trajes_dañados(trajes_de_ironman):
    pila_aux = Stack()
    modelos_dañados = []
    while trajes_de_ironman.tamanio() > 0:
        traje = trajes_de_ironman.ver_tope()
        if traje["estado"] == "Dañado":
            modelos_dañados.append(traje["modelo"])
        traje = trajes_de_ironman.desapilar()
        pila_aux.apilar(traje)

    while pila_aux.tamanio() > 0:
        trajes_de_ironman.apilar(pila_aux.desapilar())

    return modelos_dañados

# C)))


def eliminar_trajes_destruidos(trajes_de_ironman):
    pila_aux = Stack()
    while trajes_de_ironman.tamanio() > 0:
        traje = trajes_de_ironman.desapilar()
        if traje["estado"] == "Destruido":
            print(f"modelo eliminado: {traje['modelo']}")
        else:
            pila_aux.apilar(traje)

    while pila_aux.tamanio() > 0:
        trajes_de_ironman.apilar(pila_aux.desapilar())

    return trajes_de_ironman

# E)))


def determinando_existencia_modelo(trajes_de_ironman):
    pila_aux = Stack()
    existe = False

    while trajes_de_ironman.tamanio() > 0:
        traje = trajes_de_ironman.desapilar()
        if traje["modelo"] == "Mark LXXXV" and traje["pelicula"] == "Avengers: Endgame":
            existe = True
        pila_aux.apilar(traje)

    while pila_aux.tamanio() > 0:
        trajes_de_ironman.apilar(pila_aux.desapilar())

    return existe


def agregando_traje(trajes_de_ironman, existe):
    if existe:
        print("La wiki ya existe")
    else:
        trajes_de_ironman.apilar({
            "modelo": "Mark LXXXV",
            "pelicula": "Avengers: Endgame",
            "estado": "Impecable"
        })
        print("Ya se ha agregado la wiki del modelo Mark LXXXV")
    return trajes_de_ironman

# F)))


def mostrar_trajes_spiderman_civilwar(trajes_de_ironman):
    pila_aux = Stack()
    trajes_usados = []

    while trajes_de_ironman.tamanio() > 0:
        traje = trajes_de_ironman.desapilar()
        if traje["pelicula"] == "Spider-Man: Homecoming" or traje["pelicula"] == "Capitán América: Civil War":
            trajes_usados.append(traje)
        pila_aux.apilar(traje)

    while pila_aux.tamanio() > 0:
        trajes_de_ironman.apilar(pila_aux.desapilar())
    return trajes_usados

# PROGRAMA PRINCIPAL


trajes_de_ironman = Stack()

trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Impecable"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark XLIII", "pelicula": "El increible Hulk", "estado": "Dañado"},
    {"modelo": "Mark XLIV", "pelicula": "El increible Hulk", "estado": "Dañado"},
    {"modelo": "Mark XLVI", "pelicula": "Capitán América: Civil War",
        "estado": "Impecable"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Impecable"}
]

for traje in trajes:
    trajes_de_ironman.apilar(traje)

# A)))
peliculas_con_Hulkbuster = modelo_utilizado(trajes_de_ironman)
print("Películas donde se usó el Hulkbuster (Mark XLIV):")
for peli in peliculas_con_Hulkbuster:
    print(f"- {peli}")

# B)))
modelos_dañados = trajes_dañados(trajes_de_ironman)
print("\nModelos que quedaron dañados:")
for modelo in modelos_dañados:
    print(f"- {modelo}")

# C)))
trajes_de_ironman = eliminar_trajes_destruidos(trajes_de_ironman)

# E)))
existe = determinando_existencia_modelo(trajes_de_ironman)
trajes_de_ironman = agregando_traje(trajes_de_ironman, existe)

# F)))
trajes_usados = mostrar_trajes_spiderman_civilwar(trajes_de_ironman)
print("\nModelos usados en Spider-Man: Homecoming y Capitán América: Civil War:")
for traje in trajes_usados:
    print(f"- {traje['modelo']} ({traje['pelicula']})")
