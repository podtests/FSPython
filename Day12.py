class parent:

    # def __init__(self):
    #    print(f' parent is called!')
    

    def __init__(self, name):
        self.name = name
        print(f'{name} parent is called!')

    def m1(self):
        print(f'{self.name} m1 method of parent is called!')

class child(parent):

    # def __init__(self):
    #     print(f' child is called!')

    def __init__(self,age, name):
        self.age = age                
        print(f'{name} child is called!')
        #self.name = name
        #parent.__init__(parent, name)
        super().__init__(name)

    def m2(self):
        print(f'{self.age} m2 method child is called!')

# p1 = parent()
# p1.m1()

#c1 = child()
c1 = child(30,'Akhil') #constructor gets called
#c1.m2()
c1.m1()
# c1.m2()
# c1.m1()

