# 12. Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
# que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.

from Stack_ import Stack


def buscar_personaje(pila_de_personajes):
    result1 = False
    result2 = False
    pila_aux = Stack()
    while pila_de_personajes.tamanio() > 0:

        personaje = pila_de_personajes.desapilar()
        if personaje == "Leia Organa":
            result1 = True

        if personaje == "Boba Fett":
            result2 = True

        pila_aux.apilar(personaje)

    while pila_aux.tamanio() > 0:
        pila_de_personajes.apilar(pila_aux.desapilar())

    return result1, result2


pila_de_personajes = Stack()

personajes_star_wars = [
    "Luke Skywalker",
    "Leia Organa",
    "Han Solo",
    "Darth Vader",
    "Boba Fett",
    "Yoda",
    "Obi-Wan Kenobi",
    "Chewbacca",
    "R2-D2",
    "C-3PO",
    "Padmé Amidala",
    "Anakin Skywalker"
]

for pers in personajes_star_wars:
    pila_de_personajes.apilar(pers)

Leia_se_encuentra, Boba_se_encuentra = buscar_personaje(pila_de_personajes)

print("Esta es la pila de personajes de Star Wars:")
pila_de_personajes.mostrar()
print("----")
print("Determinando si Leia Organa o Boba Fett se encuentran en la pila...")
print("----")
if Leia_se_encuentra:
    print("✅ Leia Organa se encuentra en la pila.")
else:
    print("❌ Leia Organa no se encuentra en la pila.")

if Boba_se_encuentra:
    print("✅ Boba Fett se encuentra en la pila.")
else:
    print("❌ Boba Fett no se encuentra en la pila.")
