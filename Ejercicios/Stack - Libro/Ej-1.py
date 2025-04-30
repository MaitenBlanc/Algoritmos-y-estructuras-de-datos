"""Determinar el número de ocurrencias de un determinado elemento en una pila."""
import sys
sys.path.append("./Clases")
from stack import Stack
from random import randint

number_stack = Stack()
for i in range(10):
    rand_number = randint(1, 100)
    print(rand_number)
    number_stack.push(rand_number)
    
def occurrences_counter(number_stack, element):
    aux_stack = Stack()
    counter = 0
    
    # Contar cantidad uno a uno y apilar en pila auxiliar
    while number_stack.size() > 0:
        value = number_stack.pop()
        if value == element:
            counter += 1
        aux_stack.push(value)
        
    # Desapilar de pila auxiliar y volver a apilar en la pila original
    while aux_stack.size() > 0:
        number_stack.push(aux_stack.pop())
        
    return counter


element = int(input("Ingrese el numero a buscar: "))

occurrences = occurrences_counter(number_stack, element)

print(f"Veces que se encuentra el valor {element} en la pila: {occurrences}")