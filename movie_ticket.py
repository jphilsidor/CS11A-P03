# Keep asking until the user chooses to quit 
while True: 
    # Ask for the person's age 
    age = int(input("Enter your age (-1 to quit): ")) 
 
    # Stop when the user enters -1 
    if age == -1: 
        print("Thank you!") 
        break 
 
    # Reject other negative ages 
    if age < 0: 
        print("Please enter a valid age.") 
        continue 
 
    # Display the ticket price 
    if age < 3: 
        print("Your movie ticket is free.") 
    elif age <= 12: 
        print("Your movie ticket costs $10.") 
    else: 
        print("Your movie ticket costs $15.") 