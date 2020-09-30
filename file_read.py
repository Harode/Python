myfile = open("Files/fruits.txt")
content = myfile.read()
print(myfile.read())
print(myfile.read())
print(content)
print(content)
myfile.close()
#print(myfile.read())
# New way to code this file open and it will close file object in memory
# so no need to explicitly mention close clause.
with open("Files/fruits.txt") as myfile:
    content = myfile.read()

print("By new method to print file content")
print(content)