# Function to generate a range of numbers up to a specified limit
def my_range(n):
    return [i for i in range(n)]

# Input from user
n = int(input("Enter the range limit (n): "))

# Generate the range
result = my_range(n)

print(f"Range from 0 to {n - 1}: {result}")
