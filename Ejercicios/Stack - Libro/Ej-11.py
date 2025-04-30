""" Dada una pila de letras determinar cuántas vocales contiene. """

import sys
sys.path.append("./Clases")
from stack import Stack

stack = Stack()

stack.push("c")
stack.push("a")
stack.push("f")
stack.push("j")
stack.push("e")
stack.push("h")
stack.push("m")
stack.push("i")

def count_vowels(stack):
    aux_stack = Stack()
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    
    while stack.size() > 0:
        letter = stack.pop()
        
        if letter in vowels:
            count += 1
        
        aux_stack.push(letter)
        
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())
        
    return count

print(f"Cantidad de vocales de la pila: {count_vowels(stack)}")