# for loop = a statement that will execute its block of code a limited amount of times

# while loop = unlimited
# for loop = limited

# Give us each number in the range of 1-10
for i in range(10):
    print(i + 1)
    
# range of (start, stop, step)
for i in range(50, 100 + 1, 2):
    print(i)
   
# each element (letter) in the string 
for i in "BigBoyyo":
    print(i)
    
# List
fruits = ["Apple", "Banana", "Grape", "Mango", "Watermelon" ]

# For each letter of each element in the fruits list
for i in fruits:
    for c in i:
        print(c)

# time module
import time

time.sleep(1)

# clear console with os module
import os

os.system('clear')

# Countdown program


# range(start, stop, step)
for seconds in range(10, 0-1, -1):
    print(seconds)
    # From the time module, we await 1 seconds
    time.sleep(1)

print("Happy New Year!")