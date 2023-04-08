'''
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24
'''

def operation(data: list, fn): #[1,2,3,4], addition
    result = 0 # 0
    
    if fn == addition: #true
        result = 0 # 0
    else:
        result = 1
     
    for item in data: # item = 1 
        result = fn(item, result) # addition(2,1) = 3 
    
    return result

def addition(item, result): # 1,0
    result += item # 0+1 = 1
    
    return result #1

def multiplication(item,result): #2,1
        result *=item #1 * 2 = 2
        
        return result  #2


print(operation([1,2,3,4], addition))
print(operation([1,2,3,4], multiplication))