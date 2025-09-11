import polars as pl
import pandas as pd
import numpy as np
import gc as gc
import os as os
from utils.common_functions import normalizeColumnNames, save_to_formats, adjust_path_based_on_OS
#Path to the NPI csv file
fileInputPath = adjust_path_based_on_OS('input/NPI/npidata_pfile_20050523-20250810.csv')
fileOutputPath = 'output'

#Load the first 100,000 rows due to memory constraints
raw_data = pl.read_csv(fileInputPath, n_rows=100_000)

# Use Polars' when().then().otherwise() to create new columns.
# We create a 'name' column based on Entity Type Code (1=individual, 2=organization)
gc.collect()  # Force garbage collection to free up memory
raw_data = raw_data.with_columns(
    
    # Create the 'Name' column based on Entity Type Code
    # if Entity Type Code is '1', concatenate first and last names; if '2', use organization name
    pl.when(pl.col('Entity Type Code') == '1')
    .then(pl.col('Provider First Name') + ' ' + pl.col('Provider Last Name (Legal Name)'))
    .otherwise(pl.col('Provider Organization Name (Legal Business Name)'))
    .alias('Name'),
    # Create a 'Status' column based on whether the NPI Deactivation Date is null
    pl.when(pl.col('NPI Deactivation Date')== '')
    .then(pl.lit('Active'))  # Use pl.lit() for literal string values
    .otherwise(pl.lit('Inactive')) # Use pl.lit() for literal string values
    .alias('Status')
)

print(raw_data.head())

# --- Column Selection and Conversion to Pandas ---
# Define the specific columns to keep in the final DataFrame.
cols = ['NPI',
          'Name',
          'Entity Type Code',
          'Status',
          'Last Update Date',
          'NPI Deactivation Date']
# Convert the selected Polars DataFrame to Pandas for compatibility with other libraries.
clean_data = raw_data.select(cols).to_pandas()
clean_data=normalizeColumnNames(clean_data, pd)

# Save the cleaned data to the specified output formats.
save_to_formats(clean_data, fileInputPath, fileOutputPath, 'npi_data_processed.csv')
