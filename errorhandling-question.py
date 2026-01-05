# 9. Write a program to handle a ValueError when the user enters invalid input (for
# example, entering letters instead of a number).
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")
# 10. Write a program to handle invalid input (user enters a string instead of a
# number).
try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("Invalid input! You must enter a number, not a string.")
# 11. Write a program that handles file not found error while opening a file.
try:
    file = open("samples.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist.")
# 12. Write a program using try , except , and else blocks.
try:
    a=int(input("enter the number:"))
    res=10/a
except ZeroDivisionError:
    print("Cant divide by zero")
else:
    print(f"result:{res}")
# 13. Write a program using try , except , and finally to ensure a message
# "Program ended" is always printed.
try:
    a=int(input("enter the number:"))
    res=10/a
except ZeroDivisionError:
    print("Cant divide by zero")
else:
    print(f"result:{res}")
finally:
    print("Program ended")
# 14. Write a program that catches multiple exceptions using multiple except
# blocks.
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numeric values.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception:
    print("Error: Something went wrong.")
# 15. Write a program that raises a custom error when the user enters a negative
# number.
try:
    num = int(input("Enter a number: "))
    
    if num < 0:
        raise ValueError("Negative numbers are not allowed.")
    
    print("You entered:", num)

except ValueError as e:
    print("Error:", e)


