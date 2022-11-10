# while loop = a statement that will execute its block of code, AS LONG (while) as it's condition remains true

# Easy to create infinite loops
## while 1==1:
##    print("Help! I'm stuck in a loop!! Quick, press *ctrl+c* to escape!!!")


name = ""
goal = 10
start = 0

while len(name) == 0:
    name = input("Enter Your Name Here: ")
    
print("Hello " + name)

while start < goal:
    start += 1
    print("Always keep moving towards your goal: " + str(start))
