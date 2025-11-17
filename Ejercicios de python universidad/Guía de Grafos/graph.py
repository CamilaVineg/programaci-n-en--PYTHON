from typing import Any, Optional

from Heap_ import HeapMin
from List import List
from Queue_ import Queue
from Stack_ import Stack

class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            self.edges.add_criterion('value', Graph._order_by_value)
            self.edges.add_criterion('weight', Graph._order_by_weight)
            self.other_values = other_values
            self.visited = False
        
        def __str__(self):
            return self.value
    
    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values # no esta en uso aun
        
        def __str__(self):
            return f'Destination: {self.value} with weight --> {self.weight}'
    
    def __init__(self, is_directed=False):
        self.add_criterion('value', self._order_by_value)
        self.is_directed = is_directed

    def ordenar_por_valor(item):
        return item.value

    def ordenar_por_peso(item):
        return item.weight
    
    def mostrar(
        self
    ) -> None:
        for vertex in self:
            print(f"Vertex: {vertex}")
            vertex.edges.show() 

    def insertar_vertice(
        self,
        value: Any,
    ) -> None:
        node_vertex = Graph.__nodeVertex(value)
        self.append(node_vertex)

    def insertar_adyacente(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        origin = self.search(origin_vertex, 'value')
        destination = self.search(destination_vertex, 'value')
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            if self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    def eliminar_adyacente(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        pos_origin = self.buscar(origin, key_value)
        if pos_origin is not None:
            edge = self[pos_origin].edges.eliminar_valor(destination, key_value)
            if self.dirigido and edge is not None:
                pos_destination = self.search(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.eliminar_valor(origin, key_value)
            return edge

    def eliminar_vertice(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        delete_value = g.eliminar_valor(value, key_value_vertex)
        if delete_value is not None:
            for vertex in self:
                self.eliminar_adyacente(vertex.value, value, key_value_edges)
        return delete_value

    def marcar_como_noVisitado(self) -> None:
        for vertex in self:
            vertex.visited = False

    def camino_existente(self, origin, destination):
        def __camino_existente(graph, origin, destination):
            result = False
            vertex_pos = graph.buscar(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visitado:
                    graph[vertex_pos].visitado = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.buscar(edge.value, 'value')
                            if not graph[destination_edge_pos].visitado:
                                result = __camino_existente(graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result
        
        self.marcar_como_noVisitado()
        result = __camino_existente(self, origin, destination)
        return result
    
    def barrido_profundo(self, value) -> None:
        def __barrido_profundo(graph, value):
            vertex_pos = graph.buscar(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visitado:
                    graph[vertex_pos].visitado = True
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.buscar(edge.value, 'value')
                        if not graph[destination_edge_pos].visitado:
                            __barrido_profundo(graph, graph[destination_edge_pos].value)

        self.marcar_como_noVisitado()
        __barrido_profundo(self, value)
        
    def barrido_amplio(self, value)-> None:
        queue_vertex = Queue()
        self.marcar_como_noVisitado()
        vertex_pos = self.buscar(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visitado:
                self[vertex_pos].visitado = True
                queue_vertex.encolar(self[vertex_pos])
                while queue_vertex.tamanio() > 0:
                    vertex = queue_vertex.desencolar()
                    print(vertex.value)
                    for edge in vertex.edges:
                        destination_edge_pos = self.buscar(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visitado:
                                self[destination_edge_pos].visitado = True
                                queue_vertex.encolar(self[destination_edge_pos])

    def dijkstra(self, origin):
        from math import inf
        no_visited = HeapMin()
        path = Stack()
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            no_visited.apilar([vertex.value, vertex, None], distance)
        while no_visited.tamanio() > 0:
            value = no_visited.desapilar()
            costo_nodo_actual = value[0]
            path.apilar([value[1][0], costo_nodo_actual, value[1][2]])
            edges = value[1][1].edges
            for edge in edges:
                pos = no_visited.buscar(edge.value)
                if pos is not None:
                    if pos is not None:
                        if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                            no_visited.elements[pos][1][2] = value[1][0]
                            no_visited.cambiar_prioridad(pos, costo_nodo_actual + edge.weight)
        return path

    def kruskal(self, origin_vertex):
        def buscar_enEl_bosque(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index
                
        forest = []
        edges = HeapMin()
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                edges.arrive([vertex.value, edge.value], edge.weight)
        
        while len(forest) > 1 and edges.tamanio() > 0:
            edge = edges.desapilar()
            origin = buscar_enEl_bosque(forest, edge[1][0])
            destination = buscar_enEl_bosque(forest, edge[1][1])
            if origin is not None and destination is not None:
                if origin != destination:
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)


                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';'+f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination+';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')
        
        from_vertex = buscar_enEl_bosque(forest, origin_vertex)
        
        return forest[from_vertex] if from_vertex is not None else forest


g = Graph(is_directed=True)

g.insert_vertex('T')
g.insert_vertex('F')
g.insert_vertex('R')
g.insert_vertex('X')
g.insert_vertex('Z')
# g.insert_vertex('A')
# g.insert_vertex('B')

g.insert_edge('T', 'X', 6)
g.insert_edge('T', 'F', 3)
g.insert_edge('T', 'R', 8)
g.insert_edge('F', 'X', 2)
g.insert_edge('F', 'R', 2)
g.insert_edge('R', 'X', 5)
g.insert_edge('Z', 'R', 4)
g.insert_edge('Z', 'X', 9)
# g.insert_edge('A', 'B', 15)

# g.show()
print(g.exist_path('T', 'Z'))
# expansion_tree = g.kruskal('F')
# print(expansion_tree)
# peso_total = 0
# for edge in expansion_tree.split(';'):
#     origin, destination, weight = edge.split('-')
#     print(f'origin {origin} destination {destination}')
#     peso_total += int(weight)
# print(f'peso total: {peso_total}')
# path = g.dijkstra('T')
# destination = 'Z'
# peso_total = None
# camino_completo = []

# while path.size() > 0:
#     value = path.pop()
#     if value[0] == destination:
#         if peso_total is None:
#             peso_total = value[1]
#         camino_completo.append(value[0])
#         destination = value[2]
# camino_completo.reverse()
# print(f'el camino mas corto es: {"-".join(camino_completo)} con un costo de {peso_total}')

# vertex = g.delete_vertex('A', 'value')
# print(f'deleted vertex: {vertex}')

# g.amplitude_sweep('A')

# print()
# for vertex in g:
#     print(vertex.value, vertex.visited)
# g.show()
# print('segundo barrido')
# g.deep_sweep('I')

# es_adyacente(vértice, destino). Devuelve verdadero (true) si el destino es un nodo adyacente
# al vértice;
# adyacentes(vértice). Realiza un barrido de los nodos adyacentes al vértice;

# existe _paso(grafo, vértice origen, vértice destino). Devuelve verdadero (true) si es posible ir des-
# de el vértice origen hasta el vértice destino, caso contrario retornará falso (false);

# barrido_profundidad(grafo, vértice inicio). Realiza un barrido en profundidad del grafo a par-
# tir del vértice de inicio;

# barrido_amplitud(grafo, vértice inicio). Realiza un barrido en amplitud del grafo a partir del
# vértice de inicio;