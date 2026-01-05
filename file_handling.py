#file operation-read
# file = open("sample.txt", "r")
# print(file.read())
# file.close()

#readline() Method
# file = open("sample.txt", "r")
# line1 = file.readline()
# print(line1)
# file.close()

#readlines() Method
# file = open("sample.txt", "r")
# line1 = file.readlines()
# print(line1)
# file.close()

#write() Method
# file = open("sample.txt", "w")
# file.write("Hello, World!")
# file.close()

#writelines() Method
# file = open("sample.txt", "w")
# lines = ["Hello\n", "Welcome to Python file handling\n"]
# file.writelines(lines)
# file.close()

# Appending Data
# file = open("sample.txt", "a")
# file.write("Appended text.\n")
# file.close()

#using with statement
# with open("sample.txt","r") as file:
#     content=file.read()
#     print(content)

#file positioning with seek and tell
# with open("sample.txt","r")as file:
#     content=file.read()
#     pos=file.tell()
#     print(pos)

# file = open("sample.txt", "r")
# file.seek(5) 
# print(file.read())
# print(file.tell())
# file.close()
