""" Dada una secuencia de caracteres utilizando operaciones de cola y pila determinar si es un palíndromo. """

import sys
sys.path.append("./Clases")
from cola import Queue
from stack import Stack

queue = Queue()
stack = Stack()
is_palindrome = True

sequence = input("Ingrese una secuencia de caracteres: ")

for char in sequence:
    queue.arrive(char)
    stack.push(char)
    
while queue.size() > 0 and stack.size() > 0:
    if queue.attention() != stack.pop():
        is_palindrome = False
        break

if is_palindrome:
    print("La secuencia es palíndromo.")
else:
    print("La secuencia no es palíndromo.")