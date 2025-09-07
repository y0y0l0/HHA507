import pandas as pd
from utils.common_functions import setLastUpdateColumn, save_to_formats
fileInputPath ='input/LOINC/Loinc.csv'
fileOutputPath='output'

#load raw_data
raw_data = pd.read_csv(fileInputPath,low_memory=False)
cols = ['LOINC_NUM', 'COMPONENT', 'CLASSTYPE', 'STATUS']

#clean data
clean_data = raw_data [cols]
clean_data=setLastUpdateColumn(clean_data, pd)

## save cleaned data to output path
save_to_formats(clean_data, fileInputPath,fileOutputPath, "loinc2025_processed.csv")