"""Desarrollar un algoritmo que permita realizar la suma de los dígitos de un número entero, no
se puede convertir el número a cadena."""

def sumar(num):
    num = abs(num)
    
    if num < 10: 
        return num
    else: 
        return num % 10 + sumar(num // 10)
    
num = int(input("Ingrese un número: "))
print(f"Suma de los dígitos de {num} = {sumar(num)}")