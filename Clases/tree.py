from typing import Any, Optional
import sys

sys.path.append("./Clases")
from cola import Queue


class BinaryTree:

    class __nodeTree:

        def __init__(self, value: Any, other_values: Optional[Any] = None):
            self.value = value
            self.other_values = other_values
            self.left = None
            self.right = None
            self.hight = 0

    def __init__(self):
        self.root = None

    # insertar un nuevo nodo en el árbol
    def insert(self, value: Any, other_values: Optional[Any] = None):
        def __insert(root, value, other_values):
            if root is None:
                return BinaryTree.__nodeTree(value, other_values)
            elif value < root.value:
                root.left = __insert(root.left, value, other_values)
            else:
                root.right = __insert(root.right, value, other_values)

            root = self.auto_balance(root)
            self.update_hight(root)

            return root

        self.root = __insert(self.root, value, other_values)

    # recorrido de orden previo del árbol, muestra los elem almacenados en el árbol
    # 1. Visita el nodo actual (root).
    # 2. Recorre el subárbol izquierdo.
    # 3. Recorre el subárbol derecho.
    def pre_order(self):
        def __pre_order(root):
            if root is not None:
                print(root.value, root.other_values, root.hight)
                __pre_order(root.left)
                __pre_order(root.right)

        if self.root is not None:
            __pre_order(self.root)

    # recorrido en orden del árbol, muestra los elem almacenados en el árbol
    # 2. Recorre el subárbol izquierdo.
    # 1. Visita el nodo actual (root).
    # 3. Recorre el subárbol derecho.
    def in_order(self):
        def __in_order(root):
            if root is not None:
                __in_order(root.left)
                print(root.value, root.other_values)
                __in_order(root.right)

        if self.root is not None:
            __in_order(self.root)

    # recorrido de orden posterior del árbol, muestra los elem almacenados en el árbol
    # 2. Recorre el subárbol izquierdo.
    # 3. Recorre el subárbol derecho.
    # 1. Visita el nodo actual (root).
    def post_order(self):
        def __post_order(root):
            if root is not None:
                __post_order(root.right)
                print(root.value)
                __post_order(root.left)

        if self.root is not None:
            __post_order(self.root)

    # buscar un valor en el árbol, devuelve el nodo si lo encuentra o None si no
    def search(self, value: Any) -> __nodeTree:
        def __search(root, value):
            if root is not None:
                if root.value == value:
                    return root
                elif root.value > value:
                    return __search(root.left, value)
                else:
                    return __search(root.right, value)

        aux = None
        if self.root is not None:
            aux = __search(self.root, value)
        return aux

    def proximity_search(self, value: Any) -> __nodeTree:
        aux = []
        
        def __search(root, value):
            if root is not None:
                if root.value.startswith(value):
                    aux.append(root)
                    # print(root.value)
                # elif root.value > value:
                __search(root.left, value)
                # else:
                __search(root.right, value)

        __search(self.root, value)
        return aux

    # eliminar un valor del árbol, devuelve el valor eliminado o None si no lo encuentra
    def delete(self, value: Any):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            delete_value = None
            deleter_other_values = None
            if root is not None:
                if value < root.value:
                    root.left, delete_value, deleter_other_values = __delete(
                        root.left, value
                    )
                elif value > root.value:
                    root.right, delete_value, deleter_other_values = __delete(
                        root.right, value
                    )
                else:
                    delete_value = root.value
                    deleter_other_values = root.other_values
                    if root.left is None:
                        root = root.right
                    elif root.right is None:
                        root.right = root.left
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        root.other_values = replace_node.other_values

                root = self.auto_balance(root)
                self.update_hight(root)
            return root, delete_value, deleter_other_values

        delete_value = None
        deleter_other_values = None
        if self.root is not None:
            self.root, delete_value, deleter_other_values = __delete(self.root, value)

        return delete_value, deleter_other_values

    # recorrido por nivel del árbol, muestra los elem almacenados en el árbol
    def by_level(self):
        tree_queue = Queue()
        if self.root is not None:
            tree_queue.arrive(self.root)

            while tree_queue.size() > 0:
                node = tree_queue.attention()
                print(node.value)
                if node.left is not None:
                    tree_queue.arrive(node.left)
                if node.right is not None:
                    tree_queue.arrive(node.right)

    # Altura del árbol
    def hight(self, root):
        if root is None:
            return -1
        else:
            return root.hight

    # Actualizar la altura del árbol
    def update_hight(self, root):
        if root is not None:
            alt_left = self.hight(root.left)
            alt_right = self.hight(root.right)
            root.hight = max(alt_left, alt_right) + 1

    # Rotación simple a la derecha o izquierda
    def simple_rotation(self, root, control):
        if control:  # RS Right
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:  # RS Left
            aux = root.right
            root.right = aux.left
            aux.left = root

        self.update_hight(root)
        self.update_hight(aux)
        root = aux
        return root

    # Rotación doble a la derecha o izquierda
    def double_rotation(self, root, control):
        if control:  # RD Right
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)

        return root

    # Auto balanceo del árbol
    def auto_balance(self, root):
        if root is not None:
            if self.hight(root.left) - self.hight(root.right) == 2:
                if self.hight(root.left.left) >= self.hight(root.left.right):
                    # print("RS RIGHT")
                    root = self.simple_rotation(root, True)
                else:
                    # print("RD RIGHT")
                    root = self.double_rotation(root, True)
            if self.hight(root.right) - self.hight(root.left) == 2:
                if self.hight(root.right.right) >= self.hight(root.right.left):
                    # print("RS LEFT")
                    root = self.simple_rotation(root, False)
                else:
                    # print("RD LEFT")
                    root = self.double_rotation(root, False)
        return root


