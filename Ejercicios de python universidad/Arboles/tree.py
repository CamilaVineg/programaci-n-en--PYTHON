from typing import Any


class Tree:
    def __init__(self):
        self.root = None
        pass

    class __nodeTree:

        def __init__(self, value: Any):
            self.value = value
            self.left = None
            self.right = None
            pass

    def insert(self, value: Any):
        def _insert(root, value: Any):
            if root is None:
                print("lugar libre insertar raiz")
                return __nodeTree(value)
            if value < root.value:
                print(
                    f"vamos pa la izquierda de la rama del nodo padre {root.value}")
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
                print(
                    f"vamos pa la derecha de la rama del nodo padre {root.value}")
            return root

        self.root = _insert(self.root, value)


arbol = Tree()

# inserta un elemento en un nodo.
arbol.insert(19)
arbol.insert(7)
arbol.insert(31)
arbol.insert(11)
print(arbol.root.value, arbol.root.left.value, arbol.root.right.value)
