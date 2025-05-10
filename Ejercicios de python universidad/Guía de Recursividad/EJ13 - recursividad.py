# Desarrollar el algoritmo de Euclides para calcular también el mínimo común múltiplo (MCM)
# de dos número entero.
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(b, a % b)


def mcm(a, b):
    # MCM usando la fórmula MCM(a, b) = |a * b| / MCD(a, b)
    return abs(a * b) // mcd(a, b)


# Programa principal
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

resultado_mcd = mcd(num1, num2)
resultado_mcm = mcm(num1, num2)

print(f"El MCD de {num1} y {num2} es: {resultado_mcd}")
print(f"El MCM de {num1} y {num2} es: {resultado_mcm}")
