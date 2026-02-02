def say_hello():
    print('Hello PodTest!')


def sumOfTwoNumbers(a: int,b: int)-> int:
    sum1 = a*b
    return sum1
    #print(f'Sum is {sum1}')


sumOfTwoNumbers(b=10, a = 9)
sumOfTwoNumbers(0,7)
    
# Not returning anything
#c = sumOfTwoNumbers(10,2)
#c = sumOfTwoNumbers('Akhil','Jain')
c = sumOfTwoNumbers(['Akhil'], ['Jain'])
print(c, type(c))





#say_hello()
