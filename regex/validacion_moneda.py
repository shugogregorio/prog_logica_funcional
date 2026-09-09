#autor hugo San Juan
#Programa que valida un dato monetario con cinco dígitos y opcionalmente uno o dos decimales.
#materia: Programacion logica y funcional

import re

# Cinco dígitos y opcionalmente uno o dos decimales
patron = r"^\d{5}(\.\d{1,2})?$"


def validar_moneda():
    """Solicita y valida un dato monetario mediante un ciclo."""

    while True:
        moneda = input("Ingresa el dato moneda (#####.##): ")

        if re.fullmatch(patron, moneda):
            print("Dato moneda válido.")
            break
        else:
            print("Dato moneda inválido. Intenta nuevamente.")


# Programa principal
validar_moneda()