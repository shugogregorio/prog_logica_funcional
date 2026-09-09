#autor: hugo San Juan
# Programa: calcula la potencia de un numero
#materia: Programación lógica y funcional


def calcular_potencia(base, exponente):
    # El operador ** eleva 'base' a la potencia 'exponente'
    # Funciona con números enteros, decimales, negativos, etc.
    return base ** exponente

# Solicitamos los datos al usuario
# float() permite ingresar tanto números enteros como decimales
base = float(input("Ingresa la base: "))
exponente = float(input("Ingresa el exponente: "))

# Llamamos a la función y guardamos el resultado
resultado = calcular_potencia(base, exponente)

# Mostramos el resultado usando un f-string (formato moderno de Python)
print(f"{base} elevado a {exponente} es igual a {resultado}")