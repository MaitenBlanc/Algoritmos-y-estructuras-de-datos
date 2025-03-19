"""Leer tres números de a uno por vez, calcular su suma y su producto."""

def calculo_suma(n1, n2, n3):
    suma = n1 + n2 + n3
    return suma

def calculo_producto(n1, n2, n3):
    producto = n1 * n2 * n3
    return producto

n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))

print(f"Suma {n1} + {n2} + {n3} = {calculo_suma(n1, n2, n3):.2f}")
print(f"Producto {n1} * {n2} * {n3} = {calculo_producto(n1, n2, n3):.2f}")