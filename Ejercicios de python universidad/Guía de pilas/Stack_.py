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

    def esta_vacia(self) -> bool:
        return len(self.__elements) == 0

    def tamanio(self) -> int:
        return len(self.__elements)

    def ver_tope(self) -> Optional[Any]:
        return (
            self.__elements[-1]
            if self.__elements
            else None
        )

    def mostrar(self):
        pila_aux = Stack()
        while self.tamanio() > 0:
            valor = self.desapilar()
            print(valor)
            pila_aux.apilar(valor)
        while pila_aux.tamanio() > 0:
            self.apilar(pila_aux.desapilar())
