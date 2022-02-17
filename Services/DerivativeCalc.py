# -*- coding: utf-8 -*-

def derivative (df,yAxis,xAxis,derivativeName,multiplier):
    diff_df = df.diff()
    diff_df = diff_df.iloc[1: , :].reset_index()

    df[yAxis+'_diff'] = diff_df[yAxis]
    df[xAxis+'_diff'] = diff_df[xAxis]
    
    df.loc[df['Edisk/V_diff'] > 0, 'E_direction'] = 1
    df.loc[df['Edisk/V_diff'] < 0, 'E_direction'] = -1

    df[derivativeName+'_abs'] = df.apply( lambda row: abs((row[yAxis+'_diff'] / row[xAxis+'_diff'])*row[multiplier]) , axis=1)
    df[derivativeName] = df.apply( lambda row: (row[yAxis+'_diff'] / row[xAxis+'_diff'])*row[multiplier] , axis=1)
    
    return(df)
