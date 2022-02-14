import seaborn as sb
import pandas as pd
from matplotlib import pyplot as plt

def CorrMatrix(df):
    sb.heatmap(df.corr(), annot=True, fmt="0.2f", square=True);
    
    plt.show()
    
def ScatterMatrix(df):
    pd.plotting.scatter_matrix(df);
    
    plt.show()