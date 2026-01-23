# ##########################
# def findsquare(a):
#      return a**2

# # assign function to a variable
# res = findsquare

# #print(findsquare(4))
# print(res(4))


###########################3
# def f1 (variable1, variable2):
#     print('Start Execution')
#     variable1(variable2)
#     print('Stop Execution')
        
# #f1('Akhil')

# def f2(msg):
#     print(msg)

# def f3(msg):
#     print(f'Learning on {msg}')

# f1(f2, 'Akhil Jain')
# f1(f3, 'PodTest')

#####################
# Return a Function from another function


def f1(msg):  # msg = 'Akhil'   Parent scope
    print(f'f1 called me as {msg}')
    def f2():
        print(f'Hello f2 called me as {msg}')
    return f2

#f2("Akhil") # not allowed
res = f1("Akhil")


# res = ():
    #   print(f'Hello f2 called me as {msg}')

res()
#res('PodTest')


