"""Desarrollar un algoritmo que permita cargar procesos a la cola de ejecución de un procesador,
de los cuales se conoce id del proceso y tiempo de ejecución. Resuelva las siguientes situaciones:
a. simular la atención de los procesos de la cola transcurriendo su tiempo –utilizando la función time.sleep
(segundos) – hasta que se vacíe la cola.
b. considerar que el quantum de tiempo asignado por el procesador a cada proceso es como
máximo 4.5 segundos –si el proceso no terminó su ejecución deberá volver a la cola con el
tiempo restante para terminar su ejecución–.
c. cuando se realiza el cambio de proceso, porque finalizó su ejecución o porque se le agotó el
quantum de tiempo, se pueden ingresar nuevos procesos a la cola por el usuario.
d. no se aplican criterios de prioridad en los procesos."""

import sys

sys.path.append("./Clases")

from cola import Queue
import time

process_queue = Queue()

initial_processes = [("P1", 3.0), ("P2", 6.0), ("P3", 2.5)]

for process in initial_processes:
    process_queue.arrive(process)

QUANTUM = 4.5


def add_process(queue: Queue):
    print("Ingrese datos del nuevo proceso: ")
    process_id = input("ID: ")
    runtime = float(input("Tiempo de ejecución (segundos): "))

    queue.arrive((process_id, runtime))


# a)
def attention_simulation(queue: Queue, quantum):
    while queue.size() > 0:
        process_id, runtime = queue.attention()
        print(
            f"Ejecutando proceso {process_id}... Tiempo restante: {runtime:.2f} segundos."
        )

        # b)
        if runtime <= quantum:
            print(f"Proceso {process_id} finalizado.")
            time.sleep(runtime)
        else:
            time_left = runtime - quantum
            print(
                f"Quantum agotado para proceso {process_id} - Tiempo restante: {time_left:.2f} segundos."
            )
            time.sleep(quantum)
            queue.arrive((process_id, time_left))

        # c)
        add_process(queue)
    print("Todos los procesos fueron atendidos.")


attention_simulation(process_queue, QUANTUM)
