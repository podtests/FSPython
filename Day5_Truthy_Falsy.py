is_valid = True # False


#Truthy
name = 'Akhil'
lastname = ''  # false

#Falsy
#  '', 0, 0.0, False, [], (), {}

# Tryuthy
# all other things are True


bool_val = bool(lastname)  # false

#print(bool(lastname))

if lastname:
    print('We speak Truth')
else:
    print('Sometimes we speak false as well')