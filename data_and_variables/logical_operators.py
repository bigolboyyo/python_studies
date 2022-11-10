# Logical operators (and, or, not) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside in celsius? "))

# (not) operator = if NOT true, ie False. <Variable> NOT <True> | <Variable> == <False>    
if not temp >= 0 and temp <= 30: 
# (and) operator = both conditions need to be true. <True> AND <True> then execute
    print("It's gross out, stay inside...")
    
# (or) operator = one or the other needs to be true. <True> OR <True> then execute
elif temp < 0 or temp > 30:
    print("Weather is perfect, time to go outside!")


