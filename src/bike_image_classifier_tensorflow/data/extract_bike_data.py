# -*- coding: utf-8 -*-
import ast
import pandas as pd
import urllib

## TODO: Should we encourage if name == main??

def extract_bbb_data(year, start_page, end_page, url_string, existing_df = None):
    # create dataframe to accumulate
    if existing_df:
        df = existing_df.copy()
    else:
        df = pd.DataFrame()
    
    # loop through pages
    for page_num in range(start_page,end_page+1):
        
        # create specific URL
        url_formatted = url_string.format(year=year, page=page_num)
        
        # pull data from the URL
        print(url_formatted)
        url_dict_string = urllib.request.urlopen(url_formatted).read().decode("UTF-8")
        url_dict = ast.literal_eval(url_dict_string)
        url_df = pd.DataFrame.from_dict(url_dict['data'])
        df = df.append(url_df)
        print('Page '+str(page_num))
    
    
    return df.reset_index(drop=True)


def bike_type_converter(type):
    if type in ['Hybrid', 'Mountain', 'Road', 'Cyclocross', 'Kids']:
        new_type = type
    else:
        new_type = 'Other'
    return new_type