
print("Calculadora Básica")
print("Para salir, ingrese n")

numero = ""

while True:

    if not numero:
        numero = input("Ingrese un numero: ")
        if numero.lower() == "n":
            break
        numero = int(numero)
    operacion = input("ingrese una operacion(suma,resta,mult,div): ")
    if operacion.lower() == "n":
        break
    numero2 = input("ingresa siguiente numero: ")
    if numero2.lower() == "n":
        break
    numero2 = int(numero2)

    if operacion.lower() == "suma":
        numero += numero2
    elif operacion.lower() == "resta":
        numero -= numero2
    elif operacion.lower() == "mult":
        numero *= numero2
    elif operacion.lower() == "div":
        numero /= numero2
    else:
        print("lo ingresado no es valido, vuelva a intentarlo")
        break

    print(f"El resultado es: {numero}")
