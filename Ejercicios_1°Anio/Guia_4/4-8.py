"""Dados tres números enteros positivos, determinar cuál es el mayor."""

def mayor(n1, n2, n3):
    if (n1 > n2 and n1 > n3):
        return n1
    elif (n2 > n1 and n2 > n3):
        return n2
    else:
        return n3

n1 = int(input("Ingrese número 1: "))
n2 = int(input("Ingrese número 2: "))
n3 = int(input("Ingrese número 3: "))

print(f"El número mayor entre {n1}, {n2} y {n3} es {mayor(n1,n2,n3)}")