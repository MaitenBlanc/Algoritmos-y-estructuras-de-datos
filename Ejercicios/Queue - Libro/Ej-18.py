"""Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar un algoritmo
que resuelva las siguientes situaciones:
a. cargar 1000 turnos de manera aleatoria a la cola.
b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan con la letra A, C
y F, y la cola_2 con el resto de los turnos (B, D y E).
c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál de las letras
tiene mayor cantidad.
d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número de turno sea
mayor que 506."""

import sys

sys.path.append("./Clases")

from cola import Queue
import random
from collections import defaultdict


class Queue(Queue):
    def get_element(self):
        return self.__elements


def generate_shifts():
    letters = "ABCDEF"
    letter = random.choice(letters)
    number = random.randint(0, 999)
    return f"{letter}{number:03d}"


# a)
def load_shifts(queue, amount):
    for _ in range(amount):
        shift = generate_shifts()
        queue.arrive(shift)

    return queue


queue = Queue()
load_shifts(queue, 10)
queue.show()

# b)
def separate_queue(queue: Queue):
    queue1 = Queue()
    queue2 = Queue()

    while queue.size() > 0:
        element = queue.attention()

        if element[0] in "ACF":
            queue1.arrive(element)
        else:
            queue2.arrive(element)

    return queue1, queue2


print("b) ")
q1, q2 = separate_queue(queue)
print("Cola 1: ")
q1.show()
print("Cola 2: ")
q2.show()


# c)
def queue_more_shifts(queue1: Queue, queue2: Queue):
    if queue1.size() > queue2.size():
        print(f"La cola 1 tiene más cantidad de turnos.")
        queue = queue1
    else:
        print(f"La cola 2 tiene más cantidad de turnos.")
        queue = queue2

    letter_count = defaultdict(int)
    for shift in queue.get_element():
        letter = shift[0]
        letter_count[letter] += 1

    max_letter = max(letter_count, key=letter_count.get)
    print(
        f"Letra con más turnos en la cola: {max_letter}, con {letter_count[max_letter]} turnos."
    )


queue_more_shifts(q1, q2)
