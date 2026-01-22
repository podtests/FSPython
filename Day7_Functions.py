
#Defult parameter : make your parameter optional
# def hello( lastname: str, middlename: str, firstname: str ='World'  ) -> None: 
#     """This Hello Function helps to print your FullName
#     Also it helps to say Hello!
#     """
#     print(f'Hello {firstname} {middlename} {lastname}!')


# #calling a function
# #arguments
# hello()

#Args parameters
#  *args Arguments


# def hello(*args):
#     for i in range(len(args)):
#         print(f'index {i} is having value as {args[i]}')

# hello()   #  args = ()
# hello('Akhil')  # args = ('Akhil')
# hello('Akhil', 'Jain')  # args = ('Akhil', 'Jain')
# #hello('Akhil', 'kumar', 'Jain')

#Keyword Parameters
# **kwargs Arguments

# def hello(**kwargs):
#     for i, key in enumerate(kwargs):
#         print(f'{i} index has key as "{key}" and value as "{kwargs[key]}"')


# hello(firstname='Akhil', lastName= 'jain')   

#dict
# {
#     firstname='Akhil', 
#  lastName= 'jain'
#  }


print('akhil', 'jain',sep=':' , end=' ')
print('podtest', 'students',sep=':' , end=' ')