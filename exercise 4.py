
# 1Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

i = 0

while i <= 1000:
    if i % 3 == 0:
        print(i)
    i = i + 1



#2 Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
print("Convesion of inches to centimeters")

while True:
    i = float(input("Enter inches : "))
    if i <= 0:
        break
    cm = i * 2.54
    print(f"{i} inches is equal to {cm} centimeters.")


# 3 Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally,..


largest = smallest = int(input("Enter numbers : "))

while True:
    number = input("Enter numbers : ")
    if not number:
        break
    number = int(number)
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number

print(f"the smallest number {smallest}")
print(f"the largest number {largest}")



# 4 Write a game where the computer draws a random integer between 1 and 10. The user tries to guess...

import random

num = random.randint(1, 10)

while True:
    guess = int(input("Guess the number between 1 and 10: "))

    if num == guess:
        print("You have guess correct number ")
        break

    elif guess < num:
        print("Too low")
    else:
        print("Too high")




#5.Write a program that asks the user for a username and password. If either or both are incorrect, the program ask th...

username = "python"
password = "rules"
max_count = 5
attempt = 0

while attempt < max_count:
    user = input("Enter username: ")
    password1 = input("Enter password: ")

    if username == user and password == password1:
        print("WELCOME")
        break
    else:
        print("TRY AGAIN")
    attempt += 1

if max_count == attempt:
    print("ACCESS DENIED")



#6Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a..
import random

N = 1_000_000
n = 0
iterator = 0

while iterator < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        n += 1
    iterator += 1
print(4*n/N)