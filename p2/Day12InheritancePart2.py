class A:
    def m1(self):
        print('A:m1 is called')

class B:
    def m1(self):
        print('B:m2 is called')

class C(A, B):
    def m3(self):
        print('C:m3 is called')


c = C()
c.m3()
c.m1()



#mro  method resolution order
#print(C.mro())