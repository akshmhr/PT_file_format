import pandas as pd
import re
def format(df, season=None):
    df['BRAND'] = "U.S.POLO ASSN."

    season = df.loc[1, 'SEASON']

    season_formatted = season[0:2] + "-" + season[3:]

    df['SEASON'] = "AW-25"

    df['SIZE'] = df['SIZE'].replace('XXL', '2XL')

    df['Colour Code'] = df['Colour Code'].replace({
        'FS' : 'F/S' ,
        'HS' : 'H/S'
    })

    df['UDF04'] = df['UDF04'].replace({
        'USP-MWT-SWEAT SHIRT' : 'SWEAT SHIRT',
        'USP_MWT_SWEAT SHIRT' : 'SWEAT SHIRT',
        'USP_MWT_JACKET' : 'JACKET',
        'USP-MWT-JACKET' : 'JACKET',
        'USP_MWT_TROUSER' : 'TROUSER',
        'USP-MWT-JEANS' : 'JEANS',
        'USP_MWT_SHIRT' : 'SHIRT',
        'USP_MWT_POLO T-SHIRT' : 'T-SHIRT',
        'USP_MWT_SWEATER' : 'SWEATER',
        'USP-MWT-TRACKPANT' : 'TRACKPANT'
    })

    df['GROUP'] = "MENS"
    text = df['INVOICE_NO'][3]
    match = re.search(r'(\d+)$', text)
    number = match.group(1)
    return df, number






