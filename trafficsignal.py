# Write a Python program that acts as a traffic light controller with the following
# conditions:
# The program should accept either a color or a number as input.
# Use the mapping:
# 1 or "red" → Stop and wait for 60 seconds
# 2 or "yellow" → Ready and wait for 5 seconds
# 3 or "green" → Go and drive safely
# The program should handle inputs in a case-insensitive manner.
# If the input does not match any valid color or number, display
# Invalid signal .
signal = input("Enter traffic signal (1/2/3 or red/yellow/green): ").strip().lower()

if signal == "1" or signal == "red":
    print("Stop and wait for 60 seconds")

elif signal == "2" or signal == "yellow":
    print("Ready and wait for 5 seconds")

elif signal == "3" or signal == "green":
    print("Go and drive safely")

else:
    print("Invalid signal")