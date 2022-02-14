import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

def CorrPlotting(df,ycolumn,xcolumn,levelcolumn):

    fig, ax = plt.subplots()
    ax = SubPlotting(df,levelcolumn,xcolumn,ycolumn,ax) 
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1.02))
        
    x = df[xcolumn]
    y = df[ycolumn]
    
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),'r-')
    
    text = f"$y={z[0]:0.3f}\;x{z[1]:+0.3f}$\n$R^2 = {r2_score(y, p(x)):0.3f}$"
    plt.gca().text(0.05, 0.95, text,transform=plt.gca().transAxes,fontsize=8, verticalalignment='top')

    plt.show()
    
def SubPlotting (df, level,time,value, ax):
    colors = ["red","blue","green","yellow","magenta","purple","orange","pink","brown","grey","olive"]
    markers = ["o","v","^","<",">","s","*","x","D","d"]
    i=0
    j=0
    for key, grp in df.groupby([level]):
        ax = grp.plot.scatter(ax=ax, x=time, y=value, grid=True, c=colors[i], marker=markers[j],label=key)
       
        if j < (len(markers)-1):
            j = j+1
        else:
            j=0
        if i < (len(colors)-1):
            i = i+1
        else:
            i=0
    return(ax)
