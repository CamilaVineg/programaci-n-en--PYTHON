# 5. Determinar si una cadena de caracteres es un palíndromo.
from Stack_ import Stack


def determinar_palíndromo(palabra) -> bool:
    pila_aux = Stack()
    palabra_invertida = ""

    for caracter in palabra:
        pila_aux.apilar(caracter)

    while pila_aux.tamanio() > 0:
        palabra_invertida += pila_aux.desapilar()

    if palabra == palabra_invertida:
        print(f"La palabra {palabra} es un palíndromo.")
    else:
        print(f"La palabra {palabra} no es un palíndromo.")


palabra = input("Ingrese la palabra que desea evaluar como palíndromo:")
determinar_palíndromo(palabra)
