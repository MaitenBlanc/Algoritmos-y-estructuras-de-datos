"""Eliminar el i-ésimo elemento debajo de la cima de una pila de palabras."""

import sys
sys.path.append("./Clases")
from stack import Stack

stack = Stack()

def remove(stack, i):
    if i < 0 or i >= stack.size():
        print(f"Indice inválido: {i}")
        return
    
    aux_stack = Stack()
    count = 0
    
    while count < i:
        aux_stack.push(stack.pop())
        count += 1
        
    removed = stack.pop()
    print(f"Elemento eliminado: {removed}")
    
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

stack.push("cinco")
stack.push("cuatro")
stack.push("tres")
stack.push("dos")
stack.push("uno")
        
print("Pila original: ")
stack.show()

remove(stack, 3)

print("Pila sin el i-ésimo elemento: ")
stack.show()