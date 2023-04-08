'''
Ejercicio 5
Construir un pequeño programa que convierta números binarios en enteros.
'''

def convert(binary:str):
    
    decimal = 0
    
    for i in range(len(binary)):
        
        if binary[len(binary)-i-1] == '1':
            
            decimal += 2 ** i
       
    return decimal

print(convert("10011011"))