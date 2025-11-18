
from typing import Any, Optional


class Stack:

    def __init__(self):
        self.__elements = []


    def apilar(self, value: Any) -> None:
        self.__elements.append(value)

    def desapilar(self) -> Optional[Any]:
        return (
            self.__elements.pop()
            if self.__elements
            else None
        )

    def tamanio(self) -> int:
        return len(self.__elements)

    def en_frente(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def mostrar(self):
        aux_stack = Stack()
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
        
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())