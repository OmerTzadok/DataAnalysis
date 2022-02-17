import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime
import numpy as np
from scipy import interpolate
from Services import StatCalc as stat

def var_plotting(df,levelcolumn,valuecolumn,nsigma):  
    #This function gets a df, a categorical level column name, a value column 
    #name and a n Sigma for limit calculation and returns a boxplot chart of 
    #said values per categorical values
    
    avg,stdv = stat.col_stats(df,valuecolumn,0,2)
    df.boxplot(column=valuecolumn,by=levelcolumn,grid=True).set_title("")
    plt.xticks(rotation=90)
    add_limits_lines (avg,stdv,nsigma)
    add_labels (valuecolumn,levelcolumn)
    plt.show()
    
def trend_plotting(df,timecolumn,valuecolumn,levelcolumn,nsigma):  
    #This function gets a df, a timestamp column name, a value column name, a 
    #categorical level column and a n Sigma for limit calculation and returns a 
    #time trend chart of said values per time column grouped by the categorical 
    #column
    
    avg,stdv = stat.col_stats(df,valuecolumn,0,2)
    fig, ax = plt.subplots()
    ax = scatter_sub_plotting_date(df,levelcolumn,timecolumn,valuecolumn,ax)        
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1.02))
    tick_spacing = 20
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    add_limits_lines (avg,stdv,nsigma)
    add_labels (valuecolumn,timecolumn)
    plt.show()
    
def scatter_sub_plotting_date (df, level,time,value, ax):
    colors = ["red","blue","green","yellow","magenta","purple","orange","pink","brown","grey","olive"]
    markers = ["o","v","^","<",">","s","*","x","D","d"]
    i=0
    j=0
    for key, grp in df.groupby([level]):
        ax = grp.plot.scatter(ax=ax, x=time, y=value, grid=True, c=colors[i], marker=markers[j],label=key)
        ax.set_xlim(df[time].min()-datetime.timedelta(days=1),df[time].max()+datetime.timedelta(days=1)) 
       
        spline_plot(grp,colors,time,value,  i)

        if j < (len(markers)-1):
            j = j+1
        else:
            j=0
        if i < (len(colors)-1):
            i = i+1
        else:
            i=0
    return(ax)

def spline_plot (df, colors,time,value, colorsIndex):
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
        
def add_limits_lines (avg,stdv,nsigma):  
    #This function adds control chart limit lines per given avg, stdev and # Sigmas
    
    left,right = plt.xlim()
    plt.hlines(avg,xmin=left,xmax=right,color = 'g',linestyles='--')
    plt.hlines(avg+stdv*nsigma,xmin=left,xmax=right,color = 'r',linestyles='-')
    plt.hlines(avg-stdv*nsigma,xmin=left,xmax=right,color = 'r',linestyles='-') 
    
def add_labels (ycolumn,xcolumn): 
    #This function adds an x axis, y axis and chart labels per given column names 
    
    plt.ylabel(ycolumn)
    plt.xlabel(xcolumn)
    plt.suptitle(ycolumn+" by "+xcolumn)
    
def sub_trend_plotting(df,timecolumn,valuecolumn,levelcolumn,nsigma,avg,stdv):  
    #This function gets a df, a timestamp column name, a value column name, a 
    #categorical level column and a n Sigma for limit calculation and returns a 
    #time trend chart of said values per time column grouped by the categorical 
    #column
    
    fig, ax = plt.subplots()
    ax = scatter_sub_plotting_date(df,levelcolumn,timecolumn,valuecolumn,ax)        
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1.02))
    tick_spacing = 20
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    for tick in ax.get_xticklabels():
        tick.set_rotation(45)
    add_limits_lines (avg,stdv,nsigma)
    add_labels (valuecolumn,timecolumn)
    plt.show()
