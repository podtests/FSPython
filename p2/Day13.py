class A:

    def m1(self, a):
        pass

    def m2(self, a):
        pass

a = A() # this shouldn't have been alloowed
# abstarct classes should only be allowed to be inherited & nothing else
a.m1(7)