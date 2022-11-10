# Variable = A container for a value. Behaves as the values that it contains

# We need unique names for a variable

name = "A named string"
name = "A string!"
print(name) # A string
# We can see that name was overwritten after being re declared

a_variable_name = "What datatype am I?"
print(type(name)) # <class 'str'>
# We can use type() function to determine the datatype of a variable

answer = a_variable_name + " " + name
print(answer)
# Notice the use of snake_casing

age = 28
# No quotes for Integer datatypes

age = age + 2
print(age) # 30
print(type(age)) # <class 'int'>

string_age = "18"
# Notice this is a string, we will get an error if we try to do math to a string

# string_age += 2
# print(string_age) # TypeError: can only concatenate str (not "int") to str

fixed_age = int(string_age)
fixed_age += 2
print(fixed_age) # 20
# You can use the int() function to convert string to integer

restring = str(fixed_age)
print(type(restring)) # <class 'str'>
# Vice-versa we can use the str() function to convert an integer to a string

# print("You are " + fixed_age + " years old!") # TypeError: can only concatenate str (not "int") to str
print("Your age is " + restring + "!") # Your age is 20!

height = 250.5
print(height)
print(type(height)) # <class 'float'>
# A float is an integer (or numeric value) that contains a floating point value. 

print("Your height is: " + str(height) + "cm") # Your height is: 250.5cm

human = False
print(human) # False
print(type(human)) # <class 'bool'>
# A boolean data type: True or False. Do not put it into a string!

# Four basic data types in Python are as follows:

# String
# Integer
# Float
# Boolean




