import pandas as pd
#Path to the HCPCS text file
fileInputPath = "input/HCPCS/HCPC2025_OCT_ANWEB_v2.txt"
fileOutputPath = "output/HCPC2025_OCT_ANWEB.csv"

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
##r ename columns
clean_data=clean_data.rename (columns={
    'Code':'code',
    'Description1':'description',
    })
## hardcode current date value on last_updated column
clean_data[['last_updated']] = pd.Timestamp.today().normalize()

## save clean data to output
output_path = "output/HCPC2025_OCT_ANWEB.csv"
clean_data.to_csv(fileOutputPath)