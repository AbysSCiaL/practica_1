"""
Determina el mayor de tres números ingresados por el teclado
"""
def ordenar_numeros(a, b, c):
    """Ordena tres números de menor a mayor y devuelve una tupla con el resultado."""
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

# Solicitar los números al usuario
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# Determinar el número mayor
mayor = max(numero1, numero2, numero3)

# Ordenar los números
ordenados = ordenar_numeros(numero1, numero2, numero3)

# Imprimir los resultados
print(f"Números ordenados: {ordenados[0]}, {ordenados[1]}, {ordenados[2]}")
print(f"El mayor es: {mayor}")