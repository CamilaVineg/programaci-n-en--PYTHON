# 14. Implementar sobre un grafo no dirigido los algoritmos necesarios para dar solución a las si-
# guientes tareas:

# a. cada vértice representa un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.

from graph import Graph
casita = Graph(is_directed=False)
# ---------------------------------------------------------------------------------------------
# a. cada vértice representa un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio
# ---------------------------------------------------------------------------------------------

# Cargando los vértices
casita.insert_vertex("cocina")
casita.insert_vertex("comedor")
casita.insert_vertex("cochera")
casita.insert_vertex("quincho")
casita.insert_vertex("baño 1")
casita.insert_vertex("baño 2")
casita.insert_vertex("habitación 1")
casita.insert_vertex("habitación 2")
casita.insert_vertex("sala de estar")
casita.insert_vertex("terraza")
casita.insert_vertex("patio")


# -------------------------------------------------------------------------------------------------------
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;
# --------------------------------------------------------------------------------------------------------

# Cargando las aristas con sus respectivos pesos (distancia en metros)

# Cocina.
casita.insert_edge("cocina", "comedor", 5)
casita.insert_edge("cocina", "patio", 7)
casita.insert_edge("cocina", "baño 1", 4)

# Comedor. (5 aristas)
casita.insert_edge("comedor", "sala de estar", 6)
casita.insert_edge("comedor", "terraza", 8)
casita.insert_edge("comedor", "quincho", 10)
casita.insert_edge("comedor", "cocina", 5)
casita.insert_edge("comedor", "patio", 9)

# Cochera.
casita.insert_edge("cochera", "patio", 12)
casita.insert_edge("cochera", "habitación 2", 15)
casita.insert_edge("cochera", "baño 2", 9)

# Quincho.
casita.insert_edge("quincho", "terraza", 5)
casita.insert_edge("quincho", "patio", 11)
casita.insert_edge("quincho", "habitación 2", 14)

# Baño 1.
casita.insert_edge("baño 1", "habitación 1", 6)
casita.insert_edge("baño 1", "sala de estar", 10)
casita.insert_edge("baño 1", "cocina", 4)

# Baño 2.
casita.insert_edge("baño 2", "habitación 2", 4)
casita.insert_edge("baño 2", "habitación 1", 7)
casita.insert_edge("baño 2", "cochera", 9)

# Terraza.
casita.insert_edge("terraza", "sala de estar", 3)
casita.insert_edge("terraza", "comedor", 8)
casita.insert_edge("terraza", "quincho", 5)

# Sala de estar.
casita.insert_edge("sala de estar", "terraza", 3)
casita.insert_edge("sala de estar", "patio", 8)
casita.insert_edge("sala de estar", "comedor", 6)

# Habitación 1. (5 aristas)
casita.insert_edge("habitación 1", "habitación 2", 5)
casita.insert_edge("habitación 1", "baño 1", 6)
casita.insert_edge("habitación 1", "baño 2", 7)
casita.insert_edge("habitación 1", "cochera", 9)
casita.insert_edge("habitación 1", "terraza", 10)

# Habitación 2.
casita.insert_edge("habitación 2", "habitación 1", 5)
casita.insert_edge("habitación 2", "baño 2", 4)
casita.insert_edge("habitación 2", "cochera", 15)

# Patio.
casita.insert_edge("patio", "cocina", 7)
casita.insert_edge("patio", "comedor", 9)
casita.insert_edge("patio", "sala de estar", 8)

# -------------------------------------------------------------------------------------------------------
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# --------------------------------------------------------------------------------------------------------

# Arbol de expansión mínima usando el algoritmo de Kruskal
arbol_exp_minima = casita.kruskal("cocina")
total_cableado = 0

print("-----------------------------------------")
print("-----------------------------------------")
print("ÁRBOL DE EXPANSIÓN MÍNIMA (Kruskal)")
print("-----------------------------------------")
print("-----------------------------------------")
print()

for arista in arbol_exp_minima.split(';'):
    origin, destination, weight = arista.split('-')
    print(f"{origin} -- {destination} (costo: {weight})")
    total_cableado += int(weight)

print("-----------------------------------------")
print(
    f"Total de metros de cable necesarios para conectar todos los ambientes: {total_cableado} metros")
print("-----------------------------------------")
print()


# -------------------------------------------------------------------------------------------------------
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
# # --------------------------------------------------------------------------------------------------------

path_stack = casita.dijkstra("habitación 1")

# Extraer información del Stack (dijkstra devuelve un Stack con [nombre, distancia, padre])
distancias = {}
padres = {}

# Vaciar el stack para obtener los datos
while path_stack.tamanio() > 0:
    item = path_stack.desapilar()
    nodo_nombre = item[0]
    distancia = item[1]
    padre = item[2]
    distancias[nodo_nombre] = distancia
    padres[nodo_nombre] = padre

    destination = 'sala de estar'
    camino_a_destino = []

if destination in distancias:
    # armar el camino usando los padres
    actual = destination
    while actual is not None:
        camino_a_destino.append(actual)
        actual = padres.get(actual)

    camino_a_destino.reverse()
    distancia_total = distancias[destination]

    print(f"Camino desde habitación 1 hasta {destination}:")
    print(f"  Metros de cable necesitados: {distancia_total}")
    print(f"  Ruta: {' -> '.join(camino_a_destino)}")
else:
    print(f"No hay camino desde habitación 1 hasta {destination}")

print()
