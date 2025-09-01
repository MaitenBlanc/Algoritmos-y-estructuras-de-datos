# 1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria– que resuelva las
# siguientes actividades:
# a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
# b. determinar si un número está cargado en el árbol o no;
# c. eliminar tres valores del árbol;
# d. determinar la altura del subárbol izquierdo y del subárbol derecho;
# e. determinar la cantidad de ocurrencias de un elemento en el árbol;
# f. contar cuántos números pares e impares hay en el árbol.

import sys

sys.path.append("./Clases")
from tree import BinaryTree
import random

arbol = BinaryTree()

# Carga de 1000 números enteros aleatorios
for i in range(10):
    num = random.randint(1, 10000)
    arbol.insert(num)

# a)
print("a) ")
print("Preorden:")
arbol.pre_order()
print("\nInorden:")
arbol.in_order()
print("\nPostorden:")
arbol.post_order()
print("\nPor nivel:")
arbol.by_level()

# b)
searched_num = int(input("\nNúmero a buscar en el árbol: "))


def search_num(arbol, num):
    if arbol.search(num) is not None:
        print(f"El número {num} está en el árbol.")
    else:
        print(f"El número {num} no está en el árbol.")


print("b) ")
search_num(arbol, searched_num)


# c)
def delete_num(arbol, num):
    delete_value = arbol.delete(num)
    # si devuelve una tupla, es porque se borró el valor
    if isinstance(delete_value, tuple):
        delete_value, _ = delete_value
    else:
        delete_value = None

    if delete_value is not None:
        print(f"El número {num} fue eliminado del árbol.")
    else:
        print(f"El número {num} no se encontró en el árbol.")


print("c) ")
for i in range(3):
    num_to_delete = int(input(f"Número {i+1} a eliminar del árbol: "))
    delete_num(arbol, num_to_delete)

print("\nÁrbol después de eliminaciones:")
arbol.in_order()


# d)
def height(node):
    if node is None:
        return -1  # árbol vacío
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return 1 + max(left_height, right_height)


print("d) ")
height_left = height(arbol.root.left)
height_right = height(arbol.root.right)
print(f"Altura del subárbol izquierdo: {height_left}")
print(f"Altura del subárbol derecho: {height_right}")


# e)
def count_occurrences(node, value):
    if node is None:
        return 0
    if node.value == value:
        count = 1
    else:
        count = 0
    count += count_occurrences(node.left, value)
    count += count_occurrences(node.right, value)
    return count


print("e)")
value_to_count = int(input("Número a contar en el árbol: "))
occurrences = count_occurrences(arbol.root, value_to_count)
print(f"El número {value_to_count} aparece {occurrences} veces en el árbol.")


# f) contar cuántos números pares e impares hay en el árbol.
def count_even_odd(node):
    if node is None:
        return 0, 0
    left_even, left_odd = count_even_odd(node.left)
    right_even, right_odd = count_even_odd(node.right)
    if node.value % 2 == 0:
        return 1 + left_even + right_even, left_odd + right_odd
    else:
        return left_even + right_even, 1 + left_odd + right_odd


print("f)")
even_count, odd_count = count_even_odd(arbol.root)
print(f"Números pares en el árbol: {even_count}")
print(f"Números impares en el árbol: {odd_count}")
