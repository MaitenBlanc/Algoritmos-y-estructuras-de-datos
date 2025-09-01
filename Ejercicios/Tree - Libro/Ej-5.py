# 5. Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe (MCU), desarrollar un
# algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano que indica si es un héroe o un
# villano, True y False respectivamente;
# b. listar los villanos ordenados alfabéticamente;
# c. mostrar todos los superhéroes que empiezan con C;
# d. determinar cuántos superhéroes hay el árbol;
# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar
# su nombre;
# f. listar los superhéroes ordenados de manera descendente;
# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver
# las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol.

import sys

sys.path.append("./Clases")
sys.path.append("./Parciales/Parcial 1")
from tree import BinaryTree
from super_heroes_data import superheroes

arbol = BinaryTree()

# a.
for super_heroes_data in superheroes:
    arbol.insert(super_heroes_data["name"], super_heroes_data)


# b.
def villain_in_order(self):
    def __villain_in_order(root):
        if root is not None:
            __villain_in_order(root.left)  # me voy a la izq
            if root.other_values["is_villain"] is True:
                print(root.value)
            __villain_in_order(root.right)  # me voy a la der

    # llamada
    if self.root is not None:
        __villain_in_order(self.root)


# print("b) Listado alfabéticamente de villanos: ")
# villain_in_order(arbol)


# c.
def show_superheroes_with_c(self):
    def __show_superheroes_with_c(root):
        if root is not None:
            __show_superheroes_with_c(root.left)
            if root.value.startswith("C"):
                print(root.value)
            __show_superheroes_with_c(root.right)

    # llamada
    if self.root is not None:
        __show_superheroes_with_c(self.root)


# print("c) Listado de superheroes que empiezan con C: ")
# show_superheroes_with_c(arbol)


# d.
def count_superheores(self):
    def __count_superheroes(root):
        if root is None:
            return 0
        elif root.other_values:
            return 1 + __count_superheroes(root.left) + __count_superheroes(root.right)

    # llamada
    return __count_superheroes(self.root)


# print(f"d) Cantidad de superheroes: {count_superheores(arbol)}")

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;

# TODO: HACER ESTE PUNTO CUANDO DEMOS PROXIMIDAD


# f.
def superheroes_post_order(self):
    def __superheroes_post_order(root):
        if root is not None:
            __superheroes_post_order(root.right)
            print(root.value)
            __superheroes_post_order(root.left)

    # llamada
    if self.root is not None:
        __superheroes_post_order(self.root)


# print("f) Listado descendente de superheroes: ")
# superheroes_post_order(arbol)


# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
def generate_forest_in_order(self):
    villain_tree = BinaryTree()
    heroes_tree = BinaryTree()

    def __generate_forest_in_order(root):
        if root is not None:
            __generate_forest_in_order(root.left)
            if root.other_values["is_villain"] is True:
                villain_tree.insert(root.value, root.other_values)
            else:
                heroes_tree.insert(root.value, root.other_values)
            __generate_forest_in_order(root.right)

    # llamada
    if self.root is not None:
        __generate_forest_in_order(self.root)
        return heroes_tree, villain_tree


heroes_tree, villain_tree = generate_forest_in_order(arbol)


# g. I.
def node_counter(self):
    def __counter(root):
        if not root:
            return 0
        else:
            return 1 + __counter(root.left) + __counter(root.right)

    return __counter(self.root)


print(f"g.I) Cantidad de nodos del árbol de héroes: {node_counter(heroes_tree)}")
print(f"g.I) Cantidad de nodos del árbol de villanos: {node_counter(villain_tree)}")


# II. realizar un barrido ordenado alfabéticamente de cada árbol
# g.II)
def in_order(self):
    def __in_order(root):
        if root is not None:
            __in_order(root.left)
            print(root.value)
            __in_order(root.right)

    # llamada
    if self.root is not None:
        __in_order(self.root)


print("g.II) Barrido ordenado alfabéticamente del árbol de héroes: ")
in_order(heroes_tree)
print("g.II) Barrido ordenado alfabéticamente del árbol de villanos: ")
in_order(villain_tree)
