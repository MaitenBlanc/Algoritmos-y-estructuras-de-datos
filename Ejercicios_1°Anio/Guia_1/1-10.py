"""Escribir un programa que calcule el volumen de un cilindro. Para ello se deberá solicitar al
usuario que ingrese el radio y la altura. Mostrar el resultado por pantalla. volumen = π *
radio2 * altura."""

from math import pi

def volumen(radio, altura):
    vol = pi * (radio**2) * altura
    return vol

radio = float(input("Radio del cilindro: "))
altura = float(input("Altura del cilindro: "))

print(f"Volumen del cilindro = {volumen(radio, altura):.2f}")