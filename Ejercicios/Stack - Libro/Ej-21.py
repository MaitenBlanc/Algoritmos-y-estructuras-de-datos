"""Realizar un algoritmo que ingrese en una pila los dos valores iniciales de la sucesión de Fibonacci –o condiciones 
de fin de forma recursiva– y a partir de estos calcular los siguientes valores de dicha sucesión, hasta obtener el 
valor correspondiente a un número n ingresado por el usuario."""

# Fibonacci --> F(n) = F(n-1) + f(n-2)

import sys

sys.path.append("./Clases")
from stack import Stack

fibonacci_stack = Stack()

def fibonacci_recursive(stack, n):
    # Ya se generó hasta F(n)
    if stack.size() >= n + 1:
        return

    last = stack.pop()
    second_last = stack.pop()

    next_value = last + second_last

    stack.push(second_last)
    stack.push(last)
    stack.push(next_value)

    fibonacci_recursive(stack, n)


n = int(input("Ingrese la posición n a calcular: "))

# Los dos primeros valores de Fibonacci
fibonacci_stack.push(0)
fibonacci_stack.push(1)

fibonacci_recursive(fibonacci_stack, n)

print(f"Términos de la sucesión de Fibonacci hasta F({n}):")
fibonacci_stack.show()