# Pruebas
# arbol = BinaryTree()
# arbol_heroes = BinaryTree()
# arbol_villanos = BinaryTree()


# print()
# arbol.update_hight(arbol.root.left.left)
# print()
# arbol.update_hight(arbol.root.left)
# print()
# arbol.update_hight(arbol.root)
# print()
# arbol.pre_order()

# arbol.insert('F', 'f')
# arbol.insert('B', 'b')
# arbol.insert('K', 'k')
# arbol.insert('H', 'h')
# arbol.insert('J', 'j')
# arbol.insert('E', 'e')
# arbol.insert('B')
# arbol.insert('V')
# arbol.pre_order()
# print()

# for i in range(1, 16):
#     arbol.insert(i)

# arbol.pre_order()

# if pos is not None:
#     arbol.delete('F')
#     arbol.insert('C', 'c')

# delete_value, deleter_other_values = arbol.delete('K')
# if delete_value is not None:
#     print(delete_value, deleter_other_values)


# arbol.in_order()
# # delete_value = arbol.delete('F')

# # if delete_value is not None:
# #     print(f'valor eliminado {delete_value}')
# # else:
# #     print('valor no encontrado')
# # print()
# arbol.by_level()


# # arbol.insert(11)

# # pos = arbol.search(19)
# # print(pos)
# arbol.in_order()

# sys.path.append("./Parciales/Parcial 1")
# from super_heroes_data import superheroes

# for super_hero in superheroes:
#     arbol.insert(super_hero['name'], super_hero)


# arbol.divide_tree(arbol_heroes, arbol_villanos)

# bosque = [arbol_heroes, arbol_villanos]

# for tree in bosque:
#     tree.in_order()
#     print()

# arbol.proximity_search('Dr')
# name = input('ingrese nombre para modificar: ')
# value, other_value = arbol.delete(name)

# if value is not None:
#     fix_name = input('ingrese el nuevo nombre: ')
#     other_value['name'] = fix_name
#     arbol.insert(fix_name, other_value)

# print()
# arbol.proximity_search('Dr')
# print()
# pos = arbol.search('Dr Strange')
# if pos is not None:
#     print(pos.value, pos.other_values)

# print(arbol.count_heroes())

# arbol.villain_in_order()

# print()
# pos = arbol.search("Thanos")
# if pos is not None:
#     print(pos.value, pos.other_values)
