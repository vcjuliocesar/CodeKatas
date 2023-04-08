'''
8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
'''
def super_position(listone:list,listtwo:list):
   
    for i in listone:
        for x in listtwo:
            if i == x:
                return True
    return False

print(super_position([1,2,3,4],[5,1,3,4,5]))