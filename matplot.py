import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)                 # y is the sine of x

# Create the plot
plt.figure(figsize=(10, 5))   # Set the figure size
plt.plot(x, y, label='Sine Wave', color='blue')  # Plot y vs. x

# Adding titles and labels
plt.title('Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Adding a grid
plt.grid(True)

# Show legend
plt.legend()

# Show the plot
plt.show()
