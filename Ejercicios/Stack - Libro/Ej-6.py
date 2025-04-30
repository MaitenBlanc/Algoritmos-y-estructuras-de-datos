"""Leer una palabra y visualizarla en forma inversa."""

import sys
sys.path.append("./Clases")
from stack import Stack

stack = Stack()

def reverse(stack):
    inverted_word = ""
    # Poner caracteres del string en una pila
    for i in string:
        stack.push(i)
    
    while stack.size() > 0:
        inverted_word += stack.pop()

    return inverted_word
    
string = input("Ingrese una palabra: ")

print(f"Palabra original: {string}")
print(f"Palabra invertida: {reverse(stack)}")
