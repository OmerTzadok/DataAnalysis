import StatCalc as stat

def CleanOutliers (df,valuecolumn,sensitivity):
    avg,stdv = stat.colstats(df,valuecolumn)
    df = df.loc[(df[valuecolumn]<(avg+sensitivity*stdv))&(df[valuecolumn]>(avg-sensitivity*stdv))]
    return(df)

def DropOutliers (df,outlierlist,indexcolumn):
    df = df.set_index(indexcolumn)
    for outlier in outlierlist:
        df = df.drop(outlier)
    df = df.reset_index()
    return (df)