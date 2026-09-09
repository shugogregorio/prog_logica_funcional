# autor: hugo San Juan
# Programa: calcula el máximo común divisor (MCD) de dos números
# materia: Programación lógica y funcional

def mcd_recursivo(a, b):
    # Caso base: si b es 0, a es el MCD
    if b == 0:
        return a
    # Caso recursivo: mcd(a, b) = mcd(b, a % b)
    return mcd_recursivo(b, a % b)

# Ejemplo de uso
num1 = 48
num2 = 18
resultado = mcd_recursivo(num1, num2)
print(f"El MCD de {num1} y {num2} es: {resultado}")