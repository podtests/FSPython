import os

print(os.getcwd())
print(__file__)
p = os.getcwd() + "\\p2"+ "\\Day16_1.py"
filename = os.path.basename(__file__)
dirname = os.path.basename(__file__)
newpath = os.path.join(os.getcwd(),"p2", "dum.py" )
newpath2 = os.path.join(os.getcwd(),"p2", "dummy.py" )
print(newpath)
# print(os.path.dirname(__file__))
# print(os.path.basename(__file__))

print(os.path.exists(newpath))
#os.rename(newpath,newpath2 )
os.remove(newpath2)
