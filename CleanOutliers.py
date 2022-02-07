import StatCalc as stat

def CleanOutliers (df,valuecolumn,sensitivity):
    #This function takes a df, a specific value column name and sesnsitivy in sigmas, 
    #and returns a df without all values outside of said sinsitivity limits

    avg,stdv = stat.colstats(df,valuecolumn,0,2)
    df = df.loc[(df[valuecolumn]<(avg+sensitivity*stdv))&(df[valuecolumn]>(avg-sensitivity*stdv))]
    
    return(df)

def DropOutliers (df,outlierlist,indexcolumn):
    #This function takes a df, and index column and a list of outlier values,
    #and return a df without all rows matching the outlier values
    
    df = df.set_index(indexcolumn)
    for outlier in outlierlist:
        df = df.drop(outlier)
    df = df.reset_index()
    
    return (df)