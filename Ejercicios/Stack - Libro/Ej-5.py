"""Determinar si una cadena de caracteres es un palíndromo."""

import sys
sys.path.append("./Clases")
from stack import Stack

stack = Stack()

def es_palindromo(string):
    # Poner caracteres del string en una pila
    for i in string:
        stack.push(i)
        
    # Comparar caracteres
    for i in string:
        if i != stack.pop():
            return False
    
    return True

string = input("Ingrese una palabra: ")

if es_palindromo(string):
    print(f"{string} es palíndromo.")
else:
    print(f"{string} no es palíndromo.")
    
