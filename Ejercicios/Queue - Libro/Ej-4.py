""" Dada una cola de números cargados aleatoriamente, eliminar de ella todos los que no sean primos. """

import sys
sys.path.append("./Clases")
from cola import Queue
from random import randint

queue = Queue()

def prime_number(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(10):
    queue.arrive(randint(1, 100))
    
print("Cola original: ")
queue.show()

for i in range(queue.size()):
    n = queue.on_front()
    
    if (prime_number(n)):
        queue.move_to_end()
    else:
        queue.attention()
    
print("Cola de números primos: ")
queue.show()