# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

import sys

sys.path.append("./Clases")
from tree import BinaryTree


class CreaturesTree(BinaryTree):
    class __nodeTree(BinaryTree._BinaryTree__nodeTree):
        def __init__(self, value: str, other_values: dict = None):
            if other_values is None:
                other_values = {
                    "defeated_by": [],
                    "description": "",
                    "captured_by": None,
                }
            super().__init__(value, other_values)


creatures = {
    "Ceto": {"defeated_by": "", "description": "", "captured_by": None},
    "Tifon": {"defeated_by": "Zeus", "description": "", "captured_by": None},
    "Equidna": {
        "defeated_by": "Argos Panoptes",
        "description": "",
        "captured_by": None,
    },
    "Dino": {"defeated_by": "", "description": "", "captured_by": None},
    "Pefredo": {"defeated_by": "", "description": "", "captured_by": None},
    "Enio": {"defeated_by": "", "description": "", "captured_by": None},
    "Escila": {"defeated_by": "", "description": "", "captured_by": None},
    "Caribdis": {"defeated_by": "", "description": "", "captured_by": None},
    "Euriale": {"defeated_by": "", "description": "", "captured_by": None},
    "Esteno": {"defeated_by": "", "description": "", "captured_by": None},
    "Medusa": {"defeated_by": "Perseo", "description": "", "captured_by": None},
    "Ladon": {"defeated_by": "Heracles", "description": "", "captured_by": None},
    "Aguila del Caucaso": {"defeated_by": "", "description": "", "captured_by": None},
    "Quimera": {"defeated_by": "Belerofonte", "description": "", "captured_by": None},
    "Hidra de Lerna": {
        "defeated_by": "Heracles",
        "description": "",
        "captured_by": None,
    },
    "Leon de Nemea": {
        "defeated_by": "Heracles",
        "description": "",
        "captured_by": None,
    },
    "Esfinge": {"defeated_by": "Edipo", "description": "", "captured_by": None},
    "Dragon de Colquida": {"defeated_by": "", "description": "", "captured_by": None},
    "Cerbero": {"defeated_by": "", "description": "", "captured_by": None},
    "Cerda de Cromion": {
        "defeated_by": "Teseo",
        "description": "",
        "captured_by": None,
    },
    "Ortro": {"defeated_by": "Heracles", "description": "", "captured_by": None},
    "Toro de Creta": {"defeated_by": "Teseo", "description": "", "captured_by": None},
    "Jabali de Calidon": {
        "defeated_by": "Atalanta",
        "description": "",
        "captured_by": None,
    },
    "Carcinos": {"defeated_by": "", "description": "", "captured_by": None},
    "Gerion": {"defeated_by": "Heracles", "description": "", "captured_by": None},
    "Cloto": {"defeated_by": "", "description": "", "captured_by": None},
    "Laquesis": {"defeated_by": "", "description": "", "captured_by": None},
    "Atropos": {"defeated_by": "", "description": "", "captured_by": None},
    "Minotauro de Creta": {
        "defeated_by": "Teseo",
        "description": "",
        "captured_by": None,
    },
    "Harpias": {"defeated_by": "", "description": "", "captured_by": None},
    "Argos Panoptes": {"defeated_by": "Hermes", "description": "", "captured_by": None},
    "Aves del Estinfalo": {"defeated_by": "", "description": "", "captured_by": None},
    "Talos": {"defeated_by": "Medea", "description": "", "captured_by": None},
    "Sirenas": {"defeated_by": "", "description": "", "captured_by": None},
    "Piton": {"defeated_by": "Apolo", "description": "", "captured_by": None},
    "Cierva de Cerinea": {"defeated_by": "", "description": "", "captured_by": None},
    "Basilisco": {"defeated_by": "", "description": "", "captured_by": None},
    "Jabali de Erimanto": {"defeated_by": "", "description": "", "captured_by": None},
}


# a)
creatures_tree = CreaturesTree()
for creature, data in creatures.items():
    creatures_tree.insert(creature, data)


print("a) Listado de las criaturas:")
creatures_tree.in_order()


# b)
def set_description(creatures_tree, name, description):
    root = creatures_tree.search(name)
    if root:
        root.other_values["description"] = description


set_description(creatures_tree, "Ceto", "Monstruo marino")
set_description(creatures_tree, "Tifon", "Gigante monstruoso")
print(
    f"b) {creatures_tree.search("Ceto").value} - {creatures_tree.search("Ceto").other_values}"
)
print(
    f"{creatures_tree.search("Tifon").value} - {creatures_tree.search("Tifon").other_values}"
)


