"""
Ejercicio 1
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""

def max_in_list(numbers:list):
    
    n = numbers[0]
    
    for i in numbers:
    
        if i > n:
    
            n = i
    
    return n

print(max_in_list([1,2,4,0,5,100]))