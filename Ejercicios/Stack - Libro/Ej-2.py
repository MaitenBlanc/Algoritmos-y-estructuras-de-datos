"""Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares."""

import sys
sys.path.append("./Clases")
from stack import Stack
from random import randint

number_stack = Stack()

for i in range(10):
    rand_number = randint(1, 100)
    number_stack.push(rand_number)

def odd_numbers(number_stack):
    aux_stack = Stack()
    
    while number_stack.size() > 0:
        value = number_stack.pop()
        if value % 2 == 0:
            aux_stack.push(value)
            
    while aux_stack.size() > 0:
        number_stack.push(aux_stack.pop())

print("Pila original: ")
number_stack.show()

odd_numbers(number_stack)

print("Pila de números pares: ")
number_stack.show()