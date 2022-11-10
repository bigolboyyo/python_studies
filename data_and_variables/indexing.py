# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "big Boyyo"

if name[0].islower():
    name = name.capitalize()
    print("Capitalize your name ya dingus!") 
    
print(name)

# [start:stop:step]
first_name = name[0:3:1].upper()
print(first_name)

last_name = name[4:].lower()
print(last_name)

print(first_name + " " + last_name)

# negative indexing
yelled_name = "BIG BOYYO!"
print(yelled_name[-1]) # !