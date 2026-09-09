#autor hugo San Juan
#Programa que valida un nombre utilizando recursividad.
#materia: Programacion logica y funcional


import re

patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$"


def validar_nombre():
    """Valida un nombre utilizando recursividad."""

    nombre = input("Ingresa tu nombre: ")

    if re.fullmatch(patron, nombre):
        print("Nombre válido.")
    else:
        print("Nombre inválido.")
        print("Solo se permiten letras y espacios.")
        validar_nombre()


# Programa principal
validar_nombre()