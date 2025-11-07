from typing import Any


class HeapMax:

    def __init__(self):
        self.elements = []

    # Devuelve la cantidad de elementos del montículo
    def size(self) -> int:
        return len(self.elements)

    # Inserta un elemento al final del montículo y luego lo flota hasta que cumpla la propiedad de orden
    def add(self, value) -> Any:
        self.elements.append(value)
        self.float(self.size() - 1)

    # Quita y devuelve el mínimo elemento del montículo (dato que se ubica en la raíz del árbol), y en su lugar coloca
    # el último elemento del montículo y luego lo hunde hasta que cumpla la propiedad de orden
    def remove(self) -> Any:
        last = self.size() - 1
        self.interchange(0, last)
        value = self.elements.pop()
        self.sink(0)
        return value

    # Flota el dato almacenado en el montículo desde el índice indicado hasta que cumpla la propiedad de orden
    def float(self, index: int) -> None:
        father = (index - 1) // 2
        while index > 0 and self.elements[index] > self.elements[father]:
            self.interchange(index, father)
            index = father
            father = (index - 1) // 2

    # Hunde el dato almacenado en el montículo desde el índice indicado hasta que cumpla la propiedad de orden
    def sink(self, index: int) -> None:
        left_son = (2 * index) + 1
        control = True
        while control and left_son < self.size():
            right_son = left_son + 1

            mayor = left_son
            if right_son < self.size():
                if self.elements[right_son] > self.elements[mayor]:
                    mayor = right_son

            if self.elements[index] < self.elements[mayor]:
                self.interchange(index, mayor)
                index = mayor
                left_son = (2 * index) + 1
            else:
                control = False

    # Intercambia los datos almacenados en los índices indicados
    def interchange(self, index_1: int, index_2: int) -> None:
        self.elements[index_1], self.elements[index_2] = self.elements[index_2], self.elements[index_1]

    # Ordena el montículo
    def heapsort(self) -> list:
        result = []
        while self.size() > 0:
            result.append(self.remove())
        return result
    
    # Agrega el elemento al final del montículo y luego lo flota según su criterio de prioridad, para usarlo como cola de prioridad
    def arrive(self, value: Any, priority: int) -> None:
        # priority 1-low, 2-medium, 3-high
        self.add([priority, value])
    
    # Elimina y devuelve el elemento almacenado en la cima del montículo, usado como cola de prioridad
    def attention(self) -> Any:
        value = self.remove()
        return value


# priority_queue = HeapMax()

# priority_queue.arrive("x", 1)
# priority_queue.arrive("b", 2)
# priority_queue.arrive("a", 2)
# priority_queue.arrive("f", 1)
# priority_queue.arrive("y", 1)
# priority_queue.arrive("j", 2)
# priority_queue.arrive("z", 3)

# print(priority_queue.elements)

# while priority_queue.size() > 0:
#     print(priority_queue.attention()[1])

#                           z 3
#                   y 1             j 2
#              f 1     x 1     a 2      b 2

# h.add(19)
# h.add(5)
# h.add(1)
# h.add(3)
# h.add(9)


# list_sort = h.heapsort()

# print(list_sort)
# print(h.elements)
