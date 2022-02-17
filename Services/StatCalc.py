from numpy import mean as npmean
from numpy import std as npstd
from numpy import min as npmin
from numpy import max as npmax

def col_stats(df,columnname,doprint=0,rounddec=10):
    avg = round(npmean(df[columnname]),rounddec)
    stdv = round(npstd(df[columnname]),rounddec)
    if doprint:
        print(f"{columnname} Average is {avg}")
        print(f"{columnname} STDEV is {stdv}")
    return(avg,stdv)

def col_stats_full(df,columnname,doprint=0,rounddec=10):
    avg = round(npmean(df[columnname]),rounddec)
    stdv = round(npstd(df[columnname]),rounddec)
    minimum = round(npmin(df[columnname]),rounddec)
    maximum = round(npmax(df[columnname]),rounddec)
    colrange = round(maximum-minimum,rounddec)
    n = len(df[columnname])
    if doprint:
        print(f"{columnname} Average is {avg}")
        print(f"{columnname} STDEV is {stdv}")
        print(f"{columnname} Min is {minimum}")
        print(f"{columnname} Max is {maximum}")
        print(f"{columnname} Range is {colrange}")
        print(f"{columnname} N is {n}")
    return(avg,stdv,minimum,maximum,colrange,n)

def group_mean(df,levelcolumn,valuecolumn):
    grouped_df = df.groupby([levelcolumn])
    mean_df = grouped_df.mean()
    mean_df = mean_df.reset_index()
    return(mean_df)
    
def group_stdev(df,levelcolumn,valuecolumn):
    grouped_df = df.groupby([levelcolumn])
    stdev_df = grouped_df.std()
    stdev_df = stdev_df.reset_index()
    return(stdev_df)

def group_max(df,levelcolumn,valuecolumn):
    grouped_df = df.groupby([levelcolumn])
    max_df = grouped_df.max()
    max_df = max_df.reset_index()
    return(max_df)

def group_min(df,levelcolumn,valuecolumn):
    grouped_df = df.groupby([levelcolumn])
    min_df = grouped_df.min()
    min_df = min_df.reset_index()
    return(min_df)

def list_stats_full (listinput,decimals=10):
    
    mean = round(npmean(listinput),decimals)
    stdev = round(npstd(listinput),decimals)
    minimum = round(npmin(listinput),decimals)
    maximum = round(npmax(listinput),decimals)
    n = len(listinput)
    
    return(mean,stdev,minimum,maximum,n)
