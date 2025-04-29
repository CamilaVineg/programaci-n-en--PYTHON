# Implementar una función para calcular la potencia dado dos números enteros, el primero re-
# presenta la base y segundo el exponente.

def potencia(base, exponente):
    if exponente < 0:
        return 1/potencia(base, -exponente)
    elif exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)


base = int(input("ingrese un numero entero base: "))
exponente = int(input("ingrese la potencia entera de la base: "))

resultado = potencia(base, exponente)
print(f"el resultado de la potencia es {resultado}")
