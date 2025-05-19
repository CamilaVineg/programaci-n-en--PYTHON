# Dada una pila con los trajes de Iron Man utilizados en las películas de Marvel Cinematic Uni
# verse (MCU) de los cuales se conoce el nombre del modelo, nombre de la película en la que se
# usó y el estado en que quedó al final de la película (Dañado, Impecable, Destruido), resolver las siguientes actividades:
# a. determinar si el modelo Mark XLIV (Hulkbuster) fue utilizado en alguna de las películas,
# además mostrar el nombre de dichas películas;
# b. mostrar los modelos que quedaron dañados, sin perder información de la pila.
# c. eliminar los modelos de los trajes destruidos mostrando su nombre;
# d. un modelo de traje puede usarse en más de una película y en una película se pueden usar
# más de un modelo de traje, estos deben cargarse por separado;
# e. agregar el modelo Mark LXXXV a la pila, tener en cuenta que no se pueden cargar modelos
# repetidos en una misma película;
# f. mostrar los nombre de los trajes utilizados en las películas “Spider-Man: Homecoming” y
# “Capitan America: Civil War”.

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, datos: any):
        self.elementos.append(datos)

    def desapilar(self):
        if not self.esta_vacia():
            return self.elementos.pop()

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.elementos[-1]

    def tamaño(self):
        return len(self.elementos)

# programa principal


traje1 = {
    "modelo": "Mark III",
    "pelicula": "Iron Man",
    "estado": "Impecable"
}

traje2 = {
    "modelo": "Mark XLIV",
    "pelicula": "Avengers: Age of Ultron",
    "estado": "Dañado"
}

traje3 = {
    "modelo": "Mark L",
    "pelicula": "Avengers: Infinity War",
    "estado": "Destruido"
}

traje4 = {"modelo": "Mark XLIII",
          "pelicula": "El increible Hulk",
          "estado": "Dañado"}

traje5 = {"modelo": "Mark XLIV",
          "pelicula": "El increible Hulk",
          "estado": "Dañado"}

traje6 = {"modelo": "Mark XLVI",
          "pelicula": "Capitán América: Civil War",
          "estado": "Impecable"}

trajes_de_ironman = Pila()
trajes_de_ironman.apilar(traje1)
trajes_de_ironman.apilar(traje2)
trajes_de_ironman.apilar(traje3)
trajes_de_ironman.apilar(traje4)
trajes_de_ironman.apilar(traje5)
trajes_de_ironman.apilar(traje6)

# A)))
peliculas_con_Hulkbuster = []
pila_aux = Pila()

while not trajes_de_ironman.esta_vacia():
    traje = trajes_de_ironman.ver_tope()
    if traje["modelo"] == "Mark XLIV":
        peliculas_con_Hulkbuster.append(traje["pelicula"])

    trajes = trajes_de_ironman.desapilar()
    pila_aux.apilar(trajes)

while not pila_aux.esta_vacia():
    trajes_de_ironman.apilar(pila_aux.desapilar())

print("Películas donde se usó el Hulkbuster (Mark XLIV):")
for peli in peliculas_con_Hulkbuster:
    print(f"- {peli}")


# B)))

trajes_dañados = []
while not trajes_de_ironman.esta_vacia():
    traje = trajes_de_ironman.ver_tope()
    if traje["estado"] == "Dañado":
        trajes_dañados.append(traje["modelo"])

    trajes = trajes_de_ironman.desapilar()
    pila_aux.apilar(traje)

while not pila_aux.esta_vacia():
    trajes_de_ironman.apilar(pila_aux.desapilar())

print("\nModelos que quedaron dañados:")
for modelo in trajes_dañados:
    print(f"- {modelo}")

# C)))

while not trajes_de_ironman.esta_vacia():

    traje = trajes_de_ironman.desapilar()
    if traje["estado"] == "Destruido":
        print(f"modelo eliminado: ", traje["modelo"])
    else:
        pila_aux.apilar(traje)

while not pila_aux.esta_vacia():
    trajes_de_ironman.apilar(pila_aux.desapilar())

# E)))
existe = False
traje7 = {"modelo": "Mark LXXXV",
          "pelicula": "Avengers: Endgame",
          "estado": "Impecable"}

while not trajes_de_ironman.esta_vacia():
    traje = trajes_de_ironman.desapilar()
    if traje["modelo"] == "Mark LXXXV" and traje["pelicula"] == "Avengers: Endgame":
        existe = True
    else:
        pila_aux.apilar(traje)


while not pila_aux.esta_vacia():
    trajes_de_ironman.apilar(pila_aux.desapilar())


if existe:
    print("La wiki ya existe")
else:
    trajes_de_ironman.apilar(traje7)
    print("Ya se ha agregado la wiki del modelo Mark LXXXV")

# F)))
traje8 = {"modelo": "Mark XLVII",
          "pelicula": "Spider-Man: Homecoming",
          "estado": "Impecable"}

trajes_de_ironman.apilar(traje8)

trajes_usados = []

while not trajes_de_ironman.esta_vacia():
    traje = trajes_de_ironman.desapilar()
    if traje["pelicula"] == "Spider-Man: Homecoming" or traje["pelicula"] == "Capitán América: Civil War":
        trajes_usados.append(traje)

    pila_aux.apilar(traje)

while not pila_aux.esta_vacia():
    trajes_de_ironman.apilar(pila_aux.desapilar())

print("\nModelos usados en Spider-Man: Homecoming y Capitán América: Civil War:")
for traje in trajes_usados:
    print(f"- {traje['modelo']} ({traje['pelicula']})")
