# 9. Resolver el problema del factorial de un número utilizando una pila.
from Stack_ import Stack
pila_factorial = Stack()
# Solicitando al usuario un número para calcular su factorial
numero = int(input("Ingrese un número para calcular su factorial: "))

for n in range(numero):
    pila_factorial.apilar(numero-n)


def calcular_factorial(pila_factorial):
    resultado = 0
    while pila_factorial.tamanio() > 0:
        valor = pila_factorial.desapilar()
        if valor > 0:
            resultado *= valor

    return resultado


factorial = calcular_factorial(pila_factorial)
print(f"El factorial de {numero} es: {factorial}")
