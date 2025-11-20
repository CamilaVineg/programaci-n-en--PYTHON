from typing import Any, Optional


class Cola:
    def __init__(self):
        # Lista interna que representa la cola
        self.__elementos = []

    def encolar(self, dato: Any) -> None:
        # Agrega un nuevo dato al final de la cola
        self.__elementos.append(dato)

    def desencolar(self) -> Optional[Any]:
        # Saca el primer dato de la cola y lo devuelve
        # Si la cola está vacía, devuelve None
        if not self.tamanio() == 0:
            return self.__elementos.pop(0)
        else:
            return None

    def tamanio(self) -> int:
        # Devuelve cuántos elementos hay en la cola
        return len(self.__elementos)

    def ver_frente(self) -> Optional[Any]:
        # Muestra el dato que está al frente (sin sacarlo)
        # Devuelve None si la cola está vacía
        if not self.tamanio() == 0:
            return self.__elementos[0]
        else:
            return None

    def mover_al_final(self) -> Optional[Any]:
        # Saca el dato del frente y lo vuelve a poner al final
        if not self.tamanio() == 0:
            dato = self.desencolar()
            self.encolar(dato)
            return dato

    def mostrar(self) -> None:
        # Muestra todos los elementos de la cola, en orden
        for _ in range(len(self.__elementos)):
            print(self.mover_al_final())