from die import Die
import pygal


die1=Die()
die2=Die(10)

results1=[]
results2=[]
results3=[]

for i in range(5000):
    result1=die1.roll()
    result2=die2.roll()
    result3=result1+result2
    results1.append(result1)
    results2.append(result2)
    results3.append(result3)

frequencies1=[]
frequencies2=[]
frequencies3=[None]

for value in range(1,die1.num_sides+1):
    frequencies1.append(results1.count(value))

for value in range(1,die2.num_sides+1):
    frequencies2.append(results2.count(value))

for value in range(2,die1.num_sides+die2.num_sides+1):
    frequencies3.append(results3.count(value))

hist=pygal.Bar()

hist.title="Results of rolling D6 and D10 dice 5000 times"
hist.x_labels=list(range(1,die1.num_sides+die2.num_sides+1))
hist.x_title="Result"
hist.y_title="Frequencies of Result"

hist.add("D6",frequencies1)
hist.add("D10",frequencies2)
hist.add("D6+D10",frequencies3)

hist.render_to_file('dice_visual.svg')
