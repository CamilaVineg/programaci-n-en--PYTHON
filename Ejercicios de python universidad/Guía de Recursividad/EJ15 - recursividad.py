# Desarrollar una función que permita calcular la raíz cuadrada entera de un número entero.
# Puede utilizar una función auxiliar para que la función principal solo reciba como parámetro
# el número a calcular su raíz.

def raiz_cuadrada_entera(n):
    def buscar_raiz(n, candidato):
        if candidato * candidato > n:
            return candidato - 1
        else:
            return buscar_raiz(n, candidato + 1)

    if n < 0:
        raise ValueError(
            "No se puede calcular la raíz cuadrada de un número negativo.")
    return buscar_raiz(n, 0)


# Programa principal
numero = int(input("Ingrese un número entero: "))
resultado = raiz_cuadrada_entera(numero)
print(f"La raíz cuadrada entera de {numero} es: {resultado}")
