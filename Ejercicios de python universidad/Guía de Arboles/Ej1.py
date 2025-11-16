# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
# toria– que resuelva las siguientes actividades:
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.

from tree import BinaryTree
from random import randint

numeros = BinaryTree()

print("Lista original:")
for i in range(25):
    numeros.insert(randint(0, 100))
print()

print("A) ")
print("Recorrido pre-orden")
numeros.pre_order()
print()
print("Recorrido in-orden")
numeros.in_order()
print()
print("Recorrido post-orden")
numeros.post_order()
print("Recorrido por nivel")
numeros.by_level()
print()

print("B) ")
num = int(input("Ingrese un numero a buscar en el arbol:"))
pos = numeros.search(num)
if pos:
    print(f"El numero {num} se encuentra en el arbol")
else:
    print(f"El numero {num} no se encuentra en el arbol")

print("C) ")
for i in range(3):
    num = int(input("Ingrese un numero a eliminar del arbol:"))
    pos = numeros.delete(num)

    if pos is not None:
        print(f"El numero {num} fue eliminado del arbol")
    else:
        print(f"El numero {num} no se encuentra en el arbol")

print("El arbol quedo de la siguiente manera: ")
numeros.pre_order()
print()

print("D) ")
alt_izq = numeros.hight(numeros.root.left)
print(f"La altura del subarbol izquierdo es: {alt_izq}")
alt_derec = numeros.hight(numeros.root.right)
print(f"La altura del subarbol derecho es: {alt_derec}")

print("E) ")
num = int(input("Ingrese un numero para contar sus ocurrencias en el arbol:"))

contador = contar_repeticiones(numeros.root, num)

if contador > 0:
    (f"El numero {num} se encuentra {contador} veces dentro del arbol")
else:
    print("El numero no se encuentra en el arbol")

print("F) ")
while True:
    if numeros.root is None:
        break
    elif numeros.root.value % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1


print(
    f"En el arbol hay {contador_pares} numeros pares y {contador_impares} numeros impares")
