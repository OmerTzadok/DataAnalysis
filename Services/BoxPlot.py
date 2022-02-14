import seaborn as sb
from matplotlib import pyplot as plt

def ViolinPlot(df,ycolumns):
    fig, ax = plt.subplots()
    
    plot = sb.violinplot(data=df[ycolumns], inner="quartile",bw=0.2);
    plot = sb.swarmplot(data=df[ycolumns], size=5, color="k", alpha=0.5);
    
    plt.show()