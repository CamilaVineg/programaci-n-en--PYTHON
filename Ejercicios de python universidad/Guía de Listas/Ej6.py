# 6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre,
# año aparición,casa de comic a la que pertenece (Marvel o DC)
# y biografía, implementar la funciones necesarias para poder
# realizar las siguientes actividades:

# a. eliminar el nodo que contiene la información de Linterna Verde;
# b. mostrar el año de aparición de Wolverine;
# c. cambiar la casa de Dr. Strange a Marvel;
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
# “traje” o “armadura”;
# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
# sea anterior a 1963;
# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
# g. mostrar toda la información de Flash y Star-Lord;
# h. listar los superhéroes que comienzan con la letra B, M y S;
# i. determinar cuántos superhéroes hay de cada casa de comic.

from List import List


class Superhero:

    def __init__(self, name, real_name, short_bio, first_appearance, comic_home):
        self.name = name
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.comic_home = comic_home

    def __str__(self):
        return f"- 'Nombre': {self.name}, 'nombre real': {self.real_name}, 'casa de comic': {self.comic_home}, 'primera aparicion': {self.first_appearance}, 'biografia':{self.short_bio}"


def ordenar_por_nombre(item):
    return item.name


lista_de_superheroes = List()

superheroes = [
    Superhero(
        name="Batman",
        real_name="Bruce Wayne",
        short_bio="Millonario, detective, usa traje y gadgets avanzados para combatir el crimen.",
        first_appearance="1939",
        comic_home="DC"
    ),
    Superhero(
        name="Nightwing",
        real_name="Dick Grayson",
        short_bio="Ex-Robin, protector de Blüdhaven, experto acróbata y luchador.",
        first_appearance="1984",
        comic_home="DC"
    ),
    Superhero(
        name="Superman",
        real_name="Clark Kent",
        short_bio="Último hijo de Krypton, posee super fuerza, visión láser y puede volar.",
        first_appearance="1938",
        comic_home="DC"
    ),
    Superhero(
        name="Harley Quinn",
        real_name="Harleen Quinzel",
        short_bio="Psiquiatra convertida en villana, compañera del Joker, experta en armas.",
        first_appearance="1992",
        comic_home="DC"
    ),
    Superhero(
        name="Iron Man",
        real_name="Tony Stark",
        short_bio="Genio multimillonario, usa una armadura tecnológica para combatir el crimen.",
        first_appearance="1963",
        comic_home="Marvel"
    ),
    Superhero(
        name="Wolverine",
        real_name="Logan",
        short_bio="Mutante con garras retráctiles, factor curativo y esqueleto de adamantium.",
        first_appearance="1974",
        comic_home="Marvel"
    ),
    Superhero(
        name="Linterna Verde",
        real_name="Hal Jordan",
        short_bio="Miembro de los Green Lantern Corps, usa un anillo de poder para crear objetos.",
        first_appearance="1959",
        comic_home="DC"
    ),
    Superhero(
        name="Flash",
        real_name="Barry Allen",
        short_bio="El hombre más rápido del mundo, puede viajar en el tiempo y entre dimensiones.",
        first_appearance="1956",
        comic_home="DC"
    ),
    Superhero(
        name="Dr. Strange",
        real_name="Stephen Strange",
        short_bio="Hechicero Supremo, maestro de las artes místicas y defensor de la Tierra.",
        first_appearance="1963",
        comic_home="DC"
    ),
    Superhero(
        name="Capitana Marvel",
        real_name="Carol Danvers",
        short_bio="Piloto de la Fuerza Aérea, poderes cósmicos, superfuerza y vuelo.",
        first_appearance="1968",
        comic_home="Marvel"
    ),
    Superhero(
        name="Mujer Maravilla",
        real_name="Diana Prince",
        short_bio="Princesa amazona, posee fuerza sobrehumana, lazo de la verdad y brazaletes mágicos.",
        first_appearance="1941",
        comic_home="DC"
    ),
    Superhero(
        name="Star-Lord",
        real_name="Peter Quill",
        short_bio="Líder de los Guardianes de la Galaxia, experto en combate y armas, usa casco y traje espacial.",
        first_appearance="1976",
        comic_home="Marvel"
    ),
]

for hero in superheroes:
    lista_de_superheroes.append(hero)


lista_de_superheroes.agregar_criterio('name', ordenar_por_nombre)

