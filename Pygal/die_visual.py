
from die import Die
import pygal

die=Die()

results1=[]
results2=[]
results3=[]

for i in range(1000):
    results1.append(die.roll())
    results2.append(die.roll())
    results3.append(die.roll())

frequencies1=[]
frequencies2=[]
frequencies3=[]

for value in range(1,die.num_sides+1):
    frequencies1.append(results1.count(value))
    frequencies2.append(results2.count(value))
    frequencies3.append(results3.count(value))

hist=pygal.Bar()

hist.title="Results of rolling D6 1000 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist.y_title="Frequencies of 3 Times Result"

hist.add("1 of D6",frequencies1)
hist.add("2 of D6",frequencies2)
hist.add("3 of D6",frequencies3)

hist.render_to_file('die_visual.svg')