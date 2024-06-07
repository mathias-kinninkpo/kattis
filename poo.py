class Person():
    n_instance = 1

    def __init__(self, nom, prenom, age):
        self._nom = nom
        self.__prenom = prenom
        self.__age = age
        
        
    def setAge(self, age):
        self.__age = age
    
    def getAge(self):
        return self.__age

class Hummain():
    
    def __init__(self, taille):
        self.taille = taille
    
    
class Homme(Person, Hummain):
    
    def __init__(self, nom, prenom, age, taille):
        Person.__init__(self, nom, prenom, age)
        Hummain.__init__(self,taille)
        self.sexe = 'M'
    
    def getNom(self):
        return self._nom
    
    def getPrenom(self):
        return self.__prenom
    
    

if __name__ == '__main__':
    
    person = Homme('KINNINKPO', 'Mathias', '17', '1m77')
    
    person.setAge(20)
    
    print(person.getAge())
    print(person.taille)
        

