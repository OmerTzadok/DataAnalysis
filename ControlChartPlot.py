import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import numpy as np
from scipy import interpolate

def VarPlotting(df,levelcolumn,valuecolumn,avg,stdv):
    df.boxplot(column=valuecolumn,by=levelcolumn,grid=True).set_title("")
    plt.xticks(rotation=90)
    left,right = plt.xlim()
    plt.hlines(avg,xmin=left,xmax=right,color = 'g',linestyles='--')
    plt.hlines(avg+stdv*3,xmin=left,xmax=right,color = 'r',linestyles='-')
    plt.hlines(avg-stdv*3,xmin=left,xmax=right,color = 'r',linestyles='-')
    plt.ylabel(valuecolumn)
    plt.xlabel(levelcolumn)
    plt.suptitle(valuecolumn+" by "+levelcolumn)
    plt.show()
    
def TrendPlotting(df,timecolumn,valuecolumn,levelcolumn,avg,stdv):
    fig, ax = plt.subplots()
    colors = ["red","blue","green","yellow","magenta","purple","orange","pink","brown","grey","olive"]
    markers = ["o","v","^","<",">","s","*","x","D","d"]
    ax = ScatterSubPlotting(df,levelcolumn,timecolumn,valuecolumn,ax,colors,markers)        
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1.02))
    tick_spacing = 20
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    left,right = plt.xlim()
    plt.hlines(avg,xmin=left,xmax=right,color = 'g',linestyles='--')
    plt.hlines(avg+stdv*3,xmin=left,xmax=right,color = 'r',linestyles='-')
    plt.hlines(avg-stdv*3,xmin=left,xmax=right,color = 'r',linestyles='-')  
    plt.ylabel(valuecolumn)
    plt.xlabel(levelcolumn)
    plt.suptitle(valuecolumn+" by "+levelcolumn)
    plt.show()
    
def ScatterSubPlotting (df, level,time,value, ax, colors, markers):
    i=0
    j=0
    for key, grp in df.groupby([level]):
        ax = grp.plot.scatter(ax=ax, x=time, y=value, grid=True, c=colors[i], marker=markers[j],label=key)
        ax.set_xlim(df[time].min()-datetime.timedelta(days=1),df[time].max()+datetime.timedelta(days=1)) 
       
        SplinePlot(grp,colors,time,value,  i)

        if j < (len(markers)-1):
            j = j+1
        else:
            j=0
        if i < (len(colors)-1):
            i = i+1
        else:
            i=0
    return(ax)

def SplinePlot (df, colors,time,value, colorsIndex):
    if df.shape[0] > 1:
        xx=df[time].values.astype(int,casting='unsafe')
        xx = np.abs(xx)
        xx = sorted (xx)
        if df.shape[0]-1 < 5:
            degree = df.shape[0]-1
        else:
            degree = 3
        yinterp = interpolate.UnivariateSpline(xx, df[value], s = 100000000, k=degree)(xx)
        plt.plot(df[time], yinterp,colors[colorsIndex] )