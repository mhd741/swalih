# Function to calculate the sum of a list of numbers
def my_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Input from user
numbers_input = input("Enter numbers separated by spaces: ")
numbers_list = [float(num) for num in numbers_input.split()]

result = my_sum(numbers_list)

print(f"The sum of the numbers is {result}.")
