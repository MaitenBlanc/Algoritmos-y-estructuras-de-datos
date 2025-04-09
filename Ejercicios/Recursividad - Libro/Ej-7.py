"""Desarrollar un algoritmo que permita calcular la siguiente serie:
    h(n) = 1 + 1/2 + 1/3 + ... + 1/n """

def serie(num):
    if num == 1:
        return num
    
    return 1/num + serie(num - 1)
    
print(serie(3))