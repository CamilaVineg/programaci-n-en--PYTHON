# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.

from Queue_ import Cola

cola_superheroes = Cola()

superheroes = [
    {"personaje": "Tony Stark", "superheroe": "Iron Man", "genero": "M"},
    {"personaje": "Steve Rogers", "superheroe": "Capitán América", "genero": "M"},
    {"personaje": "Natasha Romanoff", "superheroe": "Black Widow", "genero": "F"},
    {"personaje": "Carol Danvers", "superheroe": "Capitana Marvel", "genero": "F"},
    {"personaje": "Scott Lang", "superheroe": "Ant-Man", "genero": "M"},
    {"personaje": "Stephen Strange", "superheroe": "Doctor Strange", "genero": "M"},
    {"personaje": "Shuri", "superheroe": "Shuri", "genero": "F"},
]

for super in superheroes:
    cola_superheroes.encolar(super)

# A)))


def nombre_capitanamarvel(cola_superheroes):
    cola_aux = Cola()
    aux = ""

    while not cola_superheroes.esta_vacia():
        super = cola_superheroes.desencolar()

        if super["superheroe"] == "Capitana Marvel":
            aux = super["personaje"]

        cola_aux.encolar(super)

    while not cola_aux.esta_vacia():
        cola_superheroes.encolar(cola_aux.desencolar())

    return aux

# B)))


def superheroes_femeninas(cola_superheroes):
    cola_aux = Cola()
    lista_aux = []

    while not cola_superheroes.esta_vacia():
        super = cola_superheroes.desencolar()

        if super["genero"] == "F":
            lista_aux.append(super["superheroe"])

        cola_aux.encolar(super)

    while not cola_aux.esta_vacia():
        cola_superheroes.encolar(cola_aux.desencolar())

    return lista_aux

# C)))


def superheroes_masculinos(cola_superheroes):
    cola_aux = Cola()
    lista_aux = []

    while not cola_superheroes.esta_vacia():
        super = cola_superheroes.desencolar()

        if super["genero"] == "M":
            lista_aux.append(super["personaje"])

        cola_aux.encolar(super)

    while not cola_aux.esta_vacia():
        cola_superheroes.encolar(cola_aux.desencolar())

    return lista_aux


def nombre_de_superheroe_ScottLang(cola_superheroes):
    cola_aux = Cola()

    while not cola_superheroes.esta_vacia():
        super = cola_superheroes.desencolar()

        if super["personaje"] == "Scott Lang":
            aux = super["superheroe"]

        cola_aux.encolar(super)

    while not cola_aux.esta_vacia():
        cola_superheroes.encolar(cola_aux.desencolar())

    return aux

# E)))


def superheroes_inicial_S(cola_superheroes):
    cola_aux = Cola()
    lista_aux = []

    while not cola_superheroes.esta_vacia():
        super = cola_superheroes.desencolar()
        pers = super["personaje"]
        heroe = super["superheroe"]

        if pers.startswith("S") or heroe.startswith("S"):
            lista_aux.append(super)

        cola_aux.encolar(super)

    while not cola_aux.esta_vacia():
        cola_superheroes.encolar(cola_aux.desencolar())

    return lista_aux

# F)))


def pregunta_esta_carolDanvers(cola_superheroes):
    cola_aux = Cola()
    heroenombre = ""

    while not cola_superheroes.esta_vacia():
        super = cola_superheroes.desencolar()

        if super["personaje"] == "Carol Danvers":
            heroenombre = super["superheroe"]

        cola_aux.encolar(super)

    while not cola_aux.esta_vacia():
        cola_superheroes.encolar(cola_aux.desencolar())

    return heroenombre


# programa principal.
# A)))
nombre_real_capitanaMarvel = nombre_capitanamarvel(cola_superheroes)
print(
    f"A) El nombre real de la superheroe Capitana Marvel es {nombre_real_capitanaMarvel}")

# B)))
lista_femeninas = superheroes_femeninas(cola_superheroes)
print("B) Lista de nombres de los superheroes femeninos:")
for fem in lista_femeninas:
    print(f"{fem}")

# C)))
lista_masculinos = superheroes_masculinos(cola_superheroes)
print("B) Lista de nombres de los superheroes masculinos:")
for masc in lista_masculinos:
    print(f"{masc}")

# D)))
nombre_superheroe_scottLang = nombre_de_superheroe_ScottLang(cola_superheroes)
print(
    f"C) El nombre de superheroe del personaje Scott Lang es {nombre_superheroe_scottLang}")

# E)))
heroes_inicial_S = superheroes_inicial_S(cola_superheroes)

print("E) Estos son los datos de todos los héroes con inicial S")
for heroe in heroes_inicial_S:
    print(f"{heroe}")

# F)))
heroe_caroldanvers = pregunta_esta_carolDanvers(cola_superheroes)

if not heroe_caroldanvers:
    print("Carol Denvers no se encuentra en la cola")
else:
    print(
        f"Carol Denvers se encuentra en la cola, su nombre de superheroe es {heroe_caroldanvers}")
