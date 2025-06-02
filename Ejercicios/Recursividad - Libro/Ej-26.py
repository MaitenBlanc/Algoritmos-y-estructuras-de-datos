"""Resuelva el problema de colocar las 8 reinas sobre un tablero de ajedrez sin que las mismas se amenacen."""

# tablero = 8x8
# Reinas movimiento = horizontal, vertical y diagonal
# "sin que se amenacen" = no pueden compartir fila, columna ni diagonal
# 0 - casillas vacías, 1 - casillas con reina
# una reina por fila y luego probar en qué columna podría ir


def place_queen(panel, row, col):
    # Verificar columna
    for i in range(row):
        if panel[i][col] == 1:
            return False

    # Verificar diagonal superior izquierda
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if panel[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Verificar diagonal superior derecha
    i, j = row - 1, col + 1
    while i >= 0 and j < 0:
        if panel[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def solve(panel, row):
    # Todas las reinas ubicadas
    if row == 8:
        return True
    
    for col in range(8):
        if place_queen(panel, row, col):
            panel[row][col] = 1     # coloca reina
            
            if solve(panel, row+1):
                return True
            panel[row][col] = 0     # retrocede para buscar otro lugar
            
    return False

def show_panel(panel):
    for row in panel:
        for value in row:
            print("1" if value == 1 else "0", end=" ")
        print()

def solve_queens():
    panel = [[0 for _ in range(8)] for _ in range(8)]
    if solve(panel, 0):
        print("Solución encontrada:")
        show_panel(panel)
    else:
        print("No se encontró solución.")

solve_queens()
