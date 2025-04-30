"""Invertir el contenido de una pila, solo puede utilizar una pila auxiliar como estructura extra."""

import sys
sys.path.append("./Clases")
from stack import Stack
from random import randint

number_stack = Stack()
aux_stack = Stack()

for i in range(5):
    rand_number = randint(1, 100)
    number_stack.push(rand_number)
    
def reverse(number_stack):
    while number_stack.size() > 0:
        aux_stack.push(number_stack.pop())

    aux_stack.show()

        
print("Pila original: ")
number_stack.show()

print("Pila invertida: ")
reverse(number_stack)
