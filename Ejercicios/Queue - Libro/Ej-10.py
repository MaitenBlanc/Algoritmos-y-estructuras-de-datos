""" 
    Dada una cola con las notificaciones de las aplicaciones de redes sociales de un Smartphone, de las cual se cuenta con la hora de la notificación, la 
    aplicación que la emitió y el mensaje, resolver las siguientes actividades:
    a. escribir una función que elimine de la cola todas las notificaciones de Facebook;
    b. escribir una función que muestre todas las notificaciones de Twitter, cuyo mensaje incluya la palabra ‘Python’, si perder datos en la cola;
    c. utilizar una pila para almacenar temporáneamente las notificaciones producidas entre las 11:43 y las 15:57, y determinar cuántas son.
"""

import sys
sys.path.append("./Clases")
from cola import Queue
from stack import Stack

queue = Queue()

queue.arrive({"hour": "10:30", "app": "Facebook", "message": "Nuevo comentario"})
queue.arrive({"hour": "11:00", "app": "Twitter", "message": "Aprendiendo Java!"})
queue.arrive({"hour": "12:00", "app": "Facebook", "message": "Nuevo like"})
queue.arrive({"hour": "13:00", "app": "Twitter", "message": "Python es increíble"})
queue.arrive({"hour": "14:00", "app": "Instagram", "message": "Nueva foto publicada"})
queue.arrive({"hour": "15:00", "app": "Facebook", "message": "Nuevo mensaje privado"})

# a) 
def delete_all_facebook(queue: Queue):
    for i in range(queue.size()):
        notification = queue.attention()
    
        if (notification['app'] != "Facebook"):
            queue.arrive(notification)
        
    return queue

# b)
def show_message_python(queue: Queue):
    aux_queue = Queue()
    
    while queue.size() > 0:
        notification = queue.attention()
        
        if (notification['app'] == "Twitter" and "Python" in notification['message']):
            print(notification)

        aux_queue.arrive(notification)
        
    while aux_queue.size() > 0:
        queue.arrive(aux_queue.attention())
        
# c) 
def stack_queue(queue: Queue):
    stack = Stack()
    count = 0
    
    while queue.size() > 0:
        notification = queue.attention()
        
        if (notification['hour'] >= "11:43" and notification['hour'] <= "15:57"):
            stack.push(notification)
            count += 1
    
    while stack.size() > 0:
        queue.arrive(stack.pop())
    
    return count

print("a) ")
delete_all_facebook(queue).show()

print("b) ")
show_message_python(queue)

print(f"c) Cantidad de notificaciones producidas entre las 11:43 y las 15:57: {stack_queue(queue)}")
