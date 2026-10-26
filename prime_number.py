# Ask the user to enter a number 
num = int(input("Enter a number: ")) 
 
# Assume the number is prime initially 
is_prime = True 
 
# Numbers less than 2 are not prime 
if num < 2: 
    is_prime = False 
else: 
    # Check possible divisors from 2 up to num - 1 
    for i in range(2, num): 
        if num % i == 0: 
            is_prime = False 
            break 
 
# Display the result 
if is_prime: 
    print(f"{num} is a prime number") 
else: 
    print(f"{num} is not a prime number") 