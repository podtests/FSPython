class Human:

    def __init__(self, name1, age1, city1):
        self._name = name1   #protected
        self.age = age1 # public
        self.__city = city1 #private   --> concept called Name Mangling

        # for outside world, don't access it as __city
        # _Human__city
    
    #def _printInfo(self):
    #    print(f'{self._name} has age as {self.age} and lives in city {self.__city}')
    
    def _printInfo(self, *args):
        if len(args)>0:
            print(f'{self._name} has age as {self.age} and lives in city {self.__city} with {args[0]}')
        else:
            print(f'{self._name} has age as {self.age} and lives in city {self.__city} ')


#outside the class
h1 = Human('Pavan', 30, 'Delhi')
#print(h1.age) # public 
#print(h1._name) #accessing protected variable
#print(h1.__city) # accessing private variable
#print(h1._Human__city)

h1._printInfo('I live in Dubai')
h1._printInfo('I live in Dubai', 'I want to live in India')
#h1._printInfo()
        

