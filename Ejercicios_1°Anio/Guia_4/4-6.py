"""Dados dos números si el primero es divisible por el segundo intercambiarlos."""

def esDivisible(n1, n2):
    return n1 % n2 == 0
    
def intercambio(n1, n2):
    if esDivisible(n1, n2):
        return n2, n1
    return n1, n2

n1 = int(input("Ingrese valor 1: "))
n2 = int(input("Ingrese valor 2: "))


if (esDivisible(n1, n2)):
    n1, n2 = intercambio(n1,n2)
    print(f"Valores después del intercambio: n1 = {n1}, n2 = {n2}")
else: 
    print(f"{n1} no es divisible por {n2}, no se pueden intercambiar.")