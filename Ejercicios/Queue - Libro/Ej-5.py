""" Utilizando operaciones de cola y pila, invertir el contenido de una pila. """

import sys
sys.path.append("./Clases")
from cola import Queue
from stack import Stack
from random import randint

queue = Queue()
stack = Stack()

for i in range(5):
    stack.push(randint(1,100))
    
print("Pila original: ")
stack.show()

while stack.size() > 0:
    queue.arrive(stack.pop())
    
while queue.size() > 0:
    stack.push(queue.attention())

print("Pila invertida: ")
stack.show()