from typing import TypedDict
from dataclasses import dataclass

# class Person(TypedDict):
#     name: str
#     age: int

# p1: Person = {"name": "Akhil",  "Citizenship": "Indian"}

# print(p1)

# p2 = { "name": "Akhil",  "Citizenship": "Indian"}
# print(p2)

# @dataclass
# class Employee:
#     name: str
#     age: int

#     # def __init__(self, name, age):
#     #     self.name = name
#     #     self.age = age

#     # def __repr__(self):
#     #     return self.name

#    # def __eq__(self):


# e1: Employee = Employee(name= "Akhil", age=78)
# print(e1)

##
#dataclass


# def printSomething(vara: dict):
#     print(vara)

# #printSomething({"name": "Akhil", "age": 78}) #str


# printSomething("Akhil")

##################
# from typing import Literal

# # Only "red", "green", or "blue" are valid
# def set_color(color: Literal["red", "green", "blue"]) -> None:
#     print(f"Color set to {color}")

# #set_color('green')   # ✅ valid
# set_color("yellow") # ❌ type checker flags this

#######
#annotated: add metadata info

#from typing import Annotated

# def setAge(age: Annotated[int, "age must be positive"]):
#     print(age)

# setAge()

# from typing import Annotated
# from pydantic import BaseModel, Field

# class Person(BaseModel):
#     name:  Annotated[str,   Field(min_length=1, max_length=50)]
#     age:   Annotated[int,   Field(ge=0, le=150)]       # 0 <= age <= 150
#     email: Annotated[str,   Field(pattern=r".+@.+")]
#     price: Annotated[float, Field(gt=0)]  

# p = Person(name="")
# print(p)


#Operator

# import operator
# res = operator.add("Akhil","Jain")
# print(res)


#reduce

from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]   #Many --> Single value


def add(a,b):
    return a+b

result = reduce(add, numbers)   # 10,5
print(result)  # 15




# def add (a,b):
#     return a+b

# res = add(2,3)
# print(res)