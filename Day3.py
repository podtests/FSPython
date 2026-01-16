myIntro = "akhil is teaching on PodTest ; we is learning Python!; Hi Iwe are done for today"

#casing
print(myIntro.capitalize())
print(myIntro.upper())
print(myIntro)
myIntro.casefold()
myIntro.islower()
myIntro.lower()

# indexing
print(myIntro.count('is', 15 ))
print(myIntro.find('Selenium')) 
#print(myIntro.index('Selenium'))

# 
neIntro = myIntro.replace('Python', 'AI')  # returns a copy
#myIntro.endswith()
print(myIntro.upper().startswith("AKHIL"))

print(myIntro.split(";"))

#print(neIntro)
#print(myIntro)










# petname = firstname
#             #01234

# lastname = "Akhil"
# age = 30
# have_passport = True

# #print(firstname[0])

# #firstname[0] = "V"  # immutable
# #firstname = "Vkhil"  #5
# #print(firstname)

# # Python: Function  & Method

# #print(len(firstname))

# #equality
# if firstname is lastname: # == compares content, is compares actual object
#     print("Equal")
# else:
#     print("Not Equal")

# # convert to string

# age = 30
# agestring = str(age)
# str(None)
# str(True)


# # # concatenation
# # print(type(firstname))
# # fullname = firstname+" "+lastname
# # intro = firstname+" "+lastname+", my age is "+str(age) +", passport?:"+str(have_passport )

# # new_intro = f'{firstname} {lastname} , my age is  {age} , passport?: {have_passport}'
# # print(new_intro)

# # #print("hello",2,type(2))

