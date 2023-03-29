"""
2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""
from ejercicio1 import func_max

def max_de_tres(n1:int,n2:int,n3:int):
    a = func_max(n1,n2)

    b = func_max(a,n3)

    return b
    
print(max_de_tres(10,-1,12))