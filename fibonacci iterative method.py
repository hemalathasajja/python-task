# Function to print Fibonacci series up to n terms
def fibonacci_iterative(n):
    a, b = 0, 1
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Get user input
terms = int(input("Enter the number of terms: "))

# Validate input and print the series
if terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_iterative(terms)
