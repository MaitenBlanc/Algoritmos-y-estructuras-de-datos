"""Implementar una función que calcule la suma de todos los números enteros comprendidos
entre cero y un número entero positivo dado."""

# summ(n) = n + suma(n-1)  --> suma(0) = 0

def suma(num):
    if num == 0:
        return num
    else: 
        return num + suma(num - 1)

print(suma(5))