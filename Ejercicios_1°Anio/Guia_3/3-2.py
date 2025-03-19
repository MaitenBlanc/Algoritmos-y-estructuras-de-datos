"""Dadas las longitudes de los dos catetos de un triángulo rectángulo, hallar la longitud de la
hipotenusa."""

from math import sqrt

def hipotenusa(cat_1, cat_2):
    hip = sqrt(cat_1**2 + cat_2**2)
    return hip

cat_1 = float(input("Cateto 1: "))
cat_2 = float(input("Cateto 2: "))

print(f"Hipotenusa de triángulo con {cat_1} y {cat_2} = {hipotenusa(cat_1, cat_2):.2f}")