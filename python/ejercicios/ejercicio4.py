'''
4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
'''
def is_a_vowel(character):
    
    character = str(character).lower()
    
    dictionary = {'a','e','i','o','u'}
    
    return character in dictionary

while True:
    
    character = input("enter a character => ")
    response = is_a_vowel(character)
    print(response)
    
    if(not response):
        break