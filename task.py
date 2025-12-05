#Given a string "hello", turn it into "HELLO" using only string functions. 
s="hello"
print(s.upper())
#Check if "cat" exists inside "concatenate" (no loops). 
str="concatenate"
r=str.find("cat")
print("Found in ",r,"-rd position")
#Replace "python" with "🐍" in "i love python" 
st="i love python"
print(st.replace("python","🐍"))
#Count how many times "a" appears in "bananaa" without using a loop. 
a="bananaa"
print(a.count('a'))
# Given " space me ", remove all spaces from both ends only.
b=" space me "
res=b.strip()
print(res) 
#From "nikthebestie", extract "best" using slicing only. 
a="nikthebestie"
print(a[-6:-2])
# Reverse the string "abcdef" without using a loop. 
c="abcdef"
print(c[::-1])
#Check if "madam" is a palindrome
d="madam"
f=d[::-1]
print(d==f,"- "+d+" is palindrome")
