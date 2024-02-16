from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

# Create a D6 and a D10
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []

for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides + 1):
    freqency = results.count(value)
    frequencies.append(freqency)

# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling one D6 and D10 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'd6.html') 
    
#print(frequencies)