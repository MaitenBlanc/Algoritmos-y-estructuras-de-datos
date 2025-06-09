from typing import Any, Optional


class Queue:

    def __init__(self):
        self.__elements = []

    # Carga de datos al final de la cola
    def arrive(self, value: Any) -> None:
        return self.__elements.append(value)

    # Elimina y devuelve el elemento almacenado en el frente de la cola
    def attention(self) -> Optional[Any]:
        return self.__elements.pop(0) if self.__elements else None

    # Devuelve tamaño de la cola
    def size(self) -> int:
        return len(self.__elements)

    # Devuelve el valor del elemento que está almacenado en el frente de la cola sin eliminarlo
    def on_front(self) -> Optional[Any]:
        return self.__elements[0] if self.__elements else None

    # Elimina el elemento en el frente de la cola y lo inserta en el final
    def move_to_end(self):
        if self.__elements:
            value = self.attention()
            self.arrive(value)
            return value

    def show(self):
        for element in self.__elements:
            print(element)
