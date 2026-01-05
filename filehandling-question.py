# 1. Write a program to create a file named data.txt and write the text
# "Hello File Handling" into it.
# file = open("data.txt", "w")
# file.write("Hello File Handling")
# file.close()
# 2. Write a program to read the contents of a file data.txt and display it on the
# screen.
# file=open("data.txt","r")
# print(file.read())
# file.close()
# 3. Write a program to append the text "Python is awesome" to an existing file.
# file = open("data.txt", "a")
# file.write("Python is awesome")
# file.close()
# 4. Write a program to count the number of lines present in a file.
# with open("data.txt","r")as file:
#    lines=len(file.readlines())
#    print("No of lines:",lines)
# 5. Write a program to count the number of words in a file.
# file = open("data.txt", "r")
# data = file.read()
# words = data.split()
# print('Number of words in text file :', len(words))
# 6. Write a program to copy the contents of one file into another file.
# with open("data.txt","r")as file, open("second.txt","w") as sec:
#     for lines in file:
#         sec.write(lines)

# 7. Write a program to read a file and print only the lines that contain the word
# "Python" .
# with open("data.txt","r") as file:
#     for line in file:
#         if "Python" in line:
#             print(line,end="")

# 8. Write a program that reads numbers from a file and calculates their sum.
# total=0
# with open("numbers.txt","r")as num:
#     for n in num:
#         total+=int(n)
# print("Sum of numbers:",total)

