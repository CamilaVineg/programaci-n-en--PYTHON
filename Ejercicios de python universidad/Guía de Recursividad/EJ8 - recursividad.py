# Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a siste-
# ma binario.


def decimal_a_binario(numero):
    if numero == 0:
        return ""
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)


# Programa principal
numero = int(input("Ingrese un número entero en decimal: "))

if numero == 0:
    print("El número binario es: 0")
else:
    resultado = decimal_a_binario(numero)
    print(f"El número binario es: {resultado}")
