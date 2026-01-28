class Father:
    def __init__(self, lastName):
        self.lastName = lastName
    
    def skills(self):
        print('Father: strictness')

class Mother:
    def __init__(self, firstName):
        self.firstName = firstName
    
    def skills(self):
        print('Mother: kindness')

class child(Mother,Father):
    def __init__(self, fn, ln):
        print('Hi')
      #  self.firstName=fn
      #  self.lastName=ln
    
    def printname(self):
        print(f'{self.firstName} {self.lastName}')

c1 = child('Akhil', 'Jain')
c1.printname()