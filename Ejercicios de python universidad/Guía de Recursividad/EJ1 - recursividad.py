# Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Ejemplo de uso
num = int(input("Ingrese un número entero no negativo: "))
resultado = fibonacci(num)
print(f"El término {num} de la sucesión de Fibonacci es {resultado}")
