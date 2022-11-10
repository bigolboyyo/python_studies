# String methods are built in functions we can use to manipulate strings

name = "Wesley"
alias = "boyyo"

# Find the length of our string using len()
print(len(name)) # 6

# Use find() to locate the index of a specific character
print(name.find("l")) # 3

# Capitalize, well it capitalizes our string
print(alias.capitalize()) # Boyyo

# Upper capitalizes the entire string
print(alias.upper()) # BOYYO

# Lower does the oppposite...
yelled_name = name.upper()
print(yelled_name.lower()) # wesley

# isdigit() will return True | False determining if our string is made of numerical values
print(alias.isdigit()) # False

one_two_three = "123"
print(one_two_three.isdigit()) # True

# isalpha() will return a boolean determining if our string is made of letters
print(one_two_three.isalpha()) # False
print(yelled_name.isalpha()) # True

# count() determines the number of specific characters in a string
print(name.count("e")) # 2

# replace() will do as it sounds. It replaces all found characters with our new given character
print(name.replace("e", "o")) # Wosloy

# You can multiply strings, not technically a method, but still useful
print(name * 3) # WesleyWesleyWesley