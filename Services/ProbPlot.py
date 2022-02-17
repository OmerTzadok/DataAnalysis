from matplotlib import pyplot as plt
import probscale
from numpy import min as npmin
from numpy import max as npmax

def norm_prob_plot (df,valuecolumn,probaxis='y'):
    
    fig, ax = plt.subplots()
    common_opts = dict(
        probax=probaxis,
        datalabel=valuecolumn,
        bestfit=True,
        #estimate_ci=True,
        scatter_kws=dict(marker='.', markersize=5)
    )
    
    fig = probscale.probplot(df[valuecolumn], ax=ax, plottype='prob',
                             problabel='Standard Normal Probabilities',  **common_opts)
    
    if probaxis == 'y':
        ax.set_xlim(left=npmin(df[valuecolumn]), right=npmax(df[valuecolumn]))
        ax.set_ylim(bottom=0.01, top=99.99)
        plt.yticks([0.1,0.5,5,25,50,75,95,99.5,99.9])
    if probaxis == 'x':
        ax.set_ylim(bottom=npmin(df[valuecolumn]), top=npmax(df[valuecolumn]))
        ax.set_xlim(left=0.01, right=99.99)
        plt.xticks([0.1,0.5,5,25,50,75,95,99.5,99.9],rotation=45)
    
    plt.grid()
    plt.show();