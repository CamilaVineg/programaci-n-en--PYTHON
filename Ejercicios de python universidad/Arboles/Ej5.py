from tree import BinaryTree
from super_heroes_data import superheroes

# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
# se (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
# leano que indica si es un héroe o un villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.


# c) Mostrar todos los superhéroes que empiezan con C.

def heroes_starting_with(self, prefix):
    def __heroes_starting_with_(root):
        if root is not None:
            __heroes_starting_with_(root.left)
            if root.value["name"].startswith(prefix) and not root.value["is_villain"]:
                print(root.value["name"])
            __heroes_starting_with_(root.right)
    if self.root is not None:
        __heroes_starting_with_(self.root)


# d) Determinar cuántos superhéroes hay el árbol.


def count_heroes(self):
    def __count_heroes(root):
        count = 0
        if root is not None:
            if not root.value["is_villain"]:
                count += 1
            count += __count_heroes(root.left)
            count += __count_heroes(root.right)
        return count

    return __count_heroes(self.root)

# e) Cambiar nombre de Dr Strange a Doctor Strange por medio
# de búsqueda por proximidad.


def update_name(self, new_name, prefix, resultados):
    for nodo in resultados:
        if nodo.value["name"] == prefix:
            nodo.value["name"] = new_name
            print("Nombre actualizado correctamente.")
            print(nodo.value["name"])


# Programa principal.
# A) Crear el árbol e insertar los datos.
arbol = BinaryTree()
heroes_tree = BinaryTree()
villains_tree = BinaryTree()

for hero in superheroes:
    arbol.insert({"name": hero['name'], "is_villain": hero['is_villain']})

print("Arbol original:")
arbol.in_order()
print()
# B)
print("Villanos ordenados alfabeticamente:")
arbol.villain_in_order()
print()

# C)
print("Superheroes que empiezan con C:")
heroes_starting_with(arbol, "C")
print()

# D)
heroes_count = arbol.count_heroes()
print("Cantidad de superhéroes en el arbol: ", heroes_count)
print()

# E)
busc = input("Ingrese el nombre a buscar (Dr Strange):")
print("resultados de la busqueda por proximidad:")
resultados = arbol.proximity_search(busc)  # Suponiendo que devuelve una lista
for res in resultados:
    print(res.value)


actualizacion = input("Ingrese el nombre correcto(Doctor Strange):")
print("Actualizando nombre de Dr Strange a Doctor Strange. . .")
update_name(arbol, actualizacion, busc, resultados)
print()

# F)
print("Listado descendente de superhéroes:")
arbol.post_order()
print()

# G)
print("Dividiendo el arbol en heroes y villanos. . .")
arbol.divide_tree(heroes_tree, villains_tree)
bosque = [heroes_tree, villains_tree]
print("Bosque creado con exito.")
print()
# II. Realizar un barrido ordenado alfabéticamente de cada árbol.
print("Arbol de heroes(barrido en orden/ordenado alfabeticamente):")
heroes_tree.in_order()
print()
print("Arbol de villanos(barrido en orden/ordenado alfabeticamente):")
villains_tree.in_order()
print()

# I. Determinar cuantos nodos tiene cada arbol.
heroes_count = heroes_tree.count_nodes()
print("Cantidad de nodos en el arbol de heroes: ", heroes_count)
villains_count = villains_tree.count_nodes()
print("Cantidad de nodos en el arbol de villanos: ", villains_count)
