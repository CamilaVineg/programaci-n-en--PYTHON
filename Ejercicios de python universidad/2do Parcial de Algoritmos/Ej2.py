# Ejercicio 2: Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos
# necesarios para resolver las siguientes tareas:
# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
# b. hallar el árbol de expansión mínimo desde el vértice que contiene a: C-3PO, Yoda y Leia;
# c. determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número;
# d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8;
# f. calcule el camino mas ccorto desde: C-3PO a R2-D2 y desde Yoda a Darth Vader;
# g. indicar qué personajes aparecieron en los nueve episodios de la saga.

from graph import Graph

from starwars_data import personajes, apariciones

# a. construccion del grafo.
grafo = Graph(dirigido=False)
