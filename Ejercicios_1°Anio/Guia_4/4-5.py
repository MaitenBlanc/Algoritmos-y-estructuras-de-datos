"""Ingresar un par de valores, emitirlos, y si ambos son positivos, emitir también su promedio."""

def promedio(n1, n2):
    prom = (n1 + n2) / 2
    return prom
    
def mostrar(n1, n2):
    if (n1 > 0 and n2 > 0):
        print(f"Promedio = {promedio(n1, n2)}")
    else: 
        if (n1 < 0 and n2 > 0):
            print(f"{n1} es negativo, no se puede emitir el promedio.")
        elif (n2 < 0 and n1 > 0): 
            print(f"{n2} es negativo, no se puede emitir el promedio.")
        else: 
            print(f"{n1} y {n2} son negativos, no se puede emitir el promedio.")
            

val_1 = int(input("Ingrese valor 1: "))
val_2 = int(input("Ingrese valor 2: "))

print(f"Valor 1: {val_1}")
print(f"Valor 2: {val_2}")
mostrar(val_1, val_2)