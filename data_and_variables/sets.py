# set = a collection which is UNORDERED, UNINDEXED and has NO duplicate values. use Curly braces{}
# a set is faster than a list when checking if something exists within it

silverware = {"fork", "spoon", "knife"}

# we can iterate through, but the return values will NOT be ORDERED or INDEXED

for x in silverware:
    print(x)
    
# sets can NOT contain duplicate values
games = {"Tarkov", "Tarkov", "Overwatch", "Overwatch", "Catan", "Catan"}

def print_set(set):
    for x in set:
        print(x)
        
print_set(games) 
# Catan
# Tarkov
# Overwatch

# Set Methods

# add() = adds an element to the set
silverware.add("napkin")
print(silverware) # {'knife', 'napkin', 'fork', 'spoon'}

# remove() = remove a specific element from a set
silverware.remove("knife") # {'napkin', 'fork', 'spoon'}
print(silverware)

# clear() = remove ALL elements from a set
silverware.clear()
print(silverware) # set()

# update() = adds a set to another set
silverware.update(games)
print(silverware) # {'Tarkov', 'Catan', 'Overwatch'}

even_numbers = {2,4,6,8,10}
odd_numbers = {1,3,5,7,9,10}

# union() = join two sets
# notice it removes the duplicate 10
one_to_ten = even_numbers.union(odd_numbers)
print(one_to_ten) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# difference = compares two sets and finds what one set has the other does not
# so in this instance, even_numbers and odd_numbers both share 10. so return everything that is not 10
print(even_numbers.difference(odd_numbers)) # {8, 2, 4, 6}

# intersection = compares two sets and finds which elements both sets contain
# they both contain the number 10, so it returns 10
print(even_numbers.intersection(odd_numbers)) # {10}