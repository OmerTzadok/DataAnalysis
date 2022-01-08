import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import numpy as np
from scipy import interpolate
import StatCalc as stat

def VarPlotting(df,levelcolumn,valuecolumn,nsigma):  
    #This function gets a df, a categorical level column name, a value column 
    #name and a n Sigma for limit calculation and returns a boxplot chart of 
    #said values per categorical values
    
    avg,stdv = stat.colstats(df,valuecolumn,0,0)
    df.boxplot(column=valuecolumn,by=levelcolumn,grid=True).set_title("")
    plt.xticks(rotation=90)
    AddLimitsLines (avg,stdv,nsigma)
    AddLabels (valuecolumn,levelcolumn)
    plt.show()
    
def TrendPlotting(df,timecolumn,valuecolumn,levelcolumn,nsigma):  
    #This function gets a df, a timestamp column name, a value column name, a 
    #categorical level column and a n Sigma for limit calculation and returns a 
    #time trend chart of said values per time column grouped by the categorical 
    #column
    
    avg,stdv = stat.colstats(df,valuecolumn,0,0)
    fig, ax = plt.subplots()
    ax = ScatterSubPlottingDate(df,levelcolumn,timecolumn,valuecolumn,ax)        
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1.02))
    tick_spacing = 20
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    AddLimitsLines (avg,stdv,nsigma)
    AddLabels (valuecolumn,timecolumn)
    plt.show()
    
def ScatterSubPlottingDate (df, level,time,value, ax):
    colors = ["red","blue","green","yellow","magenta","purple","orange","pink","brown","grey","olive"]
    markers = ["o","v","^","<",">","s","*","x","D","d"]
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
        
def AddLimitsLines (avg,stdv,nsigma):  
    #This function adds control chart limit lines per given avg, stdev and # Sigmas
    
    left,right = plt.xlim()
    plt.hlines(avg,xmin=left,xmax=right,color = 'g',linestyles='--')
    plt.hlines(avg+stdv*nsigma,xmin=left,xmax=right,color = 'r',linestyles='-')
    plt.hlines(avg-stdv*nsigma,xmin=left,xmax=right,color = 'r',linestyles='-') 
    
def AddLabels (ycolumn,xcolumn): 
    #This function adds an x axis, y axis and chart labels per given column names 
    
    plt.ylabel(ycolumn)
    plt.xlabel(xcolumn)
    plt.suptitle(ycolumn+" by "+xcolumn)