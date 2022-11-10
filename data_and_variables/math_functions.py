# MATH TIME
# https://docs.python.org/3/library/math.html

# We need to make sure to import our math module
import math

# The math module has access to many functions via `math.*function*`

pi = math.pi
negative_pi = -math.pi

print(pi) # 3.141592653589793

# round will round to the nearest whole number: high or low
print(round(pi)) # 3

# ceil rounds up
print(math.ceil(pi)) # 4

# floor rounds down
print(math.floor(pi)) # 3

# abs() or absolute value of a number = tells you how far away the number is from ZERO
# So for example, passing in a negative number will give you a positive number
print(abs(negative_pi)) # 3.141592653589793

# pow() will raise a base number to a power. First argument is our number to manipulate, the 2nd argument being the power to raise it by
print(pow(pi, 2)) # 9.869604401089358

# sqrt() will find the Square Root = a number that when multiplied by itself equals a given number
print(math.sqrt(pi)) # 1.7724538509055159

# the floor of the square root of a number
print(math.floor(math.sqrt(420))) # 20

x = 1
y = 2
z = 3

# max() will find the largest of the return values passed in
print(max(x,y,z)) # 3

# min() will find the lowest of the return values passed in
print(min(x,y,z)) # 1