# Ask the user to enter an age 
age = int(input("Enter your age: ")) 
 
# Determine the stage of life 
if age < 0: 
    print("Please enter a valid age.") 
elif age < 2: 
    print("You are a baby.") 
elif age < 4: 
    print("You are a toddler.") 
elif age < 13: 
    print("You are a kid.") 
elif age < 20: 
    print("You are a teenager.") 
elif age < 65: 
    print("You are an adult.") 
else: 
    print("You are an elder.") 