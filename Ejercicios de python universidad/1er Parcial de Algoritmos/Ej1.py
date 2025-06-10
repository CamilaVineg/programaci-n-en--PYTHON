# Ejercicio 1: Dado una lista simple de python (array) de 15 superheroes realizar dos funciones recursivas:
# funcion recursiva  para buscar, determinar si Capitan America esta en la lista.
# funcion recursiva para listar los superheroes de la lista.


# Buscando al Capitán America
def buscar_capitan_américa(lista_de_superheroes, indice=0):
    if indice >= len(lista_de_superheroes):
        return False
    if lista_de_superheroes[indice] == "Capitan America":
        return True
    return buscar_capitan_américa(lista_de_superheroes, indice + 1)

# Mostrando la lista


def enlistar_superheroes(lista_de_superheroes, indice=0):
    if indice >= len(lista_de_superheroes):
        return
    print(lista_de_superheroes[indice])
    enlistar_superheroes(lista_de_superheroes, indice + 1)


lista_de_superheroes = ["Capitán América", "Thor", "Spiderman", "Viuda Negra", "Hulk",
                        "Pantera Negra", "Dr Strange", "Deadpool", "Batman", "Superman",
                        "Linterna Verde", "Wolverine", "Flash", "Ant Man", "Mujer Maravilla"]

print("Lista de Superheroes:")
enlistar_superheroes(lista_de_superheroes)

print()
print("Buscando al héroe Capitán América en la lista...")
print("---")
if buscar_capitan_américa(lista_de_superheroes):
    print("El héroe Cápitan América se encuentra en la lista!🛡️")
else:
    print("El héroe Capitán América no se encuentra en la lista.❌🥀")
