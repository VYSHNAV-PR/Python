n = int(input("Enter a decimal number: "))

binary = ""

while n > 0:
    r = n % 2
    binary = str(r) + binary
    n = n // 2

print("Binary number:", binary)

s = input("Enter String:")

words = s.split()
max_count = 1
result = "-1"

for word in words:
    for ch in word:
        count = word.count(ch)
        if count > max_count:
            max_count = count
            result = word

print(f"result:{result}")