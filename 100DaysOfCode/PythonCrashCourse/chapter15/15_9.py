"""
When you roll two dice, you usually add the two numbers together to get the result.
Create a visualization that shows what happens if you multiply these numbers instead.
"""

from die import Die
import pygal

# create two D6 dice
die_1 = Die()
die_2 = Die()

# make rolls
results = [die_1.roll() * die_2.roll() for roll_num in range(1000)]

# analyze the results
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# visualize the results
hist = pygal.Bar()
hist.title = "Results of multipling two dice"
hist.x_labels = [str(x) for x in range(1, max_result+1)]

hist.add('D6*D6', frequencies)
hist.render_to_file('15-9.svg')
