# Function to generate a range of numbers
def my_range(start, stop, step):
    numbers = []
    current = start
    if step > 0:
        while current < stop:
            numbers.append(current)
            current += step
    elif step < 0:
        while current > stop:
            numbers.append(current)
            current += step
    return numbers

# Input from user
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
step = int(input("Enter the step value: "))

# Generate the range
result = my_range(start, stop, step)

print(f"Range from {start} to {stop} with step {step}: {result}")
