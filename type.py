# Function to get the type of a variable
def my_type(value):
    return str(type(value))

# Input from user
user_input = input("Enter a value: ")

# Try to interpret the input as different types
try:
    # Try to convert to integer
    value = int(user_input)
except ValueError:
    try:
        # Try to convert to float
        value = float(user_input)
    except ValueError:
        # If it fails, keep it as string
        value = user_input

# Get the type of the value
result = my_type(value)

print(f"The type of the value is: {result}")
