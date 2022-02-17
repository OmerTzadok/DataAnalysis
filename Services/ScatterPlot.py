import matplotlib.pyplot as plt
import seaborn as sb


def scatter(df,ycolumn,xcolumn):

    fig, ax = plt.subplots()
    ax = df.plot.scatter(ax=ax, x=xcolumn, y=ycolumn, grid=True, c=df[xcolumn], marker='^', s=60, edgecolors="k", alpha=0.5)

    plt.show()

def sb_scatter(df,ycolumn,xcolumn):
    
    fig, ax = plt.subplots()
    sb.scatterplot(x=xcolumn, y=ycolumn, hue=xcolumn, s=30, edgecolor="none", data=df);
    
    ax.get_legend().remove()
    
    plt.show()