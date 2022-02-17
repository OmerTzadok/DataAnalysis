import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects

def ordered_bar_plot(df,limit,yvalue,xvalue,dobuckets=0):
    df= df.sort_values(by=[yvalue])
    
    xvaluelist = df[xvalue].tolist()
    yvaluelist = df[yvalue].tolist()
    
    ax = df.plot.bar(x=xvalue, y= yvalue,  fc=(0.9, 0, 0.1, 0.4), width=0.7, linewidth=5,figsize=(15, 7))
    plt.title(label = str(yvalue)+" by "+str(xvalue), fontsize=20,color=('black'))
    plt.tick_params(axis='x', which='both', bottom=True,top=False,labelbottom=False)
    ax.legend().remove()
    
    i = 0
    for p in ax.patches:
        ax.annotate(str(xvaluelist[i]), (p.get_x() + .18, limit/20), rotation=90, color=(0.2, 0, 0), fontsize=13,
                    fontweight='bold', path_effects=[patheffects.withStroke(linewidth=0.5,foreground='black')])
        i += 1
    
    x_positions = np.arange(len(xvaluelist))
    x_startend = [x_positions[0],x_positions[-1]]
    y_startend = [yvaluelist[0],limit]
    fit = np.polyfit(x_startend, y_startend, 1)
    yfit = [n * fit[0] for n in list(range(len(xvaluelist)))] 
    
    plt.plot(yfit, 'red', ls='--', lw=3, alpha=0.4)
    plt.grid(color='gray', linestyle='--', linewidth=1, alpha=0.1)
    plt.axhline(y=limit, linewidth=4, linestyle='--',color='black',alpha=0.6)
    plt.axhline(y=round(limit-limit/10,0), linewidth=2, linestyle='--',color='black',alpha=0.3)
    plt.text(len(xvaluelist)/12, limit, str(limit), fontsize=15, va='center', ha='center', backgroundcolor='w',alpha=0.5)
    plt.text(len(xvaluelist)/12, int(round(limit-limit/10,0)), str(int(round(limit-limit/10,0))), fontsize=15, va='center', 
             ha='center', backgroundcolor='w',alpha=0.5)
    
    if dobuckets:
        bucket_lines(yvaluelist,limit)
        
    plt.ylim(0,limit+limit/10)
    plt.tight_layout()
    
def bucket_lines(yvaluelist,limit):
    buckets = [int(round(limit*0.2,0)),int(round(limit*0.4,0)),int(round(limit*0.6,0)),int(round(limit*0.8,0))]
    i=0
    for m in range((len(yvaluelist)-1)):
        if i<len(buckets):
            if (yvaluelist[m] <= buckets[i]) and (yvaluelist[m+1] > buckets[i]):
                plt.axvline(x=m+0.5, linewidth=2, linestyle='--',color='black',alpha=0.3)
                labeltext = str(buckets[i])
                plt.text(x=(m+0.5), y=int(round(limit-limit/6,0)), s=labeltext, fontsize=15, va='center', ha='center', 
                         backgroundcolor='none',alpha=0.5)
                i=i+1
