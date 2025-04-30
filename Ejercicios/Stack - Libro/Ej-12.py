""" 
    Dada una pila con nombres de los personajes de la saga de Star Wars, implemente una función
    que permita determinar si Leia Organa o Boba Fett están en dicha pila sin perder los datos.
"""

import sys
sys.path.append("./Clases")
from stack import Stack

stack = Stack()

stack.push("Luke Skywalker")
stack.push("Darth Vader")
stack.push("Leia Organa")
stack.push("Han Solo")
stack.push("Yoda")
stack.push("Obi-Wan Kenobi")
stack.push("Chewbacca")
stack.push("R2-D2")
stack.push("C-3PO")
stack.push("Rey")
stack.push("Kylo Ren")

def searcher(stack):
    aux_stack = Stack()
    found = False
    
    while stack.size() > 0:
        char = stack.pop()
        
        if char == "Leia Organa" or char == "Boba Fett": 
            found = True
            
    aux_stack.push(char)
    
    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

    return found

if searcher(stack):
    print("Leia Organa o Boba Fett están en la pila.")
else:
    print("Leia Organa o Boba Fett no están en la pila.")