from pandas import read_csv as pdread

def properties_parser (filepath):
    
    properties =  pdread(filepath,sep=",")
    
    a = int(properties.iloc[0][1])
    b = int(properties.iloc[1][1])
    c = int(properties.iloc[2][1])
    d = properties.iloc[3][1]
    e = properties.iloc[4][1]
    f = properties.iloc[5][1]
    g = properties.iloc[6][1]
    h = properties.iloc[7][1]
    i = properties.iloc[8][1]
    j = properties.iloc[9][1]
    
    return(a,b,c,d,e,f,g,h,i,j)
