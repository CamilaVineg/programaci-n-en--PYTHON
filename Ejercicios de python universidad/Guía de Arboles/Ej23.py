# 23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado in_orden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

from tree import BinaryTree

# a. listado in_orden de las criaturas y quienes la derrotaron

arbol = BinaryTree()

Criaturas = [ {"criatura" : "Ceto", "derrotado por" : None},
             {"criatura" : "Tifón", "derrotado por" : "Zeus"},
             {"criatura" : "Equidna", "derrotado por" : "Argos Panoptes"},
             {"criatura" : "Dino", "derrotado por" :  None},
             {"criatura" : "Pefredo", "derrotado por" :  None},
             {"criatura" : "Enio", "derrotado por" :  None},
             {"criatura" : "Escila", "derrotado por" :  None},
             {"criatura" : "Caribdis", "derrotado por" : None},
             {"criatura" : "Euríale", "derrotado por" : None},
             {"criatura" : "Esteno", "derrotado por" : None},
             {"criatura" : "Medusa", "derrotado por" : "Perseo"},
             {"criatura" : "Ladón", "derrotado por" : "Heracles"},
             {"criatura" : "Águila del Cáucaso", "derrotado por" :  None},
             {"criatura" : "Quimera", "derrotado por" : "Belerofonte"},
             {"criatura" : "Hidra de Lerna", "derrotado por" : "Heracles"},
             {"criatura" : "León de Nemea", "derrotado por" : "Heracles"},
             {"criatura" : "Esfinge", "derrotado por" : "Edipo"},
             {"criatura" : "Dragón de la Cólquida", "derrotado por" :  None},
             {"criatura" : "Cerbero", "derrotado por" :  None},
             {"criatura" : "Cerda de Cromión", "derrotado por" : "Teseo"},
             {"criatura" : "Ortro", "derrotado por" : "Heracles"},
             {"criatura" : "Toro de Creta", "derrotado por" : "Teseo"},
             {"criatura" : "Jabalí de Calidón", "derrotado por" : "Atalanta"},
             {"criatura" : "Carcinos", "derrotado por" :  None},
             {"criatura" : "Gerión", "derrotado por" : "Heracles"},
             {"criatura" : "Cloto", "derrotado por" :  None},
             {"criatura" : "Láquesis", "derrotado por" :  None},
             {"criatura" : "Átropos", "derrotado por" :  None},
             {"criatura" : "Minotauro de Creta", "derrotado por" : "Teseo"},
             {"criatura" : "Harpías", "derrotado por" :  None},
             {"criatura" : "Argos Panoptes", "derrotado por" : "Hermes"},
             {"criatura" : "Aves del Estínfalo", "derrotado por" :  None},
             {"criatura" : "Talos", "derrotado por" : "Medea"},
             {"criatura" : "Sirenas", "derrotado por" :  None},
             {"criatura" : "Pitón", "derrotado por" : "Apolo"},
             {"criatura" : "Cierva de Cerinea", "derrotado por" :  None},
             {"criatura" : "Basilisco", "derrotado por" :  None},
             {"criatura" : "Jabalí de Erimanto", "derrotado por" :  None},
             ]

for cria in Criaturas:
    arbol.insert(
            cria["criatura"],
            {
                "derrotado por": cria["derrotado por"]}
        )

arbol.in_order()
print()