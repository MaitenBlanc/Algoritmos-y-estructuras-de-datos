""" Realizar un algoritmo que mantenga ordenado los elementos agregados a una cola, utilizando solo una cola 
como estructura auxiliar. """

import sys
sys.path.append("./Clases")
from cola import Queue
from random import randint

queue = Queue()
aux_queue = Queue()

for i in range(10):
    queue.arrive(i + 1)

def add_element(queue: Queue, element):
    while queue.size() > 0 and queue.on_front() < element:
        aux_queue.arrive(queue.attention())
    
    aux_queue.arrive(element)
    
    while queue.size() > 0:
        aux_queue.arrive(queue.attention())
        
    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())
        
    return queue

element = int(input("Ingrese elemento a agegar: "))

print("Cola ordenada: ")
add_element(queue, element).show()