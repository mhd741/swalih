# Function to compare two values
def my_cmp(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0

# Input from user
num1 = float(input("Enter the first number (x): "))
num2 = float(input("Enter the second number (y): "))

result = my_cmp(num1, num2)

if result == -1:
    print(f"{num1} is less than {num2}.")
elif result == 1:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")
