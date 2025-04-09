"""Confeccionar un algoritmo tal que dados dos números enteros devuelva la suma de los
mismos, si se cumple que el primero es menor que el segundo, en caso contrario devolver
el producto de los mismos."""

def menor(n1, n2):
    return n1 < n2

def suma(n1, n2):
    return n1 + n2

def producto(n1, n2):
    return n1 * n2

n1 = int(input("Ingrese número 1: "))
n2 = int(input("Ingrese número 2: "))

if(menor(n1, n2)):
    sum = suma(n1, n2)
    print(f"Suma: {n1} + {n2} = {sum}")
else:
    prod = producto(n1, n2)
    print(f"Producto: {n1} * {n2} = {prod}")