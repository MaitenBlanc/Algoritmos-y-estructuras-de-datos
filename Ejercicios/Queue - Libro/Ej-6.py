""" 
    Contar la cantidad de ocurrencias de un determinado elemento en una cola, sin utilizar ninguna estructura 
    auxiliar. 
"""

import sys
sys.path.append("./Clases")
from cola import Queue
from random import randint

queue = Queue()

for i in range(10):
    queue.arrive(randint(1,10))

def element_counter(queue: Queue, n):
    counter = 0
    
    for i in range(queue.size()):
        if queue.move_to_end() == n:
            counter += 1

    return counter
    
print("Cola: ")
queue.show()

print(f"Cantidad de 7 en la cola: {element_counter(queue, 7)}")