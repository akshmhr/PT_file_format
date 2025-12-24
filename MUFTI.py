
import pandas as pd
import re

def format(df, season=None):

    df.columns = df.iloc[1]
    df = df.iloc[2:].reset_index(drop=True)


    df['Size'] = df['Size'].str.strip().replace("XXL","2XL")


    patterns = {
        'H/S': 'H/S',
        'F/S': 'F/S',
        'S/L': 'S/L'
    }

    for pat, val in patterns.items():
        df.loc[df['Pattern'].str.contains(pat, na=False), 'Pattern'] = val
    
    
    number = df['Bill No'][0]
    
    return df, number