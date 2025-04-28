# 5. Desarrollar una función que permita convertir un número romano en un número decimal.
def romano_a_decimal(romano):
    # Se crea un diccionario para que el programa sepa identificar cuales son los valores que le correspondan
    valores = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    if not romano:
        return 0

    if len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] >= valores[romano[1]]:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
    else:
        return valores[romano[1]] - valores[romano[0]] + romano_a_decimal(romano[2:])


# Ejemplo de uso
print(romano_a_decimal(""))  # Salida: 0
print(romano_a_decimal("MM"))  # Salida: 2000
print(romano_a_decimal("XII"))  # salida 12
