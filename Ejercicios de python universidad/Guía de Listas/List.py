from typing import Any, Optional


class List(list):

    CRITERION_FUNCTIONS = {}

    def agregar_criterio(
        self,
        key_criterion: str,
        function,
    ):
        self.CRITERION_FUNCTIONS[key_criterion] = function

    def eliminar_elemento(
        self,
        value,
        key_value: str = None,
    ) -> Optional[Any]:
        index = self.buscar(value, key_value)
        return self.pop(index) if index is not None else None

    def ordenar_por_criterio(
        self,
        criterion_key: str = None,
    ) -> None:
        criterion = self.CRITERION_FUNCTIONS.get(criterion_key)

        if criterion is not None:
            self.sort(key=criterion)
        elif self and isinstance(self[0], (int, str, bool)):
            self.sort()
        else:
            print('criterio de orden no encontrado')

    def buscar(
        self,
        search_value,
        search_key: str = None,
    ) -> Optional[int]:
        self.ordenar_por_criterio(search_key)
        start = 0
        end = len(self) - 1

        while start <= end:
            middle = (start + end) // 2
            criterion = self.CRITERION_FUNCTIONS.get(search_key)
            if criterion is None and self and not isinstance(self[0], (int, str, bool)):
                return None

            value = criterion(self[middle]) if criterion else self[middle]
            if value == search_value:
                return middle
            elif value < search_value:
                start = middle + 1
            else:
                end = middle - 1
        return None

    def mostrar(self) -> None:
        for element in self:
            print(element)
