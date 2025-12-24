
import pandas as pd
import re




def format(df, season=None):

    df.columns = df.iloc[1]
    df = df.iloc[2:].reset_index(drop=True)


    # season = str(input("Enter Season: "))


    df['Size'] = df['Size'].str.strip().replace("XXL","2XL")


    df['Season'] = season


    df['Item Name'] = df['Item Name'].replace({
        'T-SHIRTS' : 'T-SHIRT',
        'TSHIRTS' : 'T-SHIRT',
        'SWEATSHIRT' : 'SWEAT SHIRT',
    })


    df['rat_dis%'] = 5


    number = df['Bill No'][0]


    return df, number



