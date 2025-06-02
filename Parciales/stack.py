from typing import Any, Optional
from random import randint

class Stack:
    __elements = [1,2,3]
        
    # constructor
    def __init__(self):
        self.__elements = []
    
    # función apilar (Agrega el elemento sobre la cima de la pila)
    def push(self, value: Any) -> None:
        self.__elements.append(value)
        
    # función desapilar (Elimina y devuelve el elemento almacenado en la cima de la pila)
    def pop(self) -> Optional[Any]:
        return (self.__elements.pop() if self.__elements else None)
    
    # función tamaño (Devuelve la cantidad de elementos en la pila)
    def size(self) -> int:
        return len(self.__elements)
        
    # función cima (Devuelve el valor del elemento que está almacenado en la cima de la pila pero sin eliminarlo)
    def on_top(self) -> Optional[Any]:
        return (self.__elements[-1] if self.__elements else None)
        
    def show(self):
        aux_stack = Stack()        
        while self.size() > 0:
            value = self.pop()
            print(value)
            aux_stack.push(value)
            
        while aux_stack.size() > 0:
            self.push(aux_stack.pop())
        
        
        
        
        
    
    
    
    
    
    # def mostrar_elementos(self):
    #     # Acá sí
    #     stack.__elements[1] = 99
    #     print(self.__elements)
        
    
# stack = Stack()
# # No funciona porque __elements es private
# # stack.__elements[1] = 99
# # stack.mostrar_elementos()

# for i in range(5):
#     stack.push(randint(1,100))
    
# # stack.show()
# # # print(stack.pop())
# # print(stack.on_top())
# # stack.show()