# 16. Write a program that uses the math module to find the square root of a
# number.
import math

num = float(input("Enter a number: "))
square_root = math.sqrt(num)

print("Square root of", num, "is:", square_root)
# 17. Write a program that uses the math module to calculate power of a number.
import math

base = float(input("Enter the base number: "))
exponent = float(input("Enter the exponent: "))

result = math.pow(base, exponent)

print("Result:", result)
# 18. Write a program that uses the math module to find the factorial of a number
import math

num = int(input("Enter a number: "))

factorial = math.factorial(num)

print("Factorial of", num, "is", factorial)

