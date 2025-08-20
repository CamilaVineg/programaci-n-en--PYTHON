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

arbol = BinaryTree()

# a
for hero in superheroes:
    arbol.insert(hero['name'], hero['is_villain'])

# b


def villanos_en_orden(arbol):
    villanos = []

    def villanos_en_orden_recursivo(node):

        if node is not None:
            villanos_en_orden_recursivo(node.left)
            print("Evaluando nodo:", node.value)
            if node.other_values:  # Si es villano
                # voy agregando a una lista los villanos
                villanos.append(node.value)

            villanos_en_orden_recursivo(node.right)

    villanos_en_orden_recursivo(arbol.root)

    return villanos


lista_de_villanos = villanos_en_orden(arbol)
for v in lista_de_villanos:
    print(v)
