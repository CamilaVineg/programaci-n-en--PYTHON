# 5. Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos nece-
# sarios para resolver las tareas, listadas a continuación:
# a. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servi-
# dor, router, switch, impresora;
# b. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook:
# Red Hat, Debian, Arch;
# c. encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro,
# Red Hat, Fedora hasta la impresora;
# d. encontrar el árbol de expansión mínima;
# e. determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”;
# f. indicar desde que computadora del switch 01 es el camino más corto
# al servidor “MongoDB”;
# g. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b;
# h. debe utilizar un grafo no dirigido.

from graph import Graph

equipitos = Graph(is_directed=False)

# -------------------------------------------------------------------------------------------------
# A. Cargando vertices y aristas con el nombre de equipo y su tipo ---------------------------------
# --------------------------------------------------------------------------------------------------

equipitos.insert_vertex('Red Hat', 'notebook')
equipitos.insert_vertex('Debian', 'notebook')
equipitos.insert_vertex('Arch', 'notebook')
equipitos.insert_vertex('Manjaro', 'pc')
equipitos.insert_vertex('Fedora', 'pc')
equipitos.insert_vertex('Ubuntu', 'pc')
equipitos.insert_vertex('Mint', 'pc')
equipitos.insert_vertex('Parrot', 'pc')
equipitos.insert_vertex('Guaraní', 'servidor')
equipitos.insert_vertex('MongoDB', 'servidor')
equipitos.insert_vertex('Router 01', 'router')
equipitos.insert_vertex('Router 02', 'router')
equipitos.insert_vertex('Router 03', 'router')
equipitos.insert_vertex('Switch 01', 'switch')
equipitos.insert_vertex('Switch 02', 'switch')
equipitos.insert_vertex('Impresora', 'impresora')

# Conexiones (aristas) según el gráfico (grafo no dirigido)
equipitos.insert_edge('Switch 01', 'Debian', 17)
equipitos.insert_edge('Switch 01', 'Ubuntu', 18)
equipitos.insert_edge('Switch 01', 'Impresora', 22)
equipitos.insert_edge('Switch 01', 'Mint', 80)
equipitos.insert_edge('Switch 01', 'Router 01', 29)

equipitos.insert_edge('Router 01', 'Router 02', 37)
equipitos.insert_edge('Router 01', 'Router 03', 43)
equipitos.insert_edge('Router 02', 'Router 03', 50)

equipitos.insert_edge('Router 02', 'Red Hat', 25)
equipitos.insert_edge('Router 02', 'Guaraní', 9)

equipitos.insert_edge('Router 03', 'Switch 02', 61)

equipitos.insert_edge('Switch 02', 'Manjaro', 40)
equipitos.insert_edge('Switch 02', 'Parrot', 12)
equipitos.insert_edge('Switch 02', 'Arch', 56)
equipitos.insert_edge('Switch 02', 'MongoDB', 5)
equipitos.insert_edge('Switch 02', 'Fedora', 3)

# -------------------------------------------------------------------------------------------------
# B. Barrido en profundidad y amplitud desde las notebooks -----------------------------------------
# --------------------------------------------------------------------------------------------------

print("-----------------------------------------")
print("-----------------------------------------")
print("BARRIDO EN PROFUNDIDAD")
print("-----------------------------------------")
print("-----------------------------------------")
print()

print("-----------------------------------------")
print("Barrido en profundidad desde Red Hat:")
print("-----------------------------------------")

equipitos.deep_sweep('Red Hat')
print()


print("-----------------------------------------")
print("Barrido en profundidad desde Debian:")
print("-----------------------------------------")

equipitos.deep_sweep('Debian')
print()


print("-----------------------------------------")
print("Barrido en profundidad desde Arch:")
print("-----------------------------------------")

equipitos.deep_sweep('Arch')
print()

print("-----------------------------------------")
print("-----------------------------------------")
print("BARRIDO EN AMPLITUD")
print("-----------------------------------------")
print("-----------------------------------------")
print()


print("-----------------------------------------")
print("Barrido en amplitud desde Red Hat:")
print("-----------------------------------------")

equipitos.amplitude_sweep('Red Hat')
print()

print("-----------------------------------------")
print("Barrido en amplitud desde Debian:")
print("-----------------------------------------")

equipitos.amplitude_sweep('Debian')
print()

print("-----------------------------------------")
print("Barrido en amplitud desde Arch:")
print("-----------------------------------------")

equipitos.amplitude_sweep('Arch')
print()

# -------------------------------------------------------------------------------------------------
# C. Encontrar el camino más corto desde Manjaro, Red Hat, Fedora hasta la impresora----------------
# -------------------------------------------------------------------------------------------------

print("-----------------------------------------")
print("-----------------------------------------")
print("CAMINO MÁS CORTO HASTA LA IMPRESORA")
print("-----------------------------------------")
print("-----------------------------------------")
print()

