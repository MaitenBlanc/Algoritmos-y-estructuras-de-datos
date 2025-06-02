"""Realizar un algoritmo que registre los movimientos de un robot, los datos que se guardan son
cantidad de pasos y dirección –suponga que el robot solo puede moverse en ocho direcciones:
norte, sur, este, oeste, noreste, noroeste, sureste y suroeste–. Luego desarrolle otro algoritmo
que genere la secuencia de movimientos necesarios para hacer volver al robot a su lugar de
partida, retornando por el mismo camino que fue."""

import sys

sys.path.append("./Clases")
from stack import Stack

opposite_direction = {
    "norte": "sur",
    "sur": "norte",
    "este": "oeste",
    "oeste": "este",
    "noreste": "suroeste",
    "noroeste": "sureste",
    "sureste": "noroeste",
    "suroeste": "noreste",
}

robot_stack = Stack()
aux_stack = Stack()

robot_stack.push((5, "norte"))
robot_stack.push((2, "noreste"))
robot_stack.push((3, "este"))
robot_stack.push((1, "sur"))


def go(stack):
    while stack.size() > 0:
        move = stack.pop()
        print(f"- {move[0]} pasos hacia el {move[1]}.")
        aux_stack.push(move)

    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())


def robot_return(stack):
    return_path = Stack()

    while stack.size() > 0:
        steps, direction = stack.pop()
        aux_stack.push((steps, direction))
        inverse_direction = opposite_direction[direction]
        return_path.push((steps, inverse_direction))

    while aux_stack.size() > 0:
        stack.push(aux_stack.pop())

    print("Secuencia de retorno al punto de partida: ")
    while return_path.size() > 0:
        steps, direction = return_path.pop()
        print(f"- {steps} pasos hacia la {direction}")


print("Movimientos realizados: ")
go(robot_stack)
robot_return(robot_stack)
