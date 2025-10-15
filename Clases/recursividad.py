def factorial(num):               # complejidad: n
    if num == 0:
        return 1
    else:
        return num* factorial(num-1)
    
    
def factorial_iterativo(num):
    acum = 1
    while num != 0:
        acum *= num
        num -= 1
    return acum

# result = factorial_iterativo(5)
# print(result)

# FIBONACCI
# fib(n) = fib(n-1) + fib(n-2)

def fib(num):
    if num == 0 or num == 1:
        return num
    else: 
        return fib(num-1) + fib(num-2)
    
# print("Fibonacci recursivo")
# for i in range(6):
#     print(fib(i))
    

def fib_iterativo(num):               # complejidad: n
    if num == 0 or num == 1:
        return num
    
    result_1 = 0
    result_2 = 1
    result = 0
    for i in range(2, num+1):
        result = result_1 + result_2
        result_1 = result_2
        result_2 = result
        
    return result
        
# print("Fibonacci iterativo")
# print(fib_iterativo(100))

numbers = [1,3,4,5,6]

def busqueda_binaria_iterativa(array, value):
    first = 0
    last = len(array) - 1
    position = -1
    
    while first <= last and position == -1:
        middle = (first + last) // 2
        
        if array[middle] == value:
            position = middle
        elif array[middle] < value: 
            last = middle - 1
        else: 
            first = middle + 1
            
    return position

# print(busqueda_binaria_iterativa(numbers, 0))
# print(busqueda_binaria_iterativa(numbers, 8))
# print(busqueda_binaria_iterativa(numbers, 4))

def busqueda_binaria_recursiva(array, value, first, last):
    middle = (first + last) // 2
    
    if first >= last:
        return -1
    elif array[middle] == value:
        return middle
    else:
        if array[middle] > value:
            return busqueda_binaria_recursiva(array, value, first, last - 1)
        else: 
            return busqueda_binaria_recursiva(array, value, first + 1, last)
        
print(busqueda_binaria_recursiva(numbers, 4, 0, len(numbers)))
print(busqueda_binaria_recursiva(numbers, 5, 0, len(numbers)))
print(busqueda_binaria_recursiva(numbers, 10, 0, len(numbers)))
print(busqueda_binaria_recursiva(numbers, 0, 0, len(numbers)))