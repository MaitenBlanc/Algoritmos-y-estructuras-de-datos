""" Dada una cola de valores enteros calcular su rango y contar cuántos elementos negativos hay. """

import sys
sys.path.append("./Clases")
from cola import Queue
from random import randint

queue_numbers = Queue()

for i in range(15):
    number = randint(-100, 100)
    queue_numbers.arrive(number)
    
queue_numbers.show()

max_value, min_value = queue_numbers.on_front(), queue_numbers.on_front()

negative_numbers = 0

while queue_numbers.size() > 0:
    number = queue_numbers.attention()
    if number < 0:
        negative_numbers += 1
        
    if number < min_value:
        min_value = number
        
    if number > max_value:
        max_value = number
        
print(f"Cantidad de negativos: {negative_numbers}")
print(f"El rango es {max_value - min_value}")