for pc in ['Manjaro', 'Red Hat', 'Fedora']:
    path_stack = equipitos.dijkstra(pc)

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

    # Reconstruir camino desde pc hasta 'Impresora'
    destination = 'Impresora'
    camino_a_destino = []

    if destination in distancias:
        # armar el camino usando los padres
        actual = destination
        while actual is not None:
            camino_a_destino.append(actual)
            actual = padres.get(actual)

        camino_a_destino.reverse()
        distancia_total = distancias[destination]

        print(f"Camino desde {pc} hasta {destination}:")
        print(f"  Distancia total: {distancia_total}")
        print(f"  Ruta: {' -> '.join(camino_a_destino)}")
    else:
        print(f"No hay camino desde {pc} hasta {destination}")

    print()

# -------------------------------------------------------------------------------------------------
# D. Encontrar el árbol de expansión mínima -------------------------------------------------------
# -------------------------------------------------------------------------------------------------

arbol_exp_minima = equipitos.kruskal('Red Hat')
print("-----------------------------------------")
print("-----------------------------------------")
print("ÁRBOL DE EXPANSIÓN MÍNIMA (Kruskal)")
print("-----------------------------------------")
print("-----------------------------------------")
print()

for arista in arbol_exp_minima.split(';'):
    origin, destination, weight = arista.split ('-')
    print(f"{origin} -- {destination} (costo: {weight})")
    
    
print()
# -------------------------------------------------------------------------------------------------
# E. Determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní” -----
# -------------------------------------------------------------------------------------------------

print("-----------------------------------------")
print("-----------------------------------------")
print("CAMINO MÁS CORTO HASTA EL SERVIDOR 'Guaraní' ")
print("-----------------------------------------")
print("-----------------------------------------")
print()

camino_menor = float('inf')
pc_menor = ''

for pc in ['Manjaro', 'Fedora', 'Ubuntu', 'Mint', 'Parrot']:
    path_stack = equipitos.dijkstra(pc)

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

    # Reconstruir camino desde pc hasta 'Guaraní'
    destination = 'Guaraní'
    camino_a_destino = []

    if destination in distancias:
        # armar el camino usando los padres
        actual = destination
        while actual is not None:
            camino_a_destino.append(actual)
            actual = padres.get(actual)

        camino_a_destino.reverse()
        distancia_total = distancias[destination]

        print(f"Camino desde {pc} hasta {destination}:")
        print(f"  Distancia total: {distancia_total}")
        print(f"  Ruta: {' -> '.join(camino_a_destino)}")

        # Actualizar si es menor
        if distancia_total < camino_menor:
            camino_menor = distancia_total
            pc_menor = pc
    else:
        print(f"No hay camino desde {pc} hasta {destination}")

    print()

print(
    f"La PC con el camino más corto hasta 'Guaraní' es {pc_menor} con una distancia de {camino_menor}")
print()

# -------------------------------------------------------------------------------------------------
# F. Indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”-----
# -------------------------------------------------------------------------------------------------
camino_menor2 = float('inf')
pc_menor2 = ''

for pc in ['Ubuntu', 'Mint', 'Debian']:
    path_stack = equipitos.dijkstra(pc)

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

    # Reconstruir camino desde pc hasta 'Guaraní'
    destination = 'MongoDB'
    camino_a_destino = []

    if destination in distancias:
        # armar el camino usando los padres
        actual = destination
        while actual is not None:
            camino_a_destino.append(actual)
            actual = padres.get(actual)

        camino_a_destino.reverse()
        distancia_total = distancias[destination]

        print(f"Camino desde {pc} hasta {destination}:")
        print(f"  Distancia total: {distancia_total}")
        print(f"  Ruta: {' -> '.join(camino_a_destino)}")

        # Actualizar si es menor
        if distancia_total < camino_menor2:
            camino_menor2 = distancia_total
            pc_menor2 = pc
    else:
        print(f"No hay camino desde {pc} hasta {destination}")

    print()

print(
    f"La PC con el camino más corto hasta 'MongoDB' es {pc_menor2} con una distancia de {camino_menor2}")
print()

# -------------------------------------------------------------------------------------------------
# G. Cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto b-----
# -------------------------------------------------------------------------------------------------
equipitos.delete_edge('Switch 01', 'Impresora')
equipitos.insert_edge('Router 02', 'Impresora', 15)
print("-----------------------------------------")
print("-----------------------------------------")
print("BARRIDO EN PROFUNDIDAD DESDE LA IMPRESORA (DESPUÉS DE CAMBIO DE CONEXIÓN)")
print("-----------------------------------------")
print("-----------------------------------------")
print()
equipitos.deep_sweep('Impresora')
print()


print("-----------------------------------------")
print("-----------------------------------------")
print("BARRIDO EN AMPLITUD DESDE LA IMPRESORA (DESPUÉS DE CAMBIO DE CONEXIÓN)")
print("-----------------------------------------")
print("-----------------------------------------")
print()
equipitos.amplitude_sweep('Impresora')
print()

