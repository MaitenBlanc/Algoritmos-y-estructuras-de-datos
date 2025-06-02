"""Realizar el algoritmo de ordenamiento quicksort de manera que funcione iterativamente."""

import sys

sys.path.append("./Clases")
from stack import Stack

element_stack = Stack()

def quicksort(stack):
    aux_stack = Stack()

    while stack.size() > 0:
        temp = stack.pop()

        while aux_stack.size() > 0 and aux_stack.on_top() > temp:
            stack.push(aux_stack.pop())

        aux_stack.push(temp)

    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())


element_stack.push(6)
element_stack.push(3)
element_stack.push(2)
element_stack.push(5)
element_stack.push(4)
element_stack.push(1)

quicksort(element_stack)

print("Pila ordenada de forma ascendente: ")
element_stack.show()