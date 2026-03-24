
# emp = {"name": "Akhil Jain" , "age": 67, "role": "Engineer"}

# empjson = '{"name": "Akhil Jain" , "age": 67, "role": "Engineer"}'

# class Employee :
#     def __init__(self, name : str, age: int, role: str):
#         self.name = name
#         self.age = age
#         self.role = role


# e : Employee = Employee(True, 67, "Engineer")   
# # missing implicit type safety, data validation which you could apply on these values

# #e1 : Employee = Employee("Akhil Jain", 67, "Engineer")     

# print(e.name , e.age, e.role)


#################################
from typing import Optional

from pydantic import BaseModel, Field

#Rules:
#Inherit BaseModel Class
# No Need to create constructor 
# Create variables & mention the data types
# while craeting the object, use Keyword argument assignment


# class EmployeeNew(BaseModel):
#     name: str
#     age: int = Field(gt=50)
#     role: Optional[str] = 'Engineer'


#e = EmployeeNew('Akhil ', 40, 'Engineer')  #positional arguments
#print(e)


#keyword arguments
#e = EmployeeNew(name='Akhil', age=40, role='Engineer')
#print(e)

# convert the object into json
# jsonoutput = e.model_dump_json()
# print(e)
# print(jsonoutput)

# jsoninput = '{"name":"Akhil","age":67,"role":"YouTuber"}'

# #convert json into object of EmployeeType
# e1 = EmployeeNew.model_validate_json(jsoninput)
# print(e1)
# print(type(e1))


#Generate JSon Schema
# schema1 = EmployeeNew.model_json_schema()
# print(schema1)




# EmployeeNew.model_dump_json()
# EmployeeNew.model_dump()
# EmployeeNew.model_validate_json()
# EmployeeNew.model_json_schema()




import json
jsoninput = '{"name":"Akhil","age":67,"role":"YouTuber"}'

class Employee :
    def __init__(self, name : str, age: int, role: str):
        self.name = name
        self.age = age
        self.role = role

#convert this json string into python object
#r1 = json.loads(jsoninput)

e = Employee(**json.loads(jsoninput))


#convert object into json string
res = json.dumps(e)
print(res)

# {'name': 'Akhil', 'age': 67, 'role': 'YouTuber'}
# **{'name': 'Akhil', 'age': 67, 'role': 'YouTuber'}  = name='Akhil', age=67, role='YouTube'


#print(r1)
#print(e.name)



# json string to an object


# object into json




