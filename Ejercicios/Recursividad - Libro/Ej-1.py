"""Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un
número dado."""

def fib(num):
    if num == 0 or num == 1:
        return num
    else: 
        return fib(num-1) + fib(num-2)
    
for i in range(6):
    print(fib(i))