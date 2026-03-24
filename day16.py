# file = open("dummyfile.txt", "a+", encoding = "utf-16")
# file.write("Hi My Name is Akhil Jain!")
# file.seek(0)
# content = file.read()
# print(content)
# file.close()

#content = file.read()
#print(content)

# with open("dummyfile.txt", "a+", encoding = "utf-16") as file:
#     file.write("Hi My Name is Podtest!")
#     file.seek(0)
#     content = file.read()
#     print(content)
#     #file.close()

# import os

# print(os.getcwd())

from pathlib import Path

# print(Path.cwd())
# print(__file__)

path = Path(__file__)

# print(path.exists())
# print(path.parent) # folder location
# print(path.name)  # file name with extension
# print(path.stem) #only file nmae
# print(path.suffix) #fil extension

# print()
# filepathtoread = path.joinpath(path.parent,"dummyfile.txt")
# #content = Path(filepathtoread).read_text(encoding='utf-16')
# Path(filepathtoread).write_text("today is Friday!")
# content = Path(filepathtoread).read_text(encoding='utf-8')
# print(content)

pth = path.joinpath(path.parent, "location.json")
print(pth)
with open(pth, "r", encoding="utf-8") as f:
    json_text = f.read()
print(json_text)