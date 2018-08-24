import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print(r.status_code)

response_dict=r.json()
print("Total respositories:",response_dict['total_count'])

repo_dicts=response_dict['items']

names=[]
#stars=[]
plot_dicts=[]

for repo in repo_dicts:
    names.append(repo['name'])

    plot_value=repo['stargazers_count']
    plot_label=repo['description'] if repo['description'] else ''
    plot_xlink=repo['html_url']
    plot_dict={'value':plot_value,'label':plot_label,'xlink':plot_xlink}

#    stars.append(repo['stargazers_count'])
    plot_dicts.append(plot_dict)

#for plot in plot_dicts:
#    print(plot['value'],plot['label'])

my_style=LS('#336699',base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000


chart=pygal.Bar(my_config,style=my_style)
chart.title='The Most popular Projects of Github'
chart.x_labels=names

#chart.add('',stars)
chart.add('',plot_dicts)

chart.render_to_file('python_repos.svg')
