from typing import Any

class HeapMax:

    def __init__(self):
        self.elements = []
    
    def tamanio(self) -> int:
        return len(self.elements)

    def agregar_prioridad(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size()-1)
    
    def eliminar(self) -> Any:
        last = self.tamanio() -1
        self.intercambio(0, last)
        value = self.elements.pop()
        self.hundir(0)
        return value

    def flotar(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            # print(f'flotar desde {index} a {father}')
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    def hundir(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.tamanio():
            right_son = left_son + 1

            mayor = left_son
            if right_son < self.tamanio():
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son

            if self.elements[index] < self.elements[mayor]:
                # print(f'hundir desde {index} a {mayor}')
                self.intercambio(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False


    def intercambio(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    def ordenar_montículo(self) -> list:
        result = []
        while self.tamanio() > 0:
            result.append(self.eliminar())
        return result

    def apilar(self, value: Any, priority: int) -> None:
        # priority 1-low, 2-medium, 3-high
        self.agregar_prioridad([priority, value])
    
    def desapilar(self) -> Any:
        value = self.eliminar()
        return value


class HeapMin:

    def __init__(self):
        self.elements = []
    
    def tamanio(self) -> int:
        return len(self.elements)

    def agregar_prioridad(self, value: Any) -> None:
        self.elements.append(value)
        self.flotar(self.tamanio()-1)
    
    def buscar(self, value):
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index

    def eliminar(self) -> Any:
        last = self.tamanio() -1
        self.intercambio(0, last)
        value = self.elements.pop()
        self.hundir(0)
        return value

    def flotar(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index] < self.elements[father]:
            self.intercambio(index, father)
            index = father
            father = (index - 1) // 2

    def hundir(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            minor = left_son
            if right_son < self.size():
                if self.elements[right_son] < self.elements[minor]:
                    minor = right_son

            if self.elements[index] > self.elements[minor]:
                self.interchange(index, minor)
                index = minor
                left_son = (2 * index) + 1
            else:
                control = False


    def intercambio(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # def monticulizar

    def ordenar_montículo(self) -> list:
        result = []
        while self.tamanio() > 0:
            result.append(self.eliminar())
        return result

    def apilar(self, value: Any, priority: int) -> None:
        # priority 1-low, 2-medium, 3-high
        self.add([priority, value])
    
    def desapilar(self) -> Any:
        value = self.remove()
        return value

    def cambiar_prioridad(self, index, new_priority):
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.hundir(index)
            elif new_priority < previous_priority:
                self.flotar(index)

# priority_queue = HeapMin()

# priority_queue.arrive('x', 1)
# priority_queue.arrive('b', 2)
# priority_queue.arrive('a', 2)
# priority_queue.arrive('f', 1)
# priority_queue.arrive('y', 1)
# priority_queue.arrive('j', 2)
# priority_queue.arrive('z', 3)
# print(priority_queue.elements)

# while priority_queue.size() > 0:
#     print(priority_queue.attention())

# h = HeapMin()
# h.add(19)
# h.add(5)
# h.add(1)
# h.add(3)
# h.add(9)


# list_sort = h.heapsort()

# print(list_sort)
# print(h.elements)

