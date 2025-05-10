# Desarrollar un algoritmo que invierta un número entero sin convertirlo a cadena.
def invertir_numero(numero, invertido=0):
    if numero == 0:
        return invertido
    else:
        return invertir_numero(numero // 10, invertido * 10 + numero % 10)


# Programa principal
numero = int(input("Ingrese un número entero: "))
numero_absoluto = abs(numero)
resultado = invertir_numero(numero_absoluto)

# Si era negativo, devolvemos negativo
if numero < 0:
    resultado = -resultado

print(f"El número invertido es: {resultado}")
