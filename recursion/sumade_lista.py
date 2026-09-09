# autor: hugo San Juan
# Programa: suma los numeros de una lista
# materia: Programación lógica y funcional

def sumar_lista(numeros): #se define la funcion sumar_lista que recibe una lista de numeros como parametro
    total = 0
    for numero in numeros: #se recorre cada numero en la lista de numeros
        total += numero
    return total #retorna el total de la suma de los numeros en la lista

# Ejemplo de uso
mi_lista = [10, 25, 3, 47, 8]
resultado = sumar_lista(mi_lista) #resultado almacena el valor retornado por la funcion sumar_lista al pasarle mi_lista como argumento
print(mi_lista) # imprime la lista de numeros
print(f"La suma de los números es: {resultado}")