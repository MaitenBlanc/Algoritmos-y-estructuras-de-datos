"""Dados dos números a y b, se desea intercambiar sus valores, utilizando una variable
auxiliar."""
    
a = int(input("Valor A: "))
b = int(input("Valor B: "))

# Método abreviado de python
a, b = b, a

print(f"Intercambio: A = {a} y B = {b}")