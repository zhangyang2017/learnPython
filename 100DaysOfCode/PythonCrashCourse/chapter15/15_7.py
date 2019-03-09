"""
Create a simulation showing what happens if you roll two eightsided dice 1000 times.
"""
from die import Die
import pygal

# create two D8s
die_1 = Die(8)
die_2 = Die(8)

# make rolls
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]

# analyze results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1000 times."
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8+D8', frequencies)
hist.render_to_file('D8dice_visual.svg')
