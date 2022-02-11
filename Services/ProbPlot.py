from matplotlib import pyplot
import probscale
from numpy import min as npmin
from numpy import max as npmax

def NormProbPlot (df,valuecolumn,probaxis):
    
    fig, ax = pyplot.subplots()
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
    if probaxis == 'x':
        ax.set_ylim(bottom=npmin(df[valuecolumn]), top=npmax(df[valuecolumn]))
        ax.set_xlim(left=0.01, right=99.99)
        
    fig.tight_layout()