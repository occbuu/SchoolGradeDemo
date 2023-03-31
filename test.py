import pandas as pd
import matplotlib.pyplot as plt

import math
from matplotlib.patches import Rectangle
import matplotlib.colors as mcolors

df = pd.read_json("students.json")
def get_grade(r):
    if str(r['class'])[:2] == "10":
        return "10"
    if str(r['class'])[:2] == "11":
        return "11"
    if str(r['class'])[:2] == "12":
        return "12"

df["grade"] =  df.apply(lambda x: get_grade(x), axis=1)
my_colors = ['lightcoral', 'lightsteelblue', 'yellowgreen']
my_explode = (0.1, 0.1, 0.1)
i = df['grade'].value_counts().index
lbl = ['Grade ' + x for  x in i]
v = df['grade'].value_counts().values
plt.figure(figsize=(6,6))
plt.pie(v,labels =lbl,autopct='%1.2f%%',
        startangle=15, shadow=True, colors=my_colors, explode=my_explode)
plt.title('Ratio of Students by Grade')
plt.savefig('pie.png', bbox_inches='tight')
plt.show()

#
plt.figure(figsize=(6,6))
plt.title('Histogram of Students by GPA')
plt.xlabel("GPA by 10 points")
plt.ylabel("No. of students")
plt.hist(df['gpa'], edgecolor='black',color='darkseagreen')
plt.savefig('hist.png', bbox_inches='tight')
plt.show()

## Boxplot
males = df.query('gender == True')['gpa']
females = df.query('gender == False')['gpa']
cols = [males, females]
fig, ax = plt.subplots(figsize=(6,6))
ax.boxplot(cols)
plt.xticks([1,2],["Male student GPA","Female student GPA"])
plt.ylabel("GPA Scores")
plt.title('Boxplot Students by GPA')
plt.savefig('box.png', bbox_inches='tight')
plt.show()

def plot_colortable(colors, *, ncols=4, sort_colors=True):

    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(
            colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c))))
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(margin/width, margin/height,
                        (width-margin)/width, (height-margin)/height)
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows-0.5), -cell_height/2.)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(text_pos_x, y, name, fontsize=14,
                horizontalalignment='left',
                verticalalignment='center')

        ax.add_patch(
            Rectangle(xy=(swatch_start_x, y-9), width=swatch_width,
                      height=18, facecolor=colors[name], edgecolor='0.7')
        )

    return fig
plot_colortable(mcolors.CSS4_COLORS)
#plt.show()