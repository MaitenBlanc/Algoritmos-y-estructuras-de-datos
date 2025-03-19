"""Dados dos valores A y B distintos, determinar cuál es el mayor."""

def mayor(a, b):
    if (a > b):
        return a
    else: 
        return b

a = int(input("Valor A: "))
b = int(input("Valor B: "))

if (a != b):
    print(f"El valor {mayor(a, b)} es mayor.")
else:
    print(f"Los valores ingresados son iguales.")