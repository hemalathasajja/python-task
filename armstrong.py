# Function to check if a number is an Armstrong number
def is_armstrong(number):
    # Convert the number to string to easily iterate through digits
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum equals the original number
    return armstrong_sum == number

# Get user input
num = int(input("Enter an integer: "))

# Check and print result
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
