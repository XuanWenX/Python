from plotly.graph_objs import Bar, Layout
from  plotly import offline

from die import Die

die_1 = Die()
die_2 = Die(10)
#骰子结果储存在列表中
results = []
for number in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result) #统计所有1000个结果

frequencies = []
max_result = die_1.nums + die_2.nums
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency) #统计1k个结果中1-6出现的次数

x_value = list(range(2, max_result+1))
data = [Bar(x=x_value, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'The frequency of each results'}
my_layout = Layout(title='The results of threwing two die for 5000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename="d6_d10.html")





