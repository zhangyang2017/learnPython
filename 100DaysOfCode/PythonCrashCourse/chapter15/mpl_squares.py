#!/usr/local/bin/python3

import matplotlib.pyplot as plt

## import the pyplot module using the alias plt so we don’t have to type pyplot repeatedly

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()
## opens matplotlib’s viewer and displays the plot
