'''
Ejercicio 7
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
'''

def find_ages(ages:tuple):
    
    # count = 0
    
    # for i in ages:
    #     if i > 20:
    #         count+=1
    print([age for age in ages if age > 20])
    count = len([age for age in ages if age > 20])
       
    return count

people_ages = []

while True:
    
    age = input('Enter age :')
    age = int(age)
    people_ages.append(age)
    
    if len(people_ages) == 10:
        break
    
print(find_ages(tuple(people_ages)))