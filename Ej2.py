# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos
# necesarios para resolver las siguientes tareas:
#   a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
#   b. hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
#   c. determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
#   d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
#   f. calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
#   g. indicar qué personajes aparecieron en los nueve episodios de la saga.

from inspect import stack
from graph import Graph
from starwars_data import personajes, apariciones

# a. construccion del grafo.
grafo = Graph(is_directed=False)

for personaje in personajes: 
    grafo.insert_vertex(personaje)

# Función para contar episodios en común entre dos personajes
def contar_episodios_comunes(personaje1, personaje2, apariciones):
    """
    Cuenta cuántos episodios tienen en común dos personajes.
    
    Argumentos:
        personaje1: nombre del primer personaje
        personaje2: nombre del segundo personaje
        apariciones: diccionario {personaje: [lista de episodios]}
    
    Returns:
        cantidad de episodios en común
    """
    # Obtener los episodios de cada personaje
    episodios_p1 = set(apariciones.get(personaje1, []))
    episodios_p2 = set(apariciones.get(personaje2, []))
    
    # Calcular la intersección (episodios en común)
    episodios_comunes = episodios_p1.intersection(episodios_p2)
    
    return len(episodios_comunes)

# Insertar aristas entre personajes que aparecieron juntos
for i in range(len(personajes)):
    for j in range(i + 1, len(personajes)):
        personaje1 = personajes[i]
        personaje2 = personajes[j]
        
        # Contar episodios en común
        episodios_comunes = contar_episodios_comunes(personaje1, personaje2, apariciones)
        
        # Si tienen al menos un episodio en común, insertar arista
        if episodios_comunes > 0:
            grafo.insert_edge(personaje1, personaje2, episodios_comunes)

print("Grafo construido correctamente.")
print(f"Vértices: {len(personajes)}")


# b. hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
print()
print("---------------------------------")
print("Árbol de expansión minimo usando Kruskal")
print("---------------------------------")

personajes_aem = ["C-3PO", "Yoda", "Leia"]

for personaje in personajes_aem:
    print()
    print(f"--- Árbol de expansión mínimo desde {personaje} ---")
    print()
    
    arbol = grafo.kruskal(personaje)
    
    if arbol:
        print("Aristas del árbol de expansión mínimo:")
        
        aristas = arbol.split(';')
        peso_total = 0
        
        for arista in aristas:
            partes = arista.split('-')
            if len(partes) == 3:
                origen, destino, peso = partes
                print(f"{origen} -- {destino} (Episodios compartidos: {peso})")
                peso_total += int(peso)
        

        print("---------------------------------")
        print(f"Peso total del árbol: {peso_total} (episodios)")
        print(f"Aristas totales: {len(aristas)}")
        print("---------------------------------")
    else:
        print(f"No se pudo generar el árbol desde {personaje}")

# c. determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número
print()
print("---------------------------------")
print("Máximo de episodios compartidos entre dos personajes")
print("---------------------------------")

max_episodios = 0
pares_maximos = []

# Recorrer todas las aristas del grafo para encontrar el máximo
for i in range(len(personajes)):
    for j in range(i + 1, len(personajes)):
        personaje1 = personajes[i]
        personaje2 = personajes[j]
        
        episodios_comunes = contar_episodios_comunes(personaje1, personaje2, apariciones)
        
        if episodios_comunes > 0:
            if episodios_comunes > max_episodios:
                max_episodios = episodios_comunes
                pares_maximos = [(personaje1, personaje2)]
            elif episodios_comunes == max_episodios:
                pares_maximos.append((personaje1, personaje2))

print(f"\nNúmero máximo de episodios compartidos: {max_episodios}")
print(f"Pares de personajes que comparten {max_episodios} episodios:")

for personaje1, personaje2 in pares_maximos:
    print(f"  • {personaje1} y {personaje2}")
print("---------------------------------")


def mostrar_camino_mas_corto_entre_personajes(grafo, origen, destino):
    """
    Calcula y muestra cuál es el camino más corto entre dos personajes en el grafo.
    """
    print("----------------")
    print(f"Camino mas corto desde: {origen} hasta {destino}")
    
    path = grafo.dijkstra(origen)
    
    nodos_info = {}
    while path.tamanio() > 0:
        nodo = path.desapilar()
        nodos_info[nodo[0]] = {'costo': nodo[1], 'predecesor': nodo[2]}
    
    if destino not in nodos_info:
        print(f"\nNo se encontró un camino entre {origen} y {destino}")
        return None, None
    
    camino_realizado = []
    nodo_actual = destino
    peso_total = nodos_info[destino]['costo']
    
    while nodo_actual is not None:
        camino_realizado.append(nodo_actual)
        nodo_actual = nodos_info[nodo_actual]['predecesor']
    
    camino_realizado.reverse()
    
    if camino_realizado and camino_realizado[0] == origen:
        print(f"Camino encontrado: {' -> '.join(camino_realizado)}")
        print(f"Costo total: {peso_total}")
        print(f"Saltos hechos: {len(camino_realizado) - 1}")
    else:
        print(f"No se encontró un camino entre {origen} y {destino}")
    
    return camino_realizado, peso_total

# f. calcule el camino mas corto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader
print()
print("---------------------------------")
print("Camino más corto entre personajes usando Dijkstra")
mostrar_camino_mas_corto_entre_personajes(grafo, "C-3PO", "R2-D2")
mostrar_camino_mas_corto_entre_personajes(grafo, "Yoda", "Darth Vader")
print("---------------------------------")

# g. indicar qué personajes aparecieron en los nueve episodios de la saga
print()
print("---------------------------------")
print("Personajes que aparecieron en los 9 episodios")
print("---------------------------------")

personajes_9_episodios = []

# Verificar cada personaje
for personaje in personajes:
    if personaje in apariciones:
        # Contar en cuántos episodios aparece
        num_episodios = len(apariciones[personaje])
        
        # Si apareció en los 9 episodios
        if num_episodios == 9:
            personajes_9_episodios.append(personaje)

print(f"\nTotal de personajes que aparecieron en los 9 episodios: {len(personajes_9_episodios)}\n")

if personajes_9_episodios:
    for personaje in personajes_9_episodios:
        episodios = sorted(apariciones[personaje])
        print(f"  • {personaje}")
        print(f"    Episodios: {episodios}")
else:
    print("No hay personajes que aparecieron en los 9 episodios.")

print("---------------------------------")