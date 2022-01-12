import numpy as np

def colstats(df,columnname,doprint,rounddec):
    avg = np.mean(df[columnname])
    stdv = np.std(df[columnname])
    if doprint:
        print(columnname+" Average is "+str(round(avg,rounddec))+" And STDEV is "+str(round(stdv,rounddec)))
    return(avg,stdv)

def groupmean(df,levelcolumn,valuecolumn):
    grouped_df = df.groupby([levelcolumn])
    mean_df = grouped_df.mean()
    mean_df = mean_df.reset_index()
    return(mean_df)
    
def groupstdev(df,levelcolumn,valuecolumn):
    grouped_df = df.groupby([levelcolumn])
    stdev_df = grouped_df.std()
    stdev_df = stdev_df.reset_index()
    return(stdev_df)
