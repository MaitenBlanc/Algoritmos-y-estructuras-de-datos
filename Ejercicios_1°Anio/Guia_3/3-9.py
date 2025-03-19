"""Dado el número matemático PI, se solicita al usuario que ingrese el valor del radio de una
circunferencia y calcule y muestre por pantalla el área y perímetro. (área = PI * radio2
perímetro = 2 * PI * radio."""

from math import pi; 

def area(radio):
    return pi * radio**2

def perimetro(radio):
    return 2 * pi * radio

radio = float(input("Ingrese el radio de la circunferencia: "))
print(f"El area de la circunferencia es: {area(radio):.2f}")
print(f"El perimetro de la circunferencia es: {perimetro(radio):.2f}")