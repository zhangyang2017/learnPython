"""
Create a visualization that shows what happens when you roll three D6 dice.
"""

from die import Die
import pygal

# create three D6s
die_1 = Die()
die_2 = Die()
die_3 = Die()

# make rolls
results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1000)]

# analyze results
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3, max_result+1)]

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 1000 times"
hist.x_labels = [str(x) for x in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6+D6', frequencies)
hist.render_to_file('3D6_visual.svg')
