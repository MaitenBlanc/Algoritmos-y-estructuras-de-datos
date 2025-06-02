"""Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
matriz de [n x n], solo se puede mover de a una casilla a la vez (no se puede mover en diagonal)
y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo."""

# Datos
# 1 - camino válido, 0 - pared
# movimientos válidos: arriba, abajo, izq, der
# si es pared - retrocede
# salida de (0,0) y fin a (n-1, n-1)


def valid_path(lab, x, y, n, visited):
    return 0 <= x < n and 0 <= y < n and lab[x][y] == 1 and not visited[x][y]


def solve_lab(lab, x, y, path, visited):
    n = len(lab)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]      # Abajo, der, arriba, izq

    # base
    if x == n - 1 and y == n - 1:
        path.append((x, y))
        return True

    visited[x][y] = True
    path.append((x, y))

    for dx, dy in directions:
        new_x, new_y = x+dx, y+dy
        
        if valid_path(lab, new_x, new_y,n ,visited):
            if solve_lab(lab, new_x, new_y, path, visited):
                return True
            
    # Retroceder
    path.pop()
    return False

def exit_lab(lab):
    n = len(lab)
    visited = []
    path = []
    
    for i in range(n):
        row = []
        for j in range(n):
            row.append(False)
        visited.append(row)
    
    if solve_lab(lab, 0, 0, path, visited):
        print("Camino encontrado: ")
        for p in path:
            print(p)
    else:
        print("No hay salida del laberinto.")
        
        
lab = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 1, 1]
]

exit_lab(lab)