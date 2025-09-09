import polars as pl
import pandas as pd

fileInputPath = 'input/NPI/npidata_pfile_20050523-20250810.csv'
fileOutputPath = 'output'

## load the first 1000 rows
raw_data = pl.read_csv(fileInputPath, n_rows=1000)
cols = ['NPI',
         'Entity Type Code', 
         'Provider Organization Name (Legal Business Name)', 
         'Provider Last Name (Legal Name)', 
         'Provider First Name', 
         'Provider Middle Name', 
         'Provider Name Prefix Text',
         'Last Update Date', 
         'NPI Deactivation Date', 
         'NPI Reactivation Date']
print(raw_data.head())

clean_data = raw_data.select([cols]).to_pandas()
print (clean_data.head())