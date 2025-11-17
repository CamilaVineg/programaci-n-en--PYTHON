from tree import BinaryTree
from super_heroes_data import superheroes

# --------------------------------------------
# FUNCIONES DEL EJERCICIO
# --------------------------------------------

# C) Mostrar todos los superhéroes que empiezan con C.


def heroes_starting_with(tree, prefix):
    def __heroes_starting_with(root):
        if root is not None:
            __heroes_starting_with(root.left)
            if root.value.startswith(prefix) and root.other_values["is_villain"] is False:
                print(root.value)
            __heroes_starting_with(root.right)

    if tree.root is not None:
        __heroes_starting_with(tree.root)


# D) Actualizar nombre por búsqueda por proximidad
def update_name(tree, new_name, old_name, resultados):
    old_name = old_name.lower()

    for nodo in resultados:
        if nodo.value.lower() == old_name:
            nodo.value = new_name
            print("Nombre actualizado correctamente:", nodo.value)
            return

    print("No se encontró el nombre exacto para actualizar.")


# --------------------------------------------
# PROGRAMA PRINCIPAL
# --------------------------------------------

# A) Crear el árbol e insertar datos CORRECTAMENTE
arbol = BinaryTree()
heroes_tree = BinaryTree()
villains_tree = BinaryTree()

for hero in superheroes:
    arbol.insert(
        hero["name"],
        {"is_villain": hero["is_villain"]
         }
    )
print()
print("------------------------------------------------------")
print()
print("Árbol original (in-order):")
arbol.in_order()
print()

print()
print("------------------------------------------------------")
print()
# B) Listar villanos ordenados alfabéticamente
print("Villanos ordenados alfabéticamente:")
arbol.villain_in_order()
print()

print()
print("------------------------------------------------------")
print()
# C) Superhéroes que empiezan con C
print("Superhéroes que empiezan con C:")
heroes_starting_with(arbol, "C")
print()

print()
print("------------------------------------------------------")
print()
# D) Cantidad de superhéroes en el árbol
heroes_count = arbol.count_heroes()
print("Cantidad de superhéroes en el árbol:", heroes_count)
print()

print()
print("------------------------------------------------------")
print()
# E) Búsqueda por proximidad y cambio de nombre
busc = input("Ingrese el nombre a buscar (Dr Strange): ")

print("\nResultados de la búsqueda por proximidad:")
resultados = arbol.proximity_search(busc)

for res in resultados:
    print(res.value)

viejo = input(
    "Elija el nombre correcto a cambiar (ingrese el nombre tal cual aparece):")

actualizacion = input("\nIngrese el nombre correcto (Doctor Strange): ")
print("\nActualizando nombre...")
update_name(arbol, actualizacion, viejo, resultados)
print()

print("------------------------------------------------------")
print()
# F) Listado descendente de superhéroes
print("Listado descendente (post-order):")
arbol.post_order()
print()

print()
print("------------------------------------------------------")
print()
# G) Dividir árbol en héroes y villanos
print("Dividiendo el árbol en héroes y villanos...")
arbol.divide_tree(heroes_tree, villains_tree)
print("Bosque creado con éxito.\n")

print()
print("------------------------------------------------------")
print()
# II) Barrido ordenado de cada árbol
print("Árbol de héroes (in-order):")
heroes_tree.in_order()
print()

print()
print("------------------------------------------------------")
print()
print("Árbol de villanos (in-order):")
villains_tree.in_order()
print()
print()
print("------------------------------------------------------")
print()
# I) Cantidad de nodos en cada árbol
heroes_count = heroes_tree.count_nodes()
villains_count = villains_tree.count_nodes()

print("Cantidad de nodos en el árbol de héroes:", heroes_count)
print("Cantidad de nodos en el árbol de villanos:", villains_count)
