"""
3 - Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud(n):
    convert = list(n)
    
    long = 0
    
    for i in convert:
        long +=1
    
    return long

print(longitud([1, 3, 5, 7, 9]))
print(longitud("hola"))
        
    
    