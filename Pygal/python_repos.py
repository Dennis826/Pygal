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
stars=[]

for repo in repo_dicts:
    names.append(repo['name'])
    stars.append(repo['stargazers_count'])

my_style=LS('#336699',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title='The Most popular Projects of Github'
chart.x_labels=names
chart.add('',stars)

chart.render_to_file('python_repos.svg')
