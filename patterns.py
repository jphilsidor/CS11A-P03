# Set the number of rows 
rows = 5 
 
# Print each row of the pattern 
for row in range(1, rows + 1): 
    # Print spaces before the stars 
    for space in range(rows - row): 
        print(" ", end=" ") 
 
    # Print the stars for this row 
    for star in range(row): 
        print("*", end=" ") 
 
    # Move to the next line 
    print() 