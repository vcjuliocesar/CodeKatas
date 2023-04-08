'''
Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
'''

def how_many_years(year:int,people:dict):
    years = ''
    
    for i in people:
        years += f'{i} this year is {(year-people[i])} years old \n '    
        
    return years.strip()


people = {}

current_year = input("Enter current year : ")

while True:
    
    name = input("Enter name: ")

    year_born = input("Enter year born: ")
    
    people[name] = int(year_born)
    
    if len(people) == 3:
        break
    
print(how_many_years(int(current_year),people))