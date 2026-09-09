#autor hugo San Juan
#Programa que valida una matrícula escolar utilizando recursividad.
#materia: Programacion logica y funcional

import re

patron = r"^26115\d{3}$"


def validar_matricula():
    """Valida una matrícula utilizando recursividad."""

    matricula = input("Ingresa tu matrícula escolar: ")

    if re.fullmatch(patron, matricula):
        print("Matrícula válida.")
    else:
        print("Matrícula inválida.")
        print("El formato debe ser: 26115XXX.")
        validar_matricula()


# Programa principal
validar_matricula()