lista_de_superheroes.ordenar_por_criterio('name')

print("Lista de superheroes:")
lista_de_superheroes.mostrar()
print()


# a) Eliminar el nodo que contiene la informacion de Linterna Verde
lista_de_superheroes.eliminar_elemento("Linterna Verde", "name")
print("a) Lista sin Linterna Verde:")
lista_de_superheroes.mostrar()
print()
# b) Mostrar el año de aparicion de Wolverine
index_wolverine = lista_de_superheroes.buscar("Wolverine", "name")
if index_wolverine is not None:
    wolverine = lista_de_superheroes[index_wolverine]
    print(f"b) Año de aparicion de Wolverin {wolverine.first_appearance}")
else:
    print("Wolverine no se encuentra en la lista")

print()
# c) Cambiar la casa de Dr. Strange a Marvel

index_strange = lista_de_superheroes.buscar("Dr. Strange", "name")
if index_strange is not None:
    strange = lista_de_superheroes[index_strange]
    strange.comic_home = "Marvel"
    print("c) Casa de Dr. Strange cambiada a Marvel")
    print(strange)
else:
    print("Dr. Strange no se encuentra en la lista")
print()

# d) Mostrar el nombre de aquellos superheroes que en su biografia menciona la palabra "traje" o "armadura"

print("d) Superheroes que mencionan 'traje' o 'armadura' en su biografia:")
cont_cumple = 0
for hero in lista_de_superheroes:
    if "traje" in hero.short_bio.lower() or "armadura" in hero.short_bio.lower():
        cont_cumple += 1
        print(hero.name)

if cont_cumple == 0:
    print("No hay superheroes que mencionen 'traje' o 'armadura' en su biografia")

print()

# e) Mostrar el nombre y la casa de los superheroes cuya fecha de aparicion sea anterior a 1963
print("e) Superheroes con fecha de aparicion anterior a 1963:")
cont_cumple_2 = 0
for hero in lista_de_superheroes:
    if int(hero.first_appearance) < 1963:
        cont_cumple_2 += 1
        print(f"{hero.name} - {hero.comic_home}")

if cont_cumple_2 == 0:
    print("No hay superheroes con fecha de aparicion anterior a 1963")

print()
# f) Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
print("f) Casa de Capitana Marvel y Mujer Maravilla:")

for hero_name in ["Capitana Marvel", "Mujer Maravilla"]:
    index_hero = lista_de_superheroes.buscar(hero_name, "name")
    if index_hero is not None:
        hero = lista_de_superheroes[index_hero]
        print(f"{hero.name} pertenece a {hero.comic_home}")
    else:
        print(f"{hero_name} no se encuentra en la lista")

print()

# g) Mostrar toda la informacion de Flash y Star-Lord
print("g) Información de Flash y Star-Lord:")
for hero_name in ["Flash", "Star-Lord"]:
    index_hero = lista_de_superheroes.buscar(hero_name, "name")
    if index_hero is not None:
        hero = lista_de_superheroes[index_hero]
        print(f"{hero}")
    else:
        print(f"{hero_name} no se encuentra en la lista")

print()

# h. listar los superhéroes que comienzan con la letra B, M y S;

print("h) Superheroes que comienzan con B, M y S:")
cont_existen = 0
for hero in lista_de_superheroes:
    if hero.name.startswith(('B', 'M', 'S')):
        cont_existen += 1
        print(hero.name)

if cont_existen == 0:
    print("No hay superheroes que comiencen con B, M o S")

print()
# i. determinar cuántos superhéroes hay de cada casa de comic.
print("i) Cantidad de superheroes por casa de comic:")
contador_dc = 0
contador_marvel = 0

for hero in lista_de_superheroes:
    if hero.comic_home == "DC":
        contador_dc += 1
    elif hero.comic_home == "Marvel":
        contador_marvel += 1

if contador_dc == 0 and contador_marvel == 0:
    print("No hay superheroes en la lista")
elif contador_dc == 0:
    print("No hay superheroes de DC en la lista")
    print(f"En la lista hay {contador_marvel} superheroes de Marvel")
elif contador_marvel == 0:
    print("No hay superheroes de Marvel en la lista")
    print(f"En la lista hay {contador_dc} superheroes de DC")
else:
    print("En la lista hay:")
    print(f"{contador_dc} superheroes de DC")
    print(f"{contador_marvel} superheroes de Marvel")
