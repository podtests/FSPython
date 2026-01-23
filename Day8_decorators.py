def f1():
    print('Hello World!')

def f2():
    print('My name is PodTest')

# def f3(val1):
#     print('$$$$$$$$')
#     val1()
#     print('*********')
#     val1()


# passing function as an argument

def f4(val1):    
    
    
    def f5():
        print('$$$$$$$$')

# inner function remebers the variable provided from the parent scope (Closure)
        val1()
        print('*********')
        val1()
# return a func from a func
    return f5


#f1()

f1 = f4(f1)

f1()

#@f4
#f1()

#f1()
