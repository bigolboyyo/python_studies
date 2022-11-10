# nested loops = The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

# our "outer loop" will loop (for) each index(i) in rows
for i in range(rows):
    # our "inner loop" will loop (for) each index(j) in columns
    for j in range(columns):
        # (end) will prevent our cursor from moving down to the next line
        print(symbol, end="")
        # print a new line once we exit the "inner loop"
    print()