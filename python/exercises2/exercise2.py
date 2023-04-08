'''
Ejercicio 2
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
'''

def longer(words:list):
    long = 0
    word = ''
    
    for w in words:
        if len(w) > long:
            word = w
            long = len(w)
            
    return word


print(longer(["hola","Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...","No hay nadie que ame el dolor mismo, que lo busque, lo encuentre y lo quiera, simplemente porque es el dolor.","","Lorem Ipsum"]))