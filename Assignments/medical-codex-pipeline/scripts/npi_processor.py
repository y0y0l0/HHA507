import polars as pl
import pandas as pd
import numpy as np

fileInputPath = 'input/NPI/npidata_pfile_20050523-20250810.csv'
fileOutputPath = 'output'


#Load the first 100,000 rows due to memory constraints
raw_data = pl.read_csv(fileInputPath, n_rows=1000)
#create name column based on Entity Type Code (1=individual, 2=organization)
raw_data['name'] = np.where(raw_data['Entity Type Code']==1, raw_data['Provider First Name'] + ' ' + raw_data['Provider Last Name'],  raw_data['Provider Organization Name (Legal Business Name)'])
print(raw_data.head())

cols = ['NPI',
         'name',
         'Entity Type Code',
         'Status',
         'Last Update Date',
         'NPI Deactivation Date',
         'NPI Reactivation Date']

#Convert to pandas for compatibility with existing functions
clean_data = raw_data [cols].to_pandas()
print (clean_data.head())
