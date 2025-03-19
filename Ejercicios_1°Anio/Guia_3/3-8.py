"""Escribir un programa que lea dos números enteros A y B, y obtenga los valores A div B, A
mod B."""

def calculo_div(a, b):
    div = a // b
    return div

def calculo_mod(a, b):
    mod = a % b
    return mod

a = int(input("Valor A: "))
b = int(input("Valor B: "))

print(f"Div {a} y {b} = {calculo_div(a, b):.2f}")
print(f"Mod {a} y {b} = {calculo_mod(a, b):.2f}")