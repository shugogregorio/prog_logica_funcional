
#autor hugo San Juan
#Programa que valida un número telefónico con formato internacional.
#materia: Programacion logica y funcional

import re

# Diccionario de prefijos: código país -> nombre y longitud esperada del número local
PREFIJOS = {
    "+52": {"nombre": "México", "min": 10, "max": 10},
    "+1":  {"nombre": "EE.UU./Canadá", "min": 10, "max": 10},
    "+34": {"nombre": "España", "min": 9, "max": 9},
    "+54": {"nombre": "Argentina", "min": 10, "max": 11},
    "+57": {"nombre": "Colombia", "min": 10, "max": 10},
    "+51": {"nombre": "Perú", "min": 9, "max": 9},
    "+56": {"nombre": "Chile", "min": 9, "max": 9},
}

# Ordenamos los prefijos de más largo a más corto para evitar falsos positivos
# (ej. que "+1" coincida antes de comprobar un prefijo de 3 dígitos)
PREFIJOS_ORDENADOS = sorted(PREFIJOS.keys(), key=len, reverse=True)


def limpiar_numero(numero: str) -> str:
    """
    Elimina espacios, guiones, paréntesis y otros caracteres no numéricos,
    pero conserva el símbolo '+' inicial si existe.
    """
    numero = numero.strip()
    # Regex: conserva '+' solo si está al inicio, y todos los dígitos
    numero_limpio = re.sub(r'[^\d+]', '', numero)
    return numero_limpio


def validar_telefono(numero: str):
    """
    Valida un número telefónico según su prefijo y cantidad de dígitos.
    Retorna una tupla (es_valido: bool, mensaje: str)
    """
    numero_limpio = limpiar_numero(numero)

    # Validar formato general: debe empezar con '+' seguido solo de dígitos
    if not re.match(r'^\+\d+$', numero_limpio):
        return False, "El número debe iniciar con '+' seguido del código de país y dígitos"

    # Buscar el prefijo correspondiente
    prefijo_encontrado = None
    for prefijo in PREFIJOS_ORDENADOS:
        if numero_limpio.startswith(prefijo):
            prefijo_encontrado = prefijo
            break

    if prefijo_encontrado is None:
        return False, "Prefijo de país no reconocido"

    datos_pais = PREFIJOS[prefijo_encontrado]
    resto = numero_limpio[len(prefijo_encontrado):]

    # Validar longitud del número local
    if not (datos_pais["min"] <= len(resto) <= datos_pais["max"]):
        if datos_pais["min"] == datos_pais["max"]:
            esperado = f"{datos_pais['min']} dígitos"
        else:
            esperado = f"entre {datos_pais['min']} y {datos_pais['max']} dígitos"
        return False, f"Número inválido para {datos_pais['nombre']}: se esperan {esperado}, se recibieron {len(resto)}"

    return True, f"Número válido ({datos_pais['nombre']}): {prefijo_encontrado} {resto}"


def main():
    print("=== Validador de números telefónicos ===")
    print("Escribe 'salir' para terminar.\n")

    while True:
        entrada = input("Ingresa un número telefónico (con código de país, ej. +52 55 1234 5678): ")
        if entrada.lower() == "salir":
            print("¡Hasta luego!")
            break

        valido, mensaje = validar_telefono(entrada)
        estado = " VÁLIDO" if valido else " INVÁLIDO"
        print(f"{estado}: {mensaje}\n")


if __name__ == "__main__":
    main()