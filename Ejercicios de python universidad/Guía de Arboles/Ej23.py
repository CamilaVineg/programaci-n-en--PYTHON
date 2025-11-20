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

def top_3_heroes(arbol):
        
    

arbol = BinaryTree()

Criaturas = [{"criatura": "Ceto", "derrotado por": None, "descripción": "Deidad marina primordial personificando los peligros del mar"},
             {"criatura": "Tifón", "derrotado por": "Zeus",
                 "descripción": "Monstruo gigante y poderoso que desafió a los dioses olímpicos"},
             {"criatura": "Equidna", "derrotado por": "Argos Panoptes",
                 "descripción": "Monstruo mitad mujer y mitad serpiente, madre de muchos monstruos famosos"},
             {"criatura": "Dino", "derrotado por":  None,
                 "descripción": "Monstruo marino gigante que aterrorizaba a los marineros"},
             {"criatura": "Pefredo", "derrotado por":  None,
                 "descripción": "Uno de los hijos de Ceto y Ponto, asociado con las tormentas marinas"},
             {"criatura": "Enio", "derrotado por":  None,
                 "descripción": "Otro hijo de Ceto y Ponto, también asociado con las tormentas marinas"},
             {"criatura": "Escila", "derrotado por":  None,
                 "descripción": "Monstruo marino con múltiples cabezas que atacaba a los barcos que pasaban cerca de ella"},
             {"criatura": "Caribdis", "derrotado por": None,
                 "descripción": "Monstruo marino que creaba remolinos peligrosos en el mar"},
             {"criatura": "Euríale", "derrotado por": None,
                 "descripción": "Una de las Gorgonas, hermanas de Medusa, con serpientes por cabello"},
             {"criatura": "Esteno", "derrotado por": None,
                 "descripción": "Otra de las Gorgonas, hermanas de Medusa, con serpientes por cabello"},
             {"criatura": "Medusa", "derrotado por": "Perseo",
                 "descripción": "La más famosa de las Gorgonas, cuya mirada convertía a las personas en piedra"},
             {"criatura": "Ladón", "derrotado por": "Heracles",
                 "descripción": "Dragón de cien cabezas que custodiaba las manzanas de oro en el Jardín de las Hespérides"},
             {"criatura": "Águila del Cáucaso", "derrotado por":  None,
                 "descripción": "Águila gigante que devoraba el hígado de Prometeo como castigo por robar el fuego a los dioses"},
             {"criatura": "Quimera", "derrotado por": "Belerofonte",
                 "descripción": "Monstruo híbrido con cabeza de león, cuerpo de cabra y cola de serpiente que lanzaba fuego"},
             {"criatura": "Hidra de Lerna", "derrotado por": "Heracles",
                 "descripción": "Monstruo acuático con múltiples cabezas; cuando una era cortada, dos más crecían en su lugar"},
             {"criatura": "León de Nemea", "derrotado por": "Heracles",
                 "descripción": "León invulnerable cuya piel no podía ser penetrada por armas"},
             {"criatura": "Esfinge", "derrotado por": "Edipo",
                 "descripción": "Criatura con cuerpo de león, alas de águila y cabeza de mujer que planteaba enigmas a los viajeros"},
             {"criatura": "Dragón de la Cólquida", "derrotado por":  None,
                 "descripción": "Dragón que custodiaba el Vellocino de Oro"},
             {"criatura": "Cerbero", "derrotado por":  None,
                 "descripción": "Perro de tres cabezas que guardaba la entrada al inframundo"},
             {"criatura": "Cerda de Cromión", "derrotado por": "Teseo",
                 "descripción": "Cerda gigante que aterrorizaba la región de Cromión"},
             {"criatura": "Ortro", "derrotado por": "Heracles",
                 "descripción": "Perro de dos cabezas que acompañaba a la Hidra de Lerna"},
             {"criatura": "Toro de Creta", "derrotado por": "Teseo",
                 "descripción": "Toro gigante que causaba estragos en Creta"},
             {"criatura": "Jabalí de Calidón", "derrotado por": "Atalanta",
                 "descripción": "Jabalí enorme enviado por Artemisa para devastar Calidón"},
             {"criatura": "Carcinos", "derrotado por":  None,
                 "descripción": "Cangrejo gigante que atacó a Heracles durante su lucha contra la Hidra de Lerna"},
             {"criatura": "Gerión", "derrotado por": "Heracles",
                 "descripción": "Gigante con tres cuerpos que poseía un rebaño de ganado rojo"},
             {"criatura": "Cloto", "derrotado por":  None,
                 "descripción": "Una de las Moiras, encargada de hilar el hilo de la vida"},
             {"criatura": "Láquesis", "derrotado por":  None,
                 "descripción": "Una de las Moiras, encargada de medir el hilo de la vida"},
             {"criatura": "Átropos", "derrotado por":  None,
                 "descripción": "Una de las Moiras, encargada de cortar el hilo de la vida"},
             {"criatura": "Minotauro de Creta", "derrotado por": "Teseo",
                 "descripción": "Criatura con cuerpo de hombre y cabeza de toro que habitaba el Laberinto de Creta"},
             {"criatura": "Harpías", "derrotado por":  None,
                 "descripción": "Monstruos alados con rostro de mujer que robaban comida y atormentaban a sus víctimas"},
             {"criatura": "Argos Panoptes", "derrotado por": "Hermes",
                 "descripción": "Gigante con cien ojos, conocido por su vigilancia constante"},
             {"criatura": "Aves del Estínfalo", "derrotado por":  None,
                 "descripción": "Aves carnívoras con picos de bronce y plumas afiladas como flechas"},
             {"criatura": "Talos", "derrotado por": "Medea",
                 "descripción": "Gigante de bronce que protegía la isla de Creta"},
             {"criatura": "Sirenas", "derrotado por":  None,
                 "descripción": "Criaturas con cuerpo de ave y cabeza de mujer, conocidas por su canto hipnótico que atraía a los marineros a la perdición"},
             {"criatura": "Pitón", "derrotado por": "Apolo",
                 "descripción": "Serpiente gigante que habitaba en Delfos y fue derrotada por Apolo"},
             {"criatura": "Cierva de Cerinea", "derrotado por":  None,
                 "descripción": "Cierva sagrada de Artemisa, conocida por su velocidad y astucia"},
             {"criatura": "Basilisco", "derrotado por":  None,
                 "descripción": "Serpiente legendaria cuya mirada podía matar"},
             {"criatura": "Jabalí de Erimanto", "derrotado por":  None,
                 "descripción": "Jabalí feroz que causaba estragos en la región de Erimanto"},
             ]

for cria in Criaturas:
    arbol.insert(
        cria["criatura"],
        {
            "derrotado por": cria["derrotado por"]}
    )

# ----------------------------------------------------------------------
# a. listado in_orden de las criaturas y quienes la derrotaron
# -----------------------------------------------------------------------
print("----------------------------------------------------------")
print("Listado in_orden de las criaturas y quienes la derrotaron:")
print("----------------------------------------------------------")

arbol.in_order()
print()

# ----------------------------------------------------------------------
# c. mostrar toda la información de la criatura Talos;
# ----------------------------------------------------------------------
print("----------------------------------------------------------")
print("Buscando a Talos:")
print("----------------------------------------------------------")

result = arbol.search("Talos")
if result:
    print(f"Criatura: Talos")
    print(f"Derrotado por: {result['derrotado por']}")
    print(f"{result['descripción']}")
else:
    print("La criatura Talos no fue encontrada.")

print()

# ----------------------------------------------------------------------
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# ----------------------------------------------------------------------
print("----------------------------------------------------------")
print("TOP 3 HÉROES/DIOSES QUE DERROTARON MÁS CRIATURAS")
print("----------------------------------------------------------")

