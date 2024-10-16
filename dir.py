# Function to get the attributes and methods of an object
def my_dir(obj):
    return dir(obj)

# Input from user
user_input = input("Enter a value (it can be a number, list, etc.): ")

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

# Get the directory of the value
result = my_dir(value)

print(f"The attributes and methods of the value are: {result}")
