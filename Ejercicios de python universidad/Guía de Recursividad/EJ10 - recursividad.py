# Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.

def conteo_de_digitos(numero):
    numero = abs(numero)
    if numero < 10:
        return 1
    else:
        return 1 + conteo_de_digitos(numero // 10)


numero = int(input("Ingrese un número entero: "))
cantidad = conteo_de_digitos(numero)

print(f"La cantidad de dígitos de {numero} es: {cantidad}")
