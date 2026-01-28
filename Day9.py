# def add(a, b):
#     return a+b

# print(type(add))


class Employee:

#not a instance variable
#class variables[these are shared resources]
    #cardid: int
    employeeCompanyName: str

#constructor
    def __init__(self, cardid, name):  
        #all your instance variables need to be initialized inside constructor only
        self.cardid =  cardid      
        self.name = name
        print(f'{self.name}[{self.cardid}]: Employee class contructor called & object created!')

# instance method
    def getPunchInTime(this, startTime, EndTime):
        #name = 'Akhil Jain' # local variable
        diff = EndTime - startTime
        return f'{this.cardid} user spent time as {diff}'



#class method
    @classmethod
    def updateCompanyName(cls, companyName ):
        # Employee.employeeCompanyName  = companyName
        cls.employeeCompanyName = companyName


#object creation
e1 = Employee(1, 'Akhil Jain')
e2 = Employee(2, 'Abilash')
res = e1.getPunchInTime(80, 100)
#e1.employeeCompanyName = 'infosys'
#Employee.employeeCompanyName = 'infosys'

e1.updateCompanyName('PodTest')
print(e1.employeeCompanyName)
print(e2.employeeCompanyName)
    




