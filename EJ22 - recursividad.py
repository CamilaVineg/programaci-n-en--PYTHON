# 22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste)
# está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada
# “usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
# a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
# b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
# c. Utilizar un vector para representar la mochila.#

def usar_la_fuerza(mochila, objetos_sacados=0):
    if not mochila:
        # No hay más objetos y no encontramos sable
        return (False, objetos_sacados)

    objeto_actual = mochila[0]
    objetos_sacados += 1

    if objeto_actual == "sable de luz":  # Punto b)
        return (True, objetos_sacados)  # Encontramos el sable

    # Si no es el sable, seguimos.
    return usar_la_fuerza(mochila[1:], objetos_sacados)  # Punto a)


# defino la mochila como una lista
mochila = ["agua", "abrigo", "comida", "sable de luz", "linterna"]  # Punto c)

# Llamamos a la función
encontro_sable, objetos_sacados = usar_la_fuerza(mochila)

# Imprimimos los resultados
if encontro_sable:
    print(
        f"¡Encontramos el sable de luz! Sacamos {objetos_sacados} objetos para encontrarlo.")
else:
    print("No encontramos el sable de luz en la mochila.")
