"""Eliminar de una cola de caracteres todas las vocales que aparecen."""

import sys
sys.path.append("./Clases")
from cola import Queue
from random import randint

queue_letters = Queue()

for i in range(15):
    queue_letters.arrive(chr(randint(65, 90)))
    
print("Cola original: ")
queue_letters.show()

for i in range(queue_letters.size()):
    if queue_letters.on_front() in ["A", "E", "I", "O", "U"]:
        queue_letters.attention()
    else:
        queue_letters.move_to_end()
        
print("Cola sin vocales: ")
queue_letters.show()