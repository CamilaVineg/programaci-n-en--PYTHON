# Implementar una función para calcular el producto de dos números enteros dados.
def producto(numero1, numero2):

    if numero2 < 0:
        return -producto(numero1, -numero2)
    if numero1 < 0:
        return -producto(-numero1, numero2)

    if numero2 == 0 or numero1 == 0:
        return 0
    elif numero1 == 1:
        return numero2
    elif numero2 == 1:
        return numero1
    else:
        return numero1 + producto(numero1, numero2 - 1)


numero1 = int(input("ingrese un primer numero: "))
numero2 = int(input("ingrese un segundo numero: "))

resultado = producto(numero1, numero2)
print(f"el resultado del producto es {resultado}")
