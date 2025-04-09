"""Dados dos números si el primero es divisible por el segundo mostrar un mensaje que así
lo indique."""

def divisible(n1, n2):
    if (n1 % n2 == 0):
        return True
    else:
        return False

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

if (divisible(n1, n2)):
    print(f"{n1} es divisible por {n2}")
else:
    print(f"{n1} no es divisible por {n2}")