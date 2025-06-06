# 6. Leer una palabra y visualizarla en forma inversa.

from Stack_ import Stack


def invertir_palabra(palabra):
    pila_aux = Stack()
    palabra_invertida = ""

    for caracter in palabra:
        pila_aux.apilar(caracter)

    while pila_aux.tamanio() > 0:
        palabra_invertida += pila_aux.desapilar()

    return palabra_invertida


palabra = input("Ingrese una palabra que deseee invertir:")

print(f"La palabra {palabra} ha sido invertida con éxito.")
print(f"Resultado: {invertir_palabra(palabra)}")
