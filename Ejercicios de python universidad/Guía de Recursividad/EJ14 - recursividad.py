# Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
# se puede convertir el número a cadena.

def suma_de_digitos(numero):
    if numero < 0:
        numero = -numero  # Trabajamos con valor absoluto si es negativo

    if numero == 0:
        return 0
    else:
        return (numero % 10) + suma_de_digitos(numero // 10)


numero = int(input("Ingrese un número entero: "))
resultado = suma_de_digitos(numero)

print(f"La suma de los dígitos del número es: {resultado}")
