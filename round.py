# Function to round a number to n decimal places
def my_round(x, n):
    factor = 10 ** n
    return round(x * factor) / factor

# Input from user
number = float(input("Enter a number (x): "))
decimal_places = int(input("Enter the number of decimal places (n): "))

result = my_round(number, decimal_places)

print(f"{number} rounded to {decimal_places} decimal places is {result}.")
