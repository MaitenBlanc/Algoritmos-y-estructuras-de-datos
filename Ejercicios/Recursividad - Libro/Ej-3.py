"""Implementar una función para calcular el producto de dos números enteros dados."""

# producto(n1, n2) = n1 + ... + n1  --> n2 veces

def producto(num1, num2):
    if num2 == 0:
        return 0
    else:
        return num1 + producto(num1, num2 - 1)
    
print(producto(4, 3))