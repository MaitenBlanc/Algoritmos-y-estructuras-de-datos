""" Utilizando operaciones de cola y pila, invertir el contenido de una cola. """

import sys
sys.path.append("./Clases")
from cola import Queue
from stack import Stack
from random import randint

queue = Queue()
stack = Stack()

for i in range(5):
    queue.arrive(randint(1, 10))

print("Cola original: ")
queue.show()

while queue.size() > 0:
    stack.push(queue.attention())
    
while stack.size() > 0:
    queue.arrive(stack.pop())

print("Cola invertida: ")
queue.show()