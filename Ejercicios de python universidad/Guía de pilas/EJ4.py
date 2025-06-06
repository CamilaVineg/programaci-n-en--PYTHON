# 4. Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra.

from Stack_ import Stack


def invertir(epic_el_musical, pila_invertida):

    while epic_el_musical.tamanio() > 0:
        pila_invertida.apilar(epic_el_musical.desapilar())

    return pila_invertida


pila_invertida = Stack()
epic_el_musical = Stack()

personajes = ["Odysseus", "Penelope", "Telemacus", "Poseidon",
              "Zeus", "Circe", "Hermes", "Atenea", "Polites"]

for pers in personajes:
    epic_el_musical.apilar(pers)

invertir(epic_el_musical, pila_invertida)

print("La Lista de personajes de Epic The Musical se ha invertido con éxito.")

pila_invertida.mostrar()
