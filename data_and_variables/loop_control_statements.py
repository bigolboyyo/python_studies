# Loop control statements = change a loops execution from its normal sequence. (break, continue, pass)

# break = used to terminate the loop entirely
while True:
    name = input("Enter your name: ")
    if len(name) > 0: 
        break 
    
print ("You have broken out!")


# continue = skips to the next iteration of the loop
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
print() # Empty print in "outer loop to print new line in terminal"


# pass = does nothing, acts as a placeholder
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
    