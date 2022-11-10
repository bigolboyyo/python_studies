# Slicing = create a substringb by extracting element from another string
# indexing[] or slice()
# indexing = [start:stop:step]

name = "Big Boyyo"

# INDEXING

first_name = name[0:3:1]
print(first_name)

last_name = name[4:9:1]
print(last_name)

full_name = first_name + last_name
print(full_name)

# If you leave the first [start] empty, Python will assume from the 0 (zeroeth) position
shortcut_first = name[:3]
print(shortcut_first) # Big

# Leaving the second [stop] empty, Python will assume til the end of the string
shorcut_last = name[4:]
print(shorcut_last) # Boyyo

# Steps determine every nth increase to our index as we slice/index
funky_name = name[0:9:2]
# This will display every second character because our index now increases by TWO STEPS
print(funky_name)

# An additional shortcut is we can assume the zeroeth position to the end with a double colon [::step]
short_funk = name[::3]
print (short_funk) # B y

# Below we are starting from the 2nd index and moving til the end, increasing by TWO STEPS
twisted_name = name[2::2]
print(twisted_name) # gByo

# Same thing can be done by stopping early. Start zeroeth, go to 3rd index, 1 step at a time
early_name = name[:3:1] # 
print(early_name) # Big

# We can reverse a name by starting at a negative index, starting at [-1]
# Start at -1 and go from that zeroeth position til the end
reversed_name = name[::-1]
print(reversed_name) # oyyoB giB

# Start at the negative two [-2] index, continue to the end at [-2] steps
jumble_reverse = name[-2::-2]
print(jumble_reverse) # yo i

# SLICING
# Let's say we want to create a substring based on a website url
## assuming a standard http and .com format in this case

website1 = "http://google.com"
website2 = "http://wikipedia.com"

# Slice also uses up to 3 values, slice(start, stop, step)

# We can mix up positive and negative indexes
webslice = slice(7, -4) 

# In Python you must create a slice object to use on a string, instead of directly applying the .slice() function to a string variable
print(website1[webslice]) # google

print(website2[webslice]) # wikipedia

slice_with_steps = slice(7, -4, 2)
print(website1[slice_with_steps]) # gol
print(website2[slice_with_steps]) # wkpda


