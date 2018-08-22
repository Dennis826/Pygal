import json

from country_code import get_country_code
from pygal_maps_world.maps import World
from pygal.style import LightColorizedStyle, RotateStyle

filename='population_data.json'
with open(filename) as file1:
    pop_data=json.load(file1)

cc_population1={}
cc_population2={}
cc_population3={}

for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country=pop_dict['Country Name']
        population=int(float(pop_dict['Value']))
        code=get_country_code(country)
        
        if code:
            if population<10000000:
                cc_population1[code]=population
            elif population<100000000:
                cc_population2[code]=population
            else:
                cc_population3[code]=population


wm_style = RotateStyle('#116699', base_style=LightColorizedStyle)
wm=World(style=wm_style)

wm.title="World Population in 2010"
wm.add("0~10m",cc_population1)
wm.add("10m~100m",cc_population2)
wm.add("100m~1bn",cc_population3)

wm.render_to_file("world_population_2010.svg")
