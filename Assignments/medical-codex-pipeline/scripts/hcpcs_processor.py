import pandas as pd
from utils.common_functions import normalizeColumnNames, save_to_formats
#Path to the HCPCS text file
fileInputPath = "input/HCPCS/HCPC2025_OCT_ANWEB_v2.txt"
fileOutputPath = "output"

## load raw_data
# Adjusted colspecs based on actual column widths
# Here is a simple guess based on the sample
colspecs = [(0, 11), (11, 90), (90, 180), (180, 200), (200, 220), (220, 240), (240, 260), (260, 280)]
column_names = [
    "Code", "Description1", "Description2", "Type", "Unknown1", "Unknown2", "Unknown3", "Unknown4"
]
# Read the file into a DataFrame
# The file appears to be fixed-width formatted, so we'll use read_fwf
raw_data = pd.read_fwf(fileInputPath, colspecs=colspecs, names=column_names)
## clean_data
cols = ['Code', 'Description1']
clean_data = raw_data[cols]
## rename columns and add last_updated column with current date
clean_data =normalizeColumnNames(clean_data, pd)

## save clean data to output
output_path = "output/HCPC2025_OCT_ANWEB.csv"
save_to_formats(clean_data, fileInputPath,fileOutputPath, "HCPC2025_processed.csv")