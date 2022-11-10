# if statement = a block of code that will execute if it's condition is true

# Remember our use of type casting 

name = input("What is your name? ")
age = int(input("How old are you? "))
wisdom = False

if age >= 100:
    wisdom = input("Wow you've lived a heck of a life! What's your secret? ")
elif age <= 99 and age >= 90:
    print("Almost a century old!")
elif age <= 89 and age >= 50:
    print("Wisdom of the ages has been bestowed upon you.")
elif age <= 49 and age >= 30:
    print("Midlife crisis much??")
elif age <= 29 and age >= 18:
    print("Welcome to adulthood, having fun yet?")
elif age <= 17 and age >= 6:
    print("Best years of your life, you will miss this")
elif age <=5 and age >=0:
    print("Your whole life is still ahead of you!")
else:
    print("You can't be negative years old liar...") 
    
if wisdom:
    print(name + ": " + wisdom)
else:
    print("Thanks for your time, " + name)