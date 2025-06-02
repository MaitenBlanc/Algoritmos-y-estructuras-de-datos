"""Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos episodios.
"""

import sys

sys.path.append("./Clases")
from stack import Stack

stack_ep_v = Stack()
stack_ep_vii = Stack()

stack_ep_v.push("Luke")
stack_ep_v.push("Leia")
stack_ep_v.push("Han Solo")
stack_ep_v.push("Yoda")
stack_ep_v.push("Darth Vader")

stack_ep_vii.push("Rey")
stack_ep_vii.push("Finn")
stack_ep_vii.push("Leia")
stack_ep_vii.push("Han Solo")
stack_ep_vii.push("Kylo Ren")

def intersection(stack_v, stack_vii):
    aux1 = Stack()
    aux2 = Stack()
    intersect = Stack()

    while stack_v.size() > 0:
        char1 = stack_v.pop()
        aux1.push(char1)

        found = False
        
        while stack_vii.size() > 0:
            char2 = stack_vii.pop()
            aux2.push(char2)

            if char2 == char1:
                found = True

        if found: 
            intersect.push(char1)

        while aux2.size() > 0:
            stack_vii.push(aux2.pop())

    while aux1.size() > 0:
        stack_v.push(aux1.pop())

    return intersect

intersect = intersection(stack_ep_v, stack_ep_vii)

print("Intersección: ")
intersect.show()
