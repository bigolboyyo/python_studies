# Type Casting = converting the data type of a value to another data type

# We have 3 different variables set to 3 different data types

x = 1 # int
y = 2.1 # float
z = "3" # str

print(type(str(x))) # <class 'str'>
print(type(int(y))) # <class 'int'>
print(type(float(z))) # <class 'float'>

# str()
print(x * 3) # 3
print(str(x) * 3) # 111

# int()
print(y + y) # 4.2
print(int(y) + int(y)) # 4

# float()
print(z * 3) # 333
print(float(z) * 3) # 9.0