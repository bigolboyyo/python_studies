# tuple = a collection which is ordered and unchangeable, used to group together related data (use parenthesis() instead of square brackets[])
# very similar to lists(arrays), but the data is IMMUTEABLE

student = ("BigBoyyo", 28, "male")

print(student.count(int("28"))) # 1
print(student.index("male")) # 2

# can still iterate through tuples

for x in student:
    print(x)
    
if "BigBoyyo" in student:
    print("Boyyo is present!")