"""
using matplotlib to make a die-rolling visualization
"""

from die import Die
from matplotlib import pyplot as plt

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

x = [value for value in range(2, max_result+1)]

plt.bar(x, frequencies)
plt.xticks(x, [str(x) for x in range(2, max_result+1)])

plt.axis([0, 20, 0, 160])

plt.show()
