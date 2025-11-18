# graph.py (adaptado a tus archivos: Heap_.py, List.py, y clases Cola/Stack tal cual)

from typing import Any, Optional

# imports resilientes — intento varios nombres comunes según tus archivos
try:
    from Heap_ import HeapMin
except Exception:
    try:
        from heap import HeapMin
    except Exception:
        HeapMin = None  # si llega a pasar, el error saldrá al usarlo

try:
    from List import List
except Exception:
    try:
        from list_ import List
    except Exception:
        # fallback muy básico (puede romper funciones que usan criterios)
        List = list

# cola: intentamos mapear tu clase Cola a la variable Queue (para no reescribir todo)
Queue = None
try:
    from cola import Cola as ColaClass  # nombre posible
    Queue = ColaClass
except Exception:
    try:
        from queue_ import Queue as QueueClass
        Queue = QueueClass
    except Exception:
        try:
            from Cola import Cola as ColaClass
            Queue = ColaClass
        except Exception:
            # si no existe el módulo, dejalo en None -> error claro al ejecutar
            Queue = None

# stack: similar, mantenemos el nombre Stack (pero sus métodos internos se respetan)
Stack = None
try:
    from stack import Stack as StackClass
    Stack = StackClass
except Exception:
    try:
        from Stack import Stack as StackClass
        Stack = StackClass
    except Exception:
        Stack = None


