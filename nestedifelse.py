'''
# Check if a number is positive, negative, or zero
num = int(input("Please enter a number  : "))
if num > 0 :
    print("positive number")
elif num < 0:
    print("negative number")
else:
    print("Zero")
# Check if a number is even or odd
num = int(input("Please enter a number  : "))
if num % 2 == 0:
    print("Even number")
else: 
    print("Odd number")
# Find the largest of two numbers
num_1 = int(input("Please enter a first number: "))
num_2 = int(input("Please enter a second number: "))
if num_1 == num_2:
    print(f"{num_1} and {num_2} is the same numbers.")
elif num_1 > num_2:
    print(f"{num_1} is the larhest number.")
else:
    print(f"{num_2} is the largest number.")

# Grade classification
score = int(input("Please enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("Fail")

# Check if a person is eligible to vote   
age = int(input("PLease enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("not eligible")


# Simple password checker
Stores_password = "Kanani123@#"
password = input("Please enter your password: ")
if password == Stores_password:
    print("Access granted")
else:
    print("Access denied")


# Number in range check
num = int(input("Please enter a number: "))
if num in range(10, 20):
    print("Number is in the range")
else:
    print("Number is not in the range")
'''
# Leap year checker
year = int(input("Please enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

