import polars as pl
import pandas as pd
import numpy as np

fileInputPath = 'input/NPI/npidata_pfile_20050523-20250810.csv'
fileOutputPath = 'output'


#Load the first 100,000 rows due to memory constraints
raw_data = pl.read_csv(fileInputPath, n_rows=1000)

# Use Polars' when().then().otherwise() to create new columns.
# We create a 'name' column based on Entity Type Code (1=individual, 2=organization)
raw_data = raw_data.with_columns(
    # Create the 'name' column
    pl.when(pl.col('Entity Type Code') == 1)
    .then(pl.col('Provider First Name') + ' ' + pl.col('Provider Last Name'))
    .otherwise(pl.col('Provider Organization Name (Legal Business Name)'))
    .alias('name'),
    # Create a 'Status' column based on whether the NPI Deactivation Date is null
    pl.when(pl.col('NPI Deactivation Date').is_null())
    .then(pl.lit('Active'))  # Use pl.lit() for literal string values
    .otherwise(pl.lit('Inactive')) # Use pl.lit() for literal string values
    .alias('Status')
)

print(raw_data.head())


# --- Column Selection and Conversion to Pandas ---
# Define the specific columns to keep in the final DataFrame.
cols = ['NPI',
          'name',
          'Entity Type Code',
          'Status',
          'Last Update Date',
          'NPI Deactivation Date',
          'NPI Reactivation Date']

# Convert the selected Polars DataFrame to Pandas for compatibility with other libraries.
clean_data = raw_data.select(cols).to_pandas()

print("\nPandas DataFrame Head:")
print(clean_data.head())