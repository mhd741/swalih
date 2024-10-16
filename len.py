# Function to get the length of an object
def my_len(obj):
    return len(obj)

# Input from user
user_input = input("Enter a string or a list (comma-separated): ")

# Check if the input is meant to be a list or a string
if ',' in user_input:
    # Convert to a list
    value = [item.strip() for item in user_input.split(',')]
else:
    # Keep as string
    value = user_input

# Get the length of the value
result = my_len(value)

print(f"The length of the value is: {result}")
