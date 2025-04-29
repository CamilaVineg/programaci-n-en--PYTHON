# Dada una secuencia de caracteres, obtener dicha secuencia invertida.

def invertir_secuencia(secuencia):
    if len(secuencia) == 0:
        return ""
    else:
        return secuencia[-1] + invertir_secuencia(secuencia[:-1])


# Programa principal
texto = input("Ingrese una secuencia de caracteres: ")

resultado = invertir_secuencia(texto)
print(f"La secuencia invertida es: {resultado}")
