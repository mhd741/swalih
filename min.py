# Function to calculate the minimum of three numbers
def my_min(x, y, z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z

# Input from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

result = my_min(num1, num2, num3)

print(f"The minimum of {num1}, {num2}, and {num3} is {result}.")
