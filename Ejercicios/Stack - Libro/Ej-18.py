"""Dada una pila de objetos de una oficina de los que se dispone de su nombre y peso (por ejemplo monitor 1 kg,
teclado 0.25 kg, silla 7 kg, etc.), ordenar dicha pila de acuerdo a su peso –del objeto más liviano al más pesado–.
Solo pueden utilizar pilas auxiliares como estructuras extras, no se pueden utilizar métodos de ordenamiento.
"""

import sys

sys.path.append("./Clases")
from stack import Stack

object_stack = Stack()
aux_stack = Stack()

object_stack.push(("Monitor", 1.0))
object_stack.push(("Teclado", 0.25))
object_stack.push(("Silla", 7.0))
object_stack.push(("Mouse", 0.1))
object_stack.push(("Escritorio", 15.0))


while object_stack.size() > 0:
    e = object_stack.pop()
    
    while aux_stack.size() > 0 and aux_stack.on_top()[1] > e[1]:
        object_stack.push(aux_stack.pop())
        
    aux_stack.push(e)

while aux_stack.size() > 0:
    object_stack.push(aux_stack.pop())

print("Pila ordenada por peso:")
object_stack.show()
