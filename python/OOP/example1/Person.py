class Person :

    def __init__(self,firstName : str,lastName : str):
        self._firstName = firstName
        self._lastName = lastName
    
    @property
    def firstName(self):
        return self._firstName
    
    @firstName.setter
    def firstName(self,firstName:str):
        self._firstName = firstName
        
    @property
    def lastName(self):
        return self._lastName
    
    @lastName.setter
    def lastName(self,lastName:str):
        self._lastName = lastName
    
    def setNickname(self,nickName :str):
        self._nickName = nickName
    
    @property
    def nickName(self):
        return self._nickName

person = Person("Julio Cesar","Castañeda")

print(person._firstName)

#person.firstName = "Alan"

#print(person._firstName)

person.setNickname("JuliuzDoe")

print(person.nickName)