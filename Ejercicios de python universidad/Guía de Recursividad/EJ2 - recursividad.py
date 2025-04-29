# Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.
def suma_de_numeros(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma_de_numeros(numero-1)


numero = int(input("ingrese un numero entero positivo: "))
resultado = suma_de_numeros(numero)


print(
    f"El resultado de la suma de los numeros comprendidos entre 0 y {numero} es {resultado}")
