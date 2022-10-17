
import pandas as pd
from datetime import datetime

# This is adapted from Emily Fyeh's notebook under the preprocessing-IDoTdata branch

def cleaning(data):
    """
    Cleaning the IDOT (Illinois Department of Transportation) data.

    The function does the following: 
        * Convert data/time related variables to their specific types
        * Convert drivers' races and sexs to a string
        * Filter out unnecessary columns

    Return: 
        a cleaned IDOT dataset (as a pandas dataframe)  
    """
    def convert_DATESTOP(datestr):
        try:
            return datetime.strptime(datestr, '%m/%d/%Y').date()
        except:
            return datetime.strptime(datestr, '%m/%d/%y').date()

    def convert_TIMESTOP(timestr):
        try:
            if timestr[1] == ':':
                timestr = '0' + timestr
            if len(timestr) == 8:
                return datetime.strptime(timestr, '%H:%M:%S').time()
            return datetime.strptime(timestr, '%H:%M').time()
        except:
            if timestr[0:2] == '0:':
                timestr = '12' + timestr[1:]
            return datetime.strptime(timestr, '%I:%M:%S %p').time()

    data['DATESTOP'] = data['DATESTOP'].apply(lambda x: convert_DATESTOP(x))
    data['TIMESTOP'] = data['TIMESTOP'].apply(lambda x: convert_TIMESTOP(x))

    df_dr = data[['DATESTOP', 'TIMESTOP', 'DURATION', 
            'VEHMAKE', 'VEHYEAR', 'YRBIRTH', 'DRSEX', 'DRRACE']]
    df_dr.loc[:,'YEARSTOP'] = df_dr.loc[:,'DATESTOP'].apply(lambda x: x.year)
    df_dr.loc[:,'DRAGE'] = df_dr.apply(lambda x: x['YEARSTOP'] - x['YRBIRTH'], axis=1)
    df_dr.loc[:,'DRRACE'] = df_dr.loc[:,'DRRACE'].astype(str)
    df_dr.loc[:,'DRSEX'] = df_dr.loc[:,'DRSEX'].astype(str)

    return df_dr