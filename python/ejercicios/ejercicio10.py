'''
10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
'''

def procedure(numbers:list):
    
    result = ''
    
    for i in numbers:
        
        result += '*' * i + ' \n'
    
    return result.strip()
    
print(procedure([4, 9, 7]))