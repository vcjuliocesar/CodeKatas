'''
Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
'''

def search_letter(letter:str,names:list):
    
    result = 0
    
    for name in names:
        
        if letter.lower() in name[0].lower():
            
            result +=1
    
    return result


letter = input('find the letter into names:')
print(search_letter(letter,['julio','cesar','ana','alan']))