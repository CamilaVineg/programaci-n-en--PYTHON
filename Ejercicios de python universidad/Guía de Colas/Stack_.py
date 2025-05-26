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
