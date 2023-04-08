'''
Ejercicio 3
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
'''

def filter_words(words:list,number:int):
    world = ''
    
    for i in words:
    
        if len(i) >= number:
    
            world += i  + ' \n'
    
    return world
    
    
    

print(filter_words(["hola","Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...","No hay nadie que ame el dolor mismo, que lo busque, lo encuentre y lo quiera, simplemente porque es el dolor.","Lorem Ipsum"],10))
    