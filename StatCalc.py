import numpy as np

def colstats(df,columnname):
    avg = np.mean(df[columnname])
    stdv = np.std(df[columnname])
    
    print(avg,stdv,columnname)
    return(avg,stdv)

def groupmean(df,levelcolumn,valuecolumn):
    grouped_df = df.groupby([levelcolumn])
    mean_df = grouped_df.mean()
    mean_df = mean_df.reset_index()
    return(mean_df)
