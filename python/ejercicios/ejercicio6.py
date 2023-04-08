'''
Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
'''

def reverse(string: str):
    result = ""
    for i in range(len(string) - 1, -1, -1): #range(13,-1,-1) = 13,12,11,10,9,8,7,6,5,4,3,2,1,0,-1
        result += string[i] # string[13] = o
    return result


print(reverse("estoy probando"))