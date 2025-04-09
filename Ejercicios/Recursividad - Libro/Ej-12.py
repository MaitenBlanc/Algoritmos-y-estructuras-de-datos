"""Desarrollar el algoritmo de Euclides para calcular el máximo común divisor (MCD) de dos número entero."""

def mcd(num1, num2):
    if num2 == 0:
        return abs(num1)
    else:
        return mcd(num2, num1 % num2)
    
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print(f"MCD de {num1} y {num2} = {mcd(num1, num2)}")