# Create a program to find and print all numbers from 0 to 1000 (both included), that are divisible by 7 and whose digits sum are divisible by 3.

for number in range(1001):
    if (number % 3 == 0) and (number % 7 == 0):
        print(number)
