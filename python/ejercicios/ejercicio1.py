"""
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def func_max(n1:int,n2:int):
    if n1 > n2:
        return n1
    else:
        return n2
    

print(func_max(-4,-3))