# Function to convert an integer to binary, octal, and hexadecimal
def convert_number(num):
    binary = bin(num)
    octal = oct(num)
    hexadecimal = hex(num)
    return binary, octal, hexadecimal

# Input from user
try:
    number = int(input("Enter an integer: "))
    
    # Convert the number
    binary, octal, hexadecimal = convert_number(number)

    print(f"Binary representation: {binary}")
    print(f"Octal representation: {octal}")
    print(f"Hexadecimal representation: {hexadecimal}")

except ValueError:
    print("Please enter a valid integer.")
