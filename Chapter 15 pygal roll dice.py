#Chapter 15 pygal roll dice
from die import Die
import pygal
from lxml import etree
die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

print(results)

frequencies =[]
max = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(1, max+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
#visualization to the random roll
hist = pygal.Bar(title="Result for rolling 3 D6 dice",
                      x_labels=['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'],
                      x_title="Result",
                      y_title="Frequency")

hist.add('D6 + D6 + D6', frequencies)

hist.render_in_browser()  