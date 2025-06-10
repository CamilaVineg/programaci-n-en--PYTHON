from typing import Any, Optional


class Cola:

    def __init__(self):
        self.__elements = []

    def encolar(self, value: Any) -> None:
        self.__elements.append(value)

    def desencolar(self) -> Optional[Any]:
        return (
            self.__elements.pop(0)
            if self.__elements
            else None
        )

    def tamanio(self) -> int:
        return len(self.__elements)

    def en_frente(self) -> Optional[Any]:
        return (
            self.__elements[0]
            if self.__elements
            else None
        )

    def mover_al_final(self) -> Optional[Any]:
        if self.__elements:
            value = self.desencolar()
            self.encolar(value)
            return value

    def mostrar(self):
        for i in range(len(self.__elements)):
            print(self.mover_al_final())
