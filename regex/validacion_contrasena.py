#autor hugo San Juan
#Programa que valida una contraseña con criterios de seguridad.
#materia: Programacion logica y funcional

import re

def validar_contrasena(contrasena: str) -> tuple[bool, list[str]]:
    """
    Valida que una contraseña cumpla con criterios de seguridad.
    Retorna (es_valida, lista_de_errores)
    """
    errores = []

    # 1. Longitud mínima
    if len(contrasena) < 8:
        errores.append("Debe tener al menos 8 caracteres.")

    # 2. Al menos una mayúscula
    if not re.search(r"[A-Z]", contrasena):
        errores.append("Debe contener al menos una letra mayúscula.")

    # 3. Al menos una minúscula
    if not re.search(r"[a-z]", contrasena):
        errores.append("Debe contener al menos una letra minúscula.")

    # 4. Al menos un número
    if not re.search(r"[0-9]", contrasena):
        errores.append("Debe contener al menos un número.")

    # 5. Al menos un carácter especial
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", contrasena):
        errores.append("Debe contener al menos un carácter especial (!@#$%, etc.).")

    # 6. Sin espacios en blanco
    if re.search(r"\s", contrasena):
        errores.append("No debe contener espacios en blanco.")

    # 7. No debe ser una secuencia común/débil
    comunes = ["123456", "password", "qwerty", "contraseña", "12345678"]
    if contrasena.lower() in comunes:
        errores.append("La contraseña es demasiado común/débil.")

    es_valida = len(errores) == 0
    return es_valida, errores


def main():
    print("=== Validador de contraseñas ===")
    print("Escribe 'salir' en cualquier momento para terminar.\n")

    while True:
        contrasena = input("Ingresa tu contraseña: ")

        if contrasena.strip().lower() == "salir":
            print("Programa finalizado. ¡Hasta luego!")
            break

        es_valida, errores = validar_contrasena(contrasena)

        if es_valida:
            print( "Contraseña segura.\n")
        else:
            print(" Contraseña no válida. Motivos:")
            for error in errores:
                print(f"  - {error}")
            print()  # línea en blanco para separar intentos


if __name__ == "__main__":
    main()