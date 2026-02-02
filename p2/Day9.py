# def add(a, b):
#     return a+b

# print(type(add))


class Employee:

#not a instance variable
#class variables[these are shared resources]
    #cardid: int
    employeeCompanyName: str

#constructor
    def __init__(self, cardid: str, name):  
        #all your instance variables need to be initialized inside constructor only
        self.cardid =  cardid      
        self.name = name
        print(f'{self.name}[{self.cardid}]: Employee class contructor called & object created!')

    @staticmethod
    def m4():        
        print('Hi I am here!')
        #print(name)
        #print(self.name)
        print(Employee.employeeCompanyName)

    def accessVariables(self):
        print('inside accessVariables')
        #print(self.employeeCompanyName)
        #print(cls.)
        self.m4()
        print(Employee.employeeCompanyName)
        #print(self.cardid) 
        #print(name)

# instance method
    def getPunchInTime(self, startTime, EndTime):
        #name = 'Akhil Jain' # local variable
        Employee.accessVariables()
        diff = EndTime - startTime
        return f'{self.cardid} user spent time as {diff}'



#class method
    @classmethod
    def updateCompanyName(cls, companyName ):
        # Employee.employeeCompanyName  = companyName
        cls.employeeCompanyName = companyName

    @classmethod
    def accessvariablesinsideclassmethod(cls):
        
        #print(self.name)
        #print(name)
        print('I am here!')
        #print(cls.name)
        cls.accessVariables()
        #Employee.accessVariables()

        #print(cls.name) #access instance variable


#object creation
e1 = Employee(1, 'Akhil Jain')
#e1.m4()
Employee.employeeCompanyName= 'PodTest'
e1.accessVariables()
#Employee.m4()
#Employee.employeeCompanyName = 'PodTest'
#e1.accessVariables()
#e1.accessvariablesinsideclassmethod()
#Employee.accessvariablesinsideclassmethod()
#e1.accessVariables()
#print(e1.name)
#e1.getPunchInTime(78, 90)
    




