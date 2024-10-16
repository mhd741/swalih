# Function to calculate absolute value
def my_abs(x):
    if x < 0:
        return -x
    else:
        return x

# Input from user
number = float(input("Enter a number: "))
result = my_abs(number)

print(f"The absolute value of {number} is {result}.")
