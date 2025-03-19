"""Hallar el área de un cuadrado, cuyos lados tienen la longitud de la hipotenusa de un
triángulo rectángulo y cuyos catetos son dados."""

from math import sqrt

def calculo_hipotenusa(cat_1, cat_2):
    hipotenusa = sqrt(cat_1**2 + cat_2**2)
    return hipotenusa

def area_cuadrado():
    lado = calculo_hipotenusa(cat_1, cat_2)
    area = lado*lado
    return area

cat_1 = float(input("Cateto 1 del triángulo: "))
cat_2 = float(input("Cateto 2 del triángulo: "))
    
print(f"Área del cuadrado de lado {calculo_hipotenusa(cat_1, cat_2):.2f} = {area_cuadrado():.2f}")