import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
from OAuth2 import reddit


titles,scores = [],[]

for post in reddit.subreddit('all').hot(limit=10):
    titles.append(post.title)
    scores.append(post.score)
#Make Visualization

my_style = LS('#333366',base_style=LCS)
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)
chart.title = 'Highest scored points of /r/all'
chart.x_labels = titles

chart.add('',scores)
chart.render_to_file('Reddit_Posts.svg')

