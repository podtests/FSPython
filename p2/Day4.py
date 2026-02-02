#List


grades = ['a1', 'a2']
extra_students = ['natrajan', 'shilpa', 'zishan', 'priya']
name = 'jain'
students = ['akhil', 'piyush', 56, True, 'akhil',grades]

#indexing
#print(students[1])

#insertion
students.append('Haris') # added item at the end
students.insert(1, 66)
students.extend(name)

#print(students)
#remove
# students.clear()
#poped_item = students.pop(15)  # index position
#students.remove('kumar') 


#extra
#count = students.count('kumar')
#index_pos = students.index('akhil', 3, 5)  #get index pos of the searched item
#students.sort()


#print(extra_students)
#extra_students.sort()  # ascending order
#print(extra_students)


secondlist = extra_students
thirdlist = extra_students.copy()

print(extra_students)
print(secondlist)
print(thirdlist)

extra_students.append('logesh')

print(extra_students)
print(secondlist)
print(thirdlist)

extra_students[0] = 'Yash'
print(extra_students)

#extra_students.sort(reverse=True)
#print(extra_students)
#extra_students.reverse()
#print(extra_students)

#print(index_pos)
#print(poped_item)


