# Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas
# a un archivo que contiene personajes de la saga de Star Wars, de los cuales se sabe su nombre,
# altura y peso. Además deberá contemplar los siguientes requerimientos:
# a. en el árbol se almacenara solo el nombre del personaje, además de la posición en la que se encuentra en el archivo (nrr);
# b. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
# c. mostrar toda la información de Yoda y Boba Fett;
# d. mostrar un listado ordenado alfabéticamente de los personajes que miden más de 1 metro;
# e. mostrar un listado ordenado alfabéticamente de los personajes que pesan menos de 75 kilos;
# f. deberá utilizar el TDA archivo desarrollado en el capítulo V;
import sys

sys.path.append("./Clases")
from tree import BinaryTree

from random import randint

star_wars_tree = BinaryTree()
star_wars_tree_id = BinaryTree()

characters = [
    "Yoda",
    "Darth Vader",
    "Boba Fett",
    "Grogu",
    "Mando",
    "Han Solo",
    "Palpatine",
    "Mace Windu",
]

for character in characters:
    info = {"weight": randint(10, 100), "height": randint(40, 190)}
    info.update({"id": character[1]})
    star_wars_tree.insert(character[0], info)

    info2 = info.copy()
    info2.pop("id")
    info2.update({"name": character[0]})
    star_wars_tree_id.insert(character[1], info2)

star_wars_tree.in_order()
print()

# Punto B
star_wars_tree.insert("R2-D2", {"weight": 100, "height": 85, "id": 15})
star_wars_tree_id.insert(15, {"weight": 100, "height": 85, "name": "R2-D2"})
value, other_values = star_wars_tree.delete("Palpatine")
star_wars_tree_id.delete(other_values["id"])

pos = star_wars_tree.search("R2-D2")
if pos is not None:
    pos.other_values["weight"] = 115
    pos.other_values["height"] = 71

value, other_values = star_wars_tree.delete("Mando")
if value is not None:
    new_value = "Din Djarin"
    star_wars_tree.insert(new_value, other_values)

    print("buscado ", star_wars_tree.search("Din Djarin").value)

# Punto C
pos = star_wars_tree.search("Yoda")
if pos is not None:
    print(f"Search character {pos.value}, character info {pos.other_values}")
pos = star_wars_tree.search("Boba Fett")
if pos is not None:
    print(f"Search character {pos.value}, character info {pos.other_values}")


# Punto D
def in_order_height(self):
    def __in_order_height(root):
        if root is not None:
            __in_order_height(root.left)
            if root.other_values["height"] > 100:
                print(root.value, root.other_values["height"])
            __in_order_height(root.right)

    if self.root is not None:
        __in_order_height(self.root)


in_order_height(star_wars_tree)
print()


# Punto E
def in_order_weight(self):
    def __in_order_weight(root):
        if root is not None:
            __in_order_weight(root.left)
            if root.other_values["weight"] < 75:
                print(root.value, root.other_values["weight"])
            __in_order_weight(root.right)

    if self.root is not None:
        __in_order_weight(self.root)


in_order_weight(star_wars_tree)
print()


star_wars_tree.in_order()
print()
