"""Utilizando una lista doblemente enlazada, cargar una palabra carácter a carácter, y determinar
si la misma es un palíndromo, sin utilizar ninguna estructura auxiliar."""

# Lista doblemente enlazada: lista implementada manualmente con nodos que apuntan hacia adelante y hacia atrás.


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoubleList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, data):
        new = Node(data)
        if not self.first:
            self.first = self.last = new
        else:
            self.last.next = new
            new.prev = self.last
            self.last = new

    def is_palindrome(self):
        left = self.first
        right = self.last

        while left != None and right != None and left != right and left.prev != right:
            if left.data != right.data:
                return False

            left = left.next
            right = right.prev
        return True


lista = DoubleList()

word = input("Ingrese una palabra: ")

for letter in word:
    lista.insert(letter)

if lista.is_palindrome():
    print(f"La palabra {word} es palíndromo.")
else:
    print(f"La palabra {word} no es palíndromo.")
