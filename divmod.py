# Function to calculate quotient and remainder
def my_divmod(x, y):
    quotient = x // y
    remainder = x % y
    return quotient, remainder

# Input from user
num1 = float(input("Enter the dividend (x): "))
num2 = float(input("Enter the divisor (y): "))

# Check if divisor is zero
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = my_divmod(num1, num2)
    print(f"The quotient of {num1} divided by {num2} is {result[0]} and the remainder is {result[1]}.")
