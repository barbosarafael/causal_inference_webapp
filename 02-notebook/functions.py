from polars import *
from urllib.request import urlretrieve
import gzip
import os

def get_uplift_data():
    
    url = 'http://go.criteo.net/criteo-research-uplift-v2.1.csv.gz'
    filename = 'criteo-research-uplift-v2.1.csv.gz'
    
    
    try:
        
        raw_data_directory = '../01-data/01-raw/'
        
        os.chdir(raw_data_directory)
        
    except:
        
        pass
    
    print('Downloading data')
    
    if not os.path.exists(filename):
        
        urlretrieve(url, filename)
        
    print('Reading data')
    
    df_read = read_csv(filename)
    
    print('Finished')
    
    return df_read