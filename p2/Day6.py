age = 19

#conditional logic

# if age<=18:
#     print('User is not an adult')
# elif age >18 and age <60:
#     print('user is an adult') 
# else:
#     print('user is a senior citizen')


# guest_list = []
# if guest_list:
#     print('My Guest list is ready, I can invite now')
# else:
#     print('List not ready, can\'t invite')

# Looping
# i = 0
# while i<10:
#     i= i+1
#     print('I will do my homework next time onwards!')
# print('while loop finished!')

# guest_names = ['Akhil', 'Abhishek', 'Dhrumil']


# # # for loopis working based on values in interable
# for name in guest_names:
#     print(f'Guest name is {name}')

# guest_names = ['Akhil', 'Abhishek', 'Dhrumil']
#         #       0           1           2
# for index, name in enumerate(guest_names):   # index pos, value
#     if  name == 'Abhishek':
#         continue
#     print(f'{index}: Guest name is {guest_names[index]}')     
   



# print 10 times
# for i in range(10):
#      print(f'{i}: I will do my homework next time onwards!')

# for i in range(10,0,-1):
#     print(i)

# Write a logic to print your list in reverse order

# l1 = ["a", 12, "b"]
# l2 = ["a", 12, "b"]
# l3 = l1

# if l1 == l2:  # comparing content, not the memory
#     print('Object match')
# else:
#     print('object doesn\'t match')


l1 = ["a", 12, "b"]
#if l1.count("a") == 1:
if "c" in l1:
    print("c exist in list")
else:
    print("c doesn't exist in the list")
