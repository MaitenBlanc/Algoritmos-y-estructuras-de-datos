"""Reemplazar todas las ocurrencias de un determinado elemento en una pila."""

import sys
sys.path.append("./Clases")
from stack import Stack
from random import randint

number_stack = Stack()

for i in range(10):
    rand_number = randint(1, 100)
    number_stack.push(rand_number)

def replace_occurrences(number_stack, element1, element2):
    aux_stack = Stack()
    while number_stack.size() > 0:
        value = number_stack.pop()
        if value == element1: 
            aux_stack.push(element2)
        else:
            aux_stack.push(value)
    
    while aux_stack.size() > 0:
        number_stack.push(aux_stack.pop())
            
print("Pila original: ")
number_stack.show()

element1 = int(input("Ingrese elemento que quiere modificar: "))
element2 = int(input("Ingrese elemento nuevo: "))

replace_occurrences(number_stack, element1, element2)

print("Pila modificada: ")
number_stack.show()