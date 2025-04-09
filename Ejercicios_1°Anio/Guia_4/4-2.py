"""Mostrar si un número es mayor que 10."""

def mayor(num):
    if(num > 10):
        print(f"El número {num} es mayor que 10.")
    elif (num < 10):
        print(f"El número {num} es menor que 10.")
    else:
        print(f"El número es {num:.0f}.")
    

num = float(input("Ingrese un número: "))

print(mayor(num))