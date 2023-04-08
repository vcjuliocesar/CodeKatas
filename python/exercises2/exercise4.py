'''
Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
'''


def how_many_capital_letters(sentence:str):
    
    count = 0
    
    for i in sentence:
        
        if i.isupper():
    
            count += 1
    
    return f'The string {sentence} has {count} capital letter'
        

sentence = input("write a string -> ")

print(how_many_capital_letters(sentence))