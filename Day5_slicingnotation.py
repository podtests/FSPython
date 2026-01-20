name = 'PodTest'
guest_list = ['Shilpa', 'Haris', 'Nivetha', 'Akhil']
guest_set = {'Shilpa', 'Haris', 'Nivetha'} #doesn't work
guest_tuple = ('Shilpa', 'Haris', 'Nivetha', 'Akhil')
employee = {
    'name': 'Akhil',
    'age': 30,
    'dob': 67
}


print(list(employee.items())[1::2])

# slicing notation
# print(name[2:])
# print(name[:2])
# print(name[::2])

# print(name[6::-1]) # check this 


# print(guest_list[1:len(guest_list): 2])

#print(guest_list[1:3:1])
#print(guest_tuple[1:3:1])
# print(guest_set[1]) Not allowed
#print(guest_tuple[1])

