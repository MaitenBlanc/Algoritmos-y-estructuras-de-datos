"""Dada dos colas con valores ordenadas, realizar un algoritmo que permita combinarlas en una
nueva cola. Se deben mantener ordenados los valores sin utilizar ninguna estructura auxiliar,
ni métodos de ordenamiento."""

import sys

sys.path.append("./Clases")
from cola import Queue


queue1 = Queue()
queue2 = Queue()

queue2.arrive(1)
queue2.arrive(2)
queue2.arrive(3)
queue2.arrive(4)
queue2.arrive(5)

queue1.arrive(7)
queue1.arrive(8)
queue1.arrive(9)
queue1.arrive(10)
queue1.arrive(11)

def merge_queues(queue1, queue2):
    merged_queue = Queue()
    
    while queue1.size() > 0 and queue2.size() > 0:
        front1 = queue1.on_front()
        front2 = queue2.on_front()
        
        if front1 <= front2:
            merged_queue.arrive(queue1.attention())
        else:
            merged_queue.arrive(queue2.attention())
        
    while queue1.size() > 0:
        merged_queue.arrive(queue1.attention())
        
    while queue2.size() > 0:
        merged_queue.arrive(queue2.attention())
        
    return merged_queue

merge_queues(queue1, queue2).show()
