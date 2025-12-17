#Write a Python program to simulate a login system with the following rules:
# The correct username is "admin" and the correct password is "1234" .
# The user is allowed a maximum of 3 login attempts.
# The username comparison should be case-insensitive.
# The password comparison should be case-sensitive.
# If the user enters correct credentials within the allowed attempts, display
# Login successful .
# If all attempts are used without success, display
# Account locked .
# After each failed attempt, display the number of attempts remaining.
correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username.lower() == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Invalid credentials")
            print("Attempts remaining:", attempts)
        else:
            print("Account locked")
