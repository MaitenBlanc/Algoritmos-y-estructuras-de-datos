""" Eliminar el i-ésimo elemento después del frente de la cola. """

import sys
sys.path.append("./Clases")
from cola import Queue
from random import randint

queue = Queue()

for i in range(10):
    queue.arrive(randint(1,10))
    
print("Cola original: ")
queue.show()

n = int(input("Ingrese la posición del elemento a eliminar: "))

def delete_i(queue: Queue, n):
    for i in range(queue.size()):
        element = queue.attention()
        
        if i != (n + 1):
            queue.arrive(element)
    
    return queue

print("Cola sin el i-ésimo valor: ")            
delete_i(queue, n).show()