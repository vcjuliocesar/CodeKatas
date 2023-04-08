'''
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
'''

def is_palindrome(text:str):
    
    for i in range(len(text)):
        
        if text[i] != text[len(text)-i-1]: #text[4] != text[0] r != r
            return False
        
    return True


print(is_palindrome("radar"))
print(is_palindrome("ojo"))
print(is_palindrome("python"))