""" 
    Insertar el nombre de la diosa griega Atenea en la i-ésima posición debajo de la cima de una
    pila con nombres de dioses griegos.
"""

import sys
sys.path.append("./Clases")
from stack import Stack

stack = Stack()

stack.push("Zeus")
stack.push("Hades")
stack.push("Poseidón")
stack.push("Apolo")
stack.push("Hermes")

def insert_at_position(stack, name, i):
    aux_stack = Stack()
    
    for _ in range(i - 1):
        aux_stack.push(stack.pop())
        
    stack.push(name)
    
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())
        
    return stack
        
insert_at_position(stack, "Atenea", 4).show()