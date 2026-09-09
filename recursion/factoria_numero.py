# autor: hugo San Juan
# Programa: calcula el factorial de un numero
# materia: Programación lógica y funcional

def factorial_iterativo(n):
    # Validamos que no sea un número negativo
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    
    resultado = 1
    # Multiplicamos todos los números desde 2 hasta n
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    
    # Caso base: el factorial de 0 o 1 es 1 (detiene la recursión)
    if n == 0 or n == 1:
        return 1
    
    # Caso recursivo: n! = n * (n-1)!
    return n * factorial_recursivo(n - 1)


if __name__ == "__main__":
    numero = int(input("Ingresa un número entero: "))
    print(f"Factorial (iterativo) de {numero} = {factorial_iterativo(numero)}")
    print(f"Factorial (recursivo) de {numero} = {factorial_recursivo(numero)}")