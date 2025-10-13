# Utilice cola de prioridad, para atender la cola de impresión tomando en cuenta el siguiente criterio
# (1- empleados, 2- staff de tecnologías de la información “TI”, 3- gerente), y resuelva la siguiente situación:
# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
# c. cargue dos documentos del staff de TI.
# d. cargue un documento del gerente.
# e. imprima los dos primeros documentos de la cola.
# f. cargue dos documentos de empleados y uno de gerente.
# g. imprima todos los documentos de la cola de impresión.

import sys

sys.path.append("./Clases")
from heapMax import HeapMax

priority_heap = HeapMax()

# Prioridad a usar: 1-empleados, 2-staff de TI, 3-gerente

# a. cargue tres documentos de empleados (cada documento se representa solamente con un nombre).
priority_heap.arrive("doc_empleado_1", 1)
priority_heap.arrive("doc_empleado_2", 1)
priority_heap.arrive("doc_empleado_3", 1)

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
print("b) ")
print("Atendiendo:", priority_heap.attention()[1])

# c. cargue dos documentos del staff de TI.
priority_heap.arrive("doc_TI_1", 2)
priority_heap.arrive("doc_TI_2", 2)

# d. cargue un documento del gerente.
priority_heap.arrive("doc_gerente_1", 3)

# e. imprima los dos primeros documentos de la cola.
print("e) ")
for i in range(2):
    print("Atendiendo:", priority_heap.attention()[1])

# f. cargue dos documentos de empleados y uno de gerente.
priority_heap.arrive("doc_empleado_4", 1)
priority_heap.arrive("doc_empleado_5", 1)
priority_heap.arrive("doc_gerente_2", 3)

# g. imprima todos los documentos de la cola de impresión.
print("g) ")
while priority_heap.size() > 0:
    print("Atendiendo:", priority_heap.attention()[1])
