# 10. Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone,
# de las cual se cuenta con la hora de la notificación, la aplicación que la emitió y el mensaje,
# resolver las siguientes actividades:
# a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
# b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya
# la palabra ‘Python’, si perder datos en la cola;
# c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las
# 11:43 y las 15:57, y determinar cuántas son.

from Queue_ import Cola
from datetime import datetime
from Stack_ import Pila

cola_notificaciones = Cola()

notificaciones = [
    {"hora": "11:00", "app": "Facebook", "mensaje": "Nuevo evento cerca de ti"},
    {"hora": "22:30", "app": "Twitter", "mensaje": "Tienes un nuevo seguidor"},
    {"hora": "14:30", "app": "Instagram", "mensaje": "Nueva historia disponible"},
    {"hora": "12:15", "app": "Facebook",
        "mensaje": "X cumple años hoy, ¡pasa y dale un saludo!"},
    {"hora": "19:01", "app": "Twitter", "mensaje": "Python es tendencia."},
]

for notif in notificaciones:
    cola_notificaciones.encolar(notif)

# a)


def eliminacion_facebook(cola_notificaciones):
    cola_aux = Cola()
    cont = 0
    while not cola_notificaciones.esta_vacia():
        notif = cola_notificaciones.desencolar()
        if notif["app"] == "Facebook":
            cont += 1
        else:
            cola_aux.encolar(notif)

    while not cola_aux.esta_vacia():
        cola_notificaciones.encolar(cola_aux.desencolar())

    return cont

# b)


def notificaciones_de_twitter(cola_notificaciones):
    cola_aux = Cola()

    while not cola_notificaciones.esta_vacia():
        notif = cola_notificaciones.desencolar()

        if notif["app"] == "Twitter" and "python" in notif["mensaje"].lower():
            print(notif)

        cola_aux.encolar(notif)

    while not cola_aux.esta_vacia():
        cola_notificaciones.encolar(cola_aux.desencolar())

    return None

# c)


def notif_dentro_del_horario(cola_notificaciones):
    cola_aux = Cola()
    pila_aux = Pila()
    cont = 0

    while not cola_notificaciones.esta_vacia():
        notif = cola_notificaciones.desencolar()

        hora_notif = datetime.strptime(notif["hora"], "%H:%M")
        inicio = datetime.strptime("11:43", "%H:%M")
        fin = datetime.strptime("15:57", "%H:%M")

        if inicio <= hora_notif <= fin:
            pila_aux.apilar(notif)
            cont += 1

        cola_aux.encolar(notif)

    while not cola_aux.esta_vacia():
        cola_notificaciones.encolar(cola_aux.desencolar())

    return cont


# Programa principal
print("A)) Eliminación de notificaciones de Facebook:")
cant_notis_face_eliminadas = eliminacion_facebook(cola_notificaciones)
print(
    f"Se han eliminado {cant_notis_face_eliminadas} notificaciones de Facebook con éxito\n")

print("B)) Notificaciones de Twitter que contienen la palabra 'Python':")
notificaciones_de_twitter(cola_notificaciones)
print()

print("C)) Notificaciones entre 11:43 y 15:57:")
cant_de_notificaciones_dentro_del_horario = notif_dentro_del_horario(
    cola_notificaciones)
print(
    f"Hay un total de {cant_de_notificaciones_dentro_del_horario} notificaciones en ese rango horario")
