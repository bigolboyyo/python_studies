# We can prompt a user to input data that we can assign to variables

# input()
# Unless we specify otherwise, input is always captured as the STRING data type
# Pay attention to our use of type casting!

name = input("What is your name?: ")
age = int(input("How old are you?: ")) 
height = float(input("How tall are you? (in cm): "))

# These 3 input questions will be prompted and await an answer before continuing on and running our print statements

print("\n") # Prints a new line in the terminal

# Once again, pay attention to our type casting
# We are RE-converting our datatypes back into str

print("Hello " + name + "!")
print("You are " + str(age) + " years old!!")
print("You are " + str(height) + "cm tall!!!")


