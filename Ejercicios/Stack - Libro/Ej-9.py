""" Resolver el problema del factorial de un número utilizando una pila. """

import sys
sys.path.append("./Clases")
from stack import Stack

stack = Stack()

def factorial(n):
    result = 1
    
    for i in range(n, 0, -1):
        stack.push(i)
    
    while stack.size() > 0:
        result *= stack.pop()
        
    return result

print(factorial(5))