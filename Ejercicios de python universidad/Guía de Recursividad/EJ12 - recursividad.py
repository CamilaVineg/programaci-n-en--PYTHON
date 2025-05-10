# Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos
# número entero.

def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


# Programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado = mcd(abs(num1), abs(num2))
print(f"El MCD de {num1} y {num2} es: {resultado}")
