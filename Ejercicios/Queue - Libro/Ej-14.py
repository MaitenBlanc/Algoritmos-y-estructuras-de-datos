"""Realizar un algoritmo que permita realizar las siguientes funciones:
a. cargar semáforos de una rotonda y sus respectivos tiempos de encendido en verde (cargue
al menos tres semáforos).
b. simular el funcionamiento de los semáforos cargados (cola circular).
c. debe mostrar por pantalla el cambio de colores y el número del semáforo."""

import sys

sys.path.append("./Clases")

from cola import Queue

# a)
stoplight_queue = Queue()
stoplight_queue.arrive({"number": 1, "time": 3})
stoplight_queue.arrive({"number": 2, "time": 4})
stoplight_queue.arrive({"number": 3, "time": 2})

# b) 
def stoplight_simulator(queue: Queue, cycles: int):
    for i in range(cycles * queue.size()):
        stoplight = queue.attention()
        num = stoplight["number"]
        time = stoplight["time"]
        
        print(f"Semáforo n° {num} - Tiempo en verde: {time} segundos.")
        queue.arrive(stoplight)

print("c)")
stoplight_simulator(stoplight_queue, 2)