# c)
def show_creature_info(creatures_tree, name):
    root = creatures_tree.search(name)
    if root:
        print(f"c) Información de {name}: {root.other_values}")


show_creature_info(creatures_tree, "Talos")

# d)
from collections import Counter


def top_3_heroes(creatures_tree):
    def _count_defeats(root, counter):
        if root:
            info = root.other_values
            if info["defeated_by"]:
                counter[info["defeated_by"]] = counter.get(info["defeated_by"], 0) + 1

            _count_defeats(root.left, counter)
            _count_defeats(root.right, counter)

    counter = {}
    _count_defeats(creatures_tree.root, counter)
    return Counter(counter).most_common(3)


print(
    f"d) 3 héroes o dioses que derrotaron más criaturas: {top_3_heroes(creatures_tree)}"
)


# e)
def list_defeated_by(self, hero):
    defeated = []

    if self.root is not None:
        for node in self.proximity_search(""):
            if hero in node.other_values["defeated_by"]:
                defeated.append(node.value)

    return defeated


print(
    f"e) Criaturas derrotadas por Heracles: {list_defeated_by(creatures_tree, 'Heracles')}"
)


# f)
def list_undefeated(self):
    undefeated = []

    if self.root is not None:
        for node in self.proximity_search(""):
            if node.other_values["defeated_by"] == "":
                undefeated.append(node.value)

    return undefeated


print(f"f) Criaturas no derrotadas: {list_undefeated(creatures_tree)}")


# h)
def modify_captured(creatures_tree, names, hero):
    for name in names:
        root = creatures_tree.search(name)
        if root:
            root.other_values["captured_by"] = hero


modify_captured(
    creatures_tree,
    ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabali de Erimanto"],
    "Heracles",
)
print(
    f"h) {creatures_tree.search('Cerbero').value, creatures_tree.search('Cerbero').other_values}"
)
print(
    f"{creatures_tree.search('Toro de Creta').value, creatures_tree.search('Toro de Creta').other_values}"
)
print(
    f"{creatures_tree.search('Cierva de Cerinea').value, creatures_tree.search('Cierva de Cerinea').other_values}"
)
print(
    f"{creatures_tree.search('Jabali de Erimanto').value, creatures_tree.search('Jabali de Erimanto').other_values}"
)

# i) Ya está definido el método proximity_search en la clase BinaryTree (demuestro con un ejemplo)
results = creatures_tree.proximity_search("Cer")
if results:
    print("i) Resultados de la búsqueda por proximidad 'Cer':")
    for root in results:
        print(f"{root.value} - {root.other_values}")
else:
    print("i) No se encontraron coincidencias.")


# j)
def delete_creatures(creatures_tree, names):
    for name in names:
        creatures_tree.delete(name)


delete_creatures(creatures_tree, ["Basilisco", "Sirenas"])
print("j) Listado después de eliminar Basilisco y Sirenas:")
creatures_tree.in_order()


# k)
def modify_defeated(creatures_tree, name, info):
    root = creatures_tree.search(name)
    if root:
        root.other_values["defeated_by"] = info


modify_defeated(creatures_tree, "Aves del Estinfalo", "Heracles (varias)")
print(
    f"k) {creatures_tree.search('Aves del Estinfalo').value, creatures_tree.search('Aves del Estinfalo').other_values}"
)


# l)
def modify_name(creatures_tree, old_name, new_name):
    value, other_value = creatures_tree.delete(old_name)
    if value is not None:
        creatures_tree.insert(new_name, other_value)
    else:
        print(f"Creature {old_name} not found.")


modify_name(creatures_tree, "Ladon", "Dragón Ladón")
print(
    f"l) {creatures_tree.search('Dragón Ladón').value, creatures_tree.search('Dragón Ladón').other_values}"
)
print(f"{creatures_tree.search('Ladon')}")  # Debe ser None

# m)
print("m) Listado por nivel del árbol: ")
creatures_tree.by_level()


# n)
def list_captured_by(self, hero):
    captured = []

    if self.root is not None:
        for node in self.proximity_search(""):
            if node.other_values["captured_by"] == hero:
                captured.append(node.value)

    return captured


print(
    f"n) Criaturas capturadas por Heracles: {list_captured_by(creatures_tree, 'Heracles')}"
)
