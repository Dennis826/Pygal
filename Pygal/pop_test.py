import json

filename='population_data.json'
with open(filename) as file1:
    pop_data=json.load(file1)

for pop in pop_data:
    print(pop['Country Name'],pop['Country Code'],pop['Year'],pop['Value'])


