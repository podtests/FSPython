class P:
    def __init__(self, name, age, city):
        self.city = city
        self._name = name
        self.__age = age

    def m1(self):
        print('Parent way of running things!')

class C(P):    

    def m1(self):
        print('Now Child way of running things!')
        print(self.city) #public
        print(self._name) #protected
        #print(self.__age) #private
        print(self._P__age) #private
        

c = C('Akhil', 45, 'Delhi')
c.m1()
