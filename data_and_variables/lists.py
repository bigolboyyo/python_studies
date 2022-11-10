# list = used to store multiple items in a single variable. like an array

food = ["pizza", "hotdog", "hamburger", "spaghetti", "ice cream"]
test = list(map(list, food))
print(test)

# you can directly access elements by index
print(food[0]) # pizza
print(food[2]) # hamburger

# you can update by index
print(food[4]) # ice cream
food[4] = "sushi"
print(food[4]) # sushi

# you can loop through a list
def food_printer(food):
    for i in food:
        print(i)
        
food_printer(food)

# useful functions for lists

# append = add a element to end of list
food.append("ice cream")
print(food) # ['pizza', 'hotdog', 'hamburger', 'spaghetti', 'sushi', 'ice cream']

# remove = remove a specific element from list
food.remove("hotdog")
print(food) # ['pizza', 'hamburger', 'spaghetti', 'sushi', 'ice cream']

# pop = remove the LAST element from the list
food.pop()
print(food) # ['pizza', 'hamburger', 'spaghetti', 'sushi']

# insert = add an element to a specific position
food.insert(1, "cake")
print(food) # ['pizza', 'cake', 'hamburger', 'spaghetti', 'sushi']

# sort = sort a list alphabetically 
food.sort()
print(food) # ['cake', 'hamburger', 'pizza', 'spaghetti', 'sushi']

# clear = clear the entire list
food.clear()
print(food) # []

#==========================================================================# 

# 2D LISTS (multidimensional lists) = a list of lists!

drinks = ["coffee", "soda", "tea", "beer"]
dinner = ["steak", "pizza", "fettucini alfredo"]
dessert = ["ice cream", "cake"]

food = [drinks, dinner, dessert]
print(food)

# nested direct access
print(food[0]) # ['coffee', 'soda', 'tea', 'beer']
print(food[0][3]) # beer

