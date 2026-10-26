# Define a function to generate Fibonacci numbers 
def fibonacci(position): 
    # Handle position zero 
    if position == 0: 
        return [0] 
 
    # Start with the first two Fibonacci numbers 
    numbers = [0, 1] 
 
    # Generate values up to the requested position 
    for i in range(2, position + 1): 
        next_number = numbers[i - 1] + numbers[i - 2] 
        numbers.append(next_number) 
 
    # Return the sequence 
    return numbers 
 
 
# Ask the user for a position 
position = int(input("What position of Fibonacci number you want to see? ")) 
 
# Validate input and display the sequence 
if position < 0: 
    print("Please enter a non-negative number.") 
else: 
    result = fibonacci(position) 
    print(", ".join(str(number) for number in result)) 