import re
#re.seearch()
# text="Hello world"
# print(re.search("world",text))

#re.match(pattern, string)
# text="Hello world"
# print(re.match(r"Hello",text))
# print(re.match(r"world",text))

#re.findall(pattern, string)
# txt="i have 3 mangoes and 4 apples"
# print(re.findall(r"\d",txt))
# txt="i have 23 mangoes and 45 apples"
# print(re.findall(r"\d+",txt))
# txt="i have 3 mangoes and 4 apples"
# print(re.findall(r"\D+",txt))

# re.finditer(pattern, string)
# for match in re.finditer(r"\d",txt):
#     print(match.group(),"at",match.start())

#re.sub(pattern, repl, string)
# text = "Hello 123, welcome 456!"
# print(re.sub(r"\d+","numbers",text))
# print(re.sub(r"\D+","numbers",text))

#re.split(pattern, string)
# friuts="apple,banana,cherry;lemon"
# print(re.split(r"[,;]",friuts))

#grouping and capturing
# text = "John: 34, Alice: 45, Bob: 23"
# print(re.findall(r"(\w+): (\d+)",text))

#Compiling Regex
# pattern=re.compile(r"\d+")
# text="123 apples and 456 cherries"
# print(pattern.findall(text))

#Regex Flags-re.IGNORECASE (or re.I )
# text="Hello"
# print(re.search(r"hello",text,re.IGNORECASE))

#re.MULTILINE (or re.M )
text = """first line
second line
third line"""
print(re.findall(r"s\w+",text,re.MULTILINE))
print(re.findall(r"\w+e$",text,re.MULTILINE))

#re.DOTALL (or re.S )
# t="Hello@123World"
# print(re.search(r"Hello.*World",t,re.DOTALL))
