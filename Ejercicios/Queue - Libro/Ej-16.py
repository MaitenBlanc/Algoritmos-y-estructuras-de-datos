"""Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente
criterio (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la
siguiente situación:
a. cargue tres documentos de empleados (cada documento se representa solamente con
un nombre).
b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
c. cargue dos documentos del staff de TI.
d. cargue un documento del gerente.
e. imprima los dos primeros documentos de la cola.
f. cargue dos documentos de empleados y uno de gerente.
g. imprima todos los documentos de la cola de impresión."""

import sys

sys.path.append("./Clases")

from cola import Queue


class PriorityQueue(Queue):
    def __init__(self):
        self.__elements = []

    # Sobreescribo las funciones que necesito para que actúen por prioridad
    def arrive(self, value, priority):
        new_element = {"value": value, "priority": priority}
        self.__elements.append(new_element)

        # acomodar según prioridad
        i = len(self.__elements) - 1

        while (
            i > 0
            and self.__elements[i]["priority"] > self.__elements[i - 1]["priority"]
        ):
            self.__elements[i], self.__elements[i - 1] = (
                self.__elements[i - 1],
                self.__elements[i],
            )
            i -= 1

    def attention(self):
        if self.__elements:
            return self.__elements.pop(0)["value"]
        return None

    def size(self) -> int:
        return len(self.__elements)

    def on_front(self):
        return self.__elements[0]["value"] if self.__elements else None

    def show(self):
        for element in self.__elements:
            print(f"{element['value']} - Prioridad: {element['priority']}")


print_queue = PriorityQueue()

# Prioridades 1-Empleado, 2-Staff TI y 3-Gerente

# a)
print_queue.arrive("Documento Empleado 1", 1)
print_queue.arrive("Documento Empleado 2", 1)
print_queue.arrive("Documento Empleado 3", 1)

# b)
print(f"b) Imprimir primer documento de la cola: {print_queue.attention()}")

# c)
print_queue.arrive("Documento Staff TI 1", 2)
print_queue.arrive("Documento Staff TI 2", 2)

# d)
print_queue.arrive("Documento Gerente 1", 3)

# e)
print("e) Imprimir los dos primeros documentos de la cola: ")
print(f"   - {print_queue.attention()}")
print(f"   - {print_queue.attention()}")

# f)
print_queue.arrive("Documento Empleado 4", 1)
print_queue.arrive("Documento Empleado 5", 1)
print_queue.arrive("Documento Gerente 2", 3)

# g)
print("g) Todos los documentos de la cola:")
while print_queue.size() > 0:
    print(f"Imprimir: {print_queue.attention()}")