class Graph(List):

    class __nodeVertex:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.edges = List()
            # usar los nombres reales del List: agregar_criterio
            if hasattr(self.edges, "agregar_criterio"):
                self.edges.agregar_criterio('value', Graph._order_by_value)
                self.edges.agregar_criterio('weight', Graph._order_by_weight)
            else:
                # si List no tiene agregar_criterio, seguimos sin crash inmediato
                pass
            self.other_values = other_values
            self.visited = False

        def __str__(self):
            return str(self.value)

    class __nodeEdge:

        def __init__(self, value: Any, weight: Any, other_values: Optional[Any] = None):
            self.value = value
            self.weight = weight
            self.other_values = other_values  # no esta en uso aun

        def __str__(self):
            return f'Destination: {self.value} with weight --> {self.weight}'

    def __init__(self, is_directed=False):
        # en List.py el método se llama agregar_criterio
        if hasattr(self, "agregar_criterio"):
            self.agregar_criterio('value', self._order_by_value)
        self.is_directed = is_directed

    def _order_by_value(item):
        return item.value

    def _order_by_weight(item):
        return item.weight

    def show(
        self
    ) -> None:
        # show nativo lo dejo igual pero uso mostrar en listas internas
        for vertex in self:
            print(f"Vertex: {vertex}")
            if hasattr(vertex.edges, "mostrar"):
                vertex.edges.mostrar()
            else:
                # fallback: iterar y print
                for e in vertex.edges:
                    print(e)

    def insert_vertex(
        self,
        value: Any,
    ) -> None:
        node_vertex = Graph.__nodeVertex(value)
        self.append(node_vertex)

    def insert_edge(self, origin_vertex: Any, destination_vertex: Any, weight: int) -> None:
        origin = self.buscar(origin_vertex, 'value')  # usar buscar de List
        destination = self.buscar(destination_vertex, 'value')
        if origin is not None and destination is not None:
            node_edge = Graph.__nodeEdge(destination_vertex, weight)
            self[origin].edges.append(node_edge)
            # si el grafo NO es dirigido, agregamos la arista inversa
            if not self.is_directed and origin != destination:
                node_edge = Graph.__nodeEdge(origin_vertex, weight)
                self[destination].edges.append(node_edge)
        else:
            print('no se puede insertar falta uno de los vertices')

    def delete_edge(
        self,
        origin,
        destination,
        key_value: str = None,
    ) -> Optional[Any]:
        pos_origin = self.buscar(origin, key_value)
        if pos_origin is not None:
            # en List.py eliminar_valor
            edge = self[pos_origin].edges.eliminar_valor(destination, key_value) if hasattr(
                self[pos_origin].edges, "eliminar_valor") else None
            if not self.is_directed and edge is not None:
                pos_destination = self.buscar(destination, key_value)
                if pos_destination is not None:
                    self[pos_destination].edges.eliminar_valor(
                        origin, key_value)
            return edge

    def delete_vertex(
        self,
        value,
        key_value_vertex: str = None,
        key_value_edges: str = 'value',
    ) -> Optional[Any]:
        # corregido: usar self.eliminar_valor (List.py)
        if hasattr(self, "eliminar_valor"):
            delete_value = self.eliminar_valor(value, key_value_vertex)
        else:
            # fallback: intentar buscar y pop
            pos = self.buscar(value, key_value_vertex)
            delete_value = self.pop(pos) if pos is not None else None

        if delete_value is not None:
            for vertex in self:
                # eliminar todas las aristas hacia el valor eliminado
                if hasattr(self, "delete_edge"):
                    self.delete_edge(vertex.value, value, key_value_edges)
                else:
                    # fallback: intentar eliminar en edges manualmente si existe
                    try:
                        vertex.edges.eliminar_valor(value, key_value_edges)
                    except Exception:
                        pass
        return delete_value

    def mark_as_unvisited(self) -> None:
        for vertex in self:
            vertex.visited = False

    def exist_path(self, origin, destination):
        def __exist_path(graph, origin, destination):
            result = False
            vertex_pos = graph.buscar(origin, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    if graph[vertex_pos].value == destination:
                        return True
                    else:
                        for edge in graph[vertex_pos].edges:
                            destination_edge_pos = graph.buscar(
                                edge.value, 'value')
                            if destination_edge_pos is not None and not graph[destination_edge_pos].visited:
                                result = __exist_path(
                                    graph, graph[destination_edge_pos].value, destination)
                                if result:
                                    break
            return result

        self.mark_as_unvisited()
        result = __exist_path(self, origin, destination)
        return result

    def deep_sweep(self, value) -> None:
        def __deep_sweep(graph, value):
            vertex_pos = graph.buscar(value, 'value')
            if vertex_pos is not None:
                if not graph[vertex_pos].visited:
                    graph[vertex_pos].visited = True
                    print(graph[vertex_pos])
                    for edge in graph[vertex_pos].edges:
                        destination_edge_pos = graph.buscar(
                            edge.value, 'value')
                        if destination_edge_pos is not None and not graph[destination_edge_pos].visited:
                            __deep_sweep(
                                graph, graph[destination_edge_pos].value)

        self.mark_as_unvisited()
        __deep_sweep(self, value)

    def amplitude_sweep(self, value) -> None:
        # usar la Cola real (Queue referenciado a tu clase Cola)
        if Queue is None:
            raise ImportError(
                "No se encontró la implementación de Cola/Queue en los módulos importados.")
        queue_vertex = Queue()
        self.mark_as_unvisited()
        vertex_pos = self.buscar(value, 'value')
        if vertex_pos is not None:
            if not self[vertex_pos].visited:
                self[vertex_pos].visited = True
                # enqueue -> encolar
                queue_vertex.encolar(self[vertex_pos])
                while queue_vertex.tamanio() > 0:
                    vertex = queue_vertex.desencolar()
                    # en tu Cola, desencolar devuelve el elemento
                    print(vertex.value)
                    for edge in vertex.edges:
                        destination_edge_pos = self.buscar(edge.value, 'value')
                        if destination_edge_pos is not None:
                            if not self[destination_edge_pos].visited:
                                self[destination_edge_pos].visited = True
                                queue_vertex.encolar(
                                    self[destination_edge_pos])

    def dijkstra(self, origin):
        # usamos el HeapMin real (Heap_.py)
        if HeapMin is None:
            raise ImportError(
                "No se encontró la implementación de HeapMin para Dijkstra.")
        from math import inf
        no_visited = HeapMin()
        # path será una pila; en tu Stack, los métodos reales son 'aoilar' y 'desapilar' y 'tamanio'
        if Stack is None:
            raise ImportError(
                "No se encontró la implementación de Stack para Dijkstra.")
        path = Stack()

        # insertar nodos en el heap con el formato elegido: [distancia, [nodo, objeto_vertex, nodo_anterior]]
        for vertex in self:
            distance = 0 if vertex.value == origin else inf
            # heap.agregar_prioridad espera un único argumento (lista [priority, value])
            no_visited.agregar_prioridad(
                [distance, [vertex.value, vertex, None]])

        while no_visited.tamanio() > 0:
            # devuelve [priority, [nodo, objeto_vertex, nodo_anterior]]
            value = no_visited.eliminar()
            costo_nodo_actual = value[0]
            nodo_info = value[1]  # [vertex.value, vertex_obj, prev_node]
            # en tu Stack el método para apilar es 'aoilar' (tal cual pegaste)
            path.aoilar([nodo_info[0], costo_nodo_actual, nodo_info[2]])
            edges = nodo_info[1].edges
            for edge in edges:
                pos = no_visited.buscar(edge.value)
                if pos is not None:
                    # comparar y quizás cambiar prioridad
                    if costo_nodo_actual + edge.weight < no_visited.elements[pos][0]:
                        # actualizar nodo anterior almacenado en la estructura del heap
                        no_visited.elements[pos][1][2] = nodo_info[0]
                        # usar cambiar_prioridad del heap
                        no_visited.cambiar_prioridad(
                            pos, costo_nodo_actual + edge.weight)
        return path

    def kruskal(self, origin_vertex):
        def search_in_forest(forest, value):
            for index, tree in enumerate(forest):
                if value in tree:
                    return index

        if HeapMin is None:
            raise ImportError(
                "No se encontró la implementación de HeapMin para Kruskal.")
        forest = []
        edges = HeapMin()
        for vertex in self:
            forest.append(vertex.value)
            for edge in vertex.edges:
                # en tu HeapMin la inserción tipo prioridad es agregar_prioridad([priority, value])
                edges.agregar_prioridad(
                    [edge.weight, [vertex.value, edge.value]])

        while len(forest) > 1 and edges.tamanio() > 0:
            edge = edges.eliminar()  # [weight, [origin, destination]]
            origin = search_in_forest(forest, edge[1][0])
            destination = search_in_forest(forest, edge[1][1])
            if origin is not None and destination is not None:
                if origin != destination:
                    if origin > destination:
                        vertex_origin = forest.pop(origin)
                        vertex_destination = forest.pop(destination)
                    else:
                        vertex_destination = forest.pop(destination)
                        vertex_origin = forest.pop(origin)

                    if '-' not in vertex_origin and '-' not in vertex_destination:
                        forest.append(
                            f'{vertex_origin}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_destination:
                        forest.append(
                            vertex_origin+';'+f'{edge[1][0]}-{vertex_destination}-{edge[0]}')
                    elif '-' not in vertex_origin:
                        forest.append(vertex_destination+';' +
                                      f'{vertex_origin}-{edge[1][1]}-{edge[0]}')
                    else:
                        forest.append(vertex_origin+';'+vertex_destination +
                                      ';'+f'{edge[1][0]}-{edge[1][1]}-{edge[0]}')

        from_vertex = search_in_forest(forest, origin_vertex)

        return forest[from_vertex] if from_vertex is not None else forest
