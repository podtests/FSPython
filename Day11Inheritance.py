class Car:

    def __init__(self, wheels, jacks):
        print(f'Car Constructor running {wheels}  {jacks}')

    # def __init__(self):
    #     pass

    # def __init__(self,wheelCount, doors  ):
    #     self.wheelCount = wheelCount
    #     self.doors = doors
    
    def drive(self):
        print('Car is being Driven by the user')


class Maruti(Car):

    # def __init__(self, doors):
    #     #Python will call the default constructor in Car class
    #     #Car()
    #     print(f'Maruti Constructor running {doors}')

    def price(self):
        print('Mariti is Expensive')

# alto = Car()
# alto.drive()

baleno = Maruti(4)
#baleno.price()
#baleno.drive()