"""Realizar un algoritmo que permita ingresar elementos en una pila, y que estos queden ordenados de forma creciente.
Solo puede utilizar una pila auxiliar como estructura extra (no se pueden utilizar métodos de ordenamiento).
"""

import sys

sys.path.append("./Clases")
from stack import Stack

element_stack = Stack()
aux_stack = Stack()

element_stack.push(6)
element_stack.push(3)
element_stack.push(2)
element_stack.push(5)
element_stack.push(4)
element_stack.push(1)


while element_stack.size() > 0:
    temp = element_stack.pop()

    while aux_stack.size() > 0 and aux_stack.on_top() > temp:
            element_stack.push(aux_stack.pop())

    aux_stack.push(temp)

while aux_stack.size() > 0:
    element_stack.push(aux_stack.pop())

print("Pila ordenada de forma creciente:")
element_stack.show()
