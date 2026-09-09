

#autor hugo San Juan
#Programa que valida un correo electrónico.
#materia: Programacion logica y funcional

import re

def validar_correo_detallado(correo):
    """
    Valida el correo y devuelve un mensaje explicando el resultado.
    """
    if not correo:
        return False, "El correo no puede estar vacío."

    if correo.count('@') != 1:
        return False, "El correo debe contener exactamente un símbolo @."

    local, dominio = correo.split('@')

    if not local:
        return False, "La parte antes del @ no puede estar vacía."

    if local.startswith('.') or local.endswith('.'):
        return False, "La parte local no puede empezar ni terminar con punto."

    if '..' in local:
        return False, "La parte local no puede tener dos puntos seguidos."

    patron = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

    if re.match(patron, correo):
        return True, "Tu Correo electrónico es válido."
    else:
        return False, "El formato del correo no es válido."


def main():
    print("=== VALIDADOR DE CORREO ELECTRÓNICO ===\n")

    while True:
        correo = input("Ingresa tu correo electrónico (o escribe 'salir' para terminar): ").strip()

        if correo.lower() == "salir":
            print("¡Hasta luego!")
            break

        valido, mensaje = validar_correo_detallado(correo)

        if valido:
            print(f" {mensaje}\n")
        else:
            print(f" {mensaje} Intenta de nuevo.\n")


if __name__ == "__main__":
    main()