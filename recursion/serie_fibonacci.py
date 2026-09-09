#autor: hugo San Juan
# Programa: genera la serie de Fibonacci
#materia: Programación lógica y funcional


def fibonacci(n):
    """Genera una lista con los primeros n números de Fibonacci."""
    serie = []
    a, b = 0, 1          # a = término actual, b = siguiente término
    for _ in range(n):
        serie.append(a)       # guardamos el término actual
        a, b = b, a + b       # avanzamos: 'a' toma el valor de 'b',
                               # y 'b' se convierte en la suma de ambos
    return serie


def fibonacci_termino(n):
    """Devuelve solo el n-ésimo término de Fibonacci (empezando en 0)."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    cantidad = int(input("¿Cuántos términos quieres generar? "))
    print(fibonacci(cantidad))