import pandas as pd
from utils.common_functions import normalizeColumnNames, save_to_formats,adjust_path_based_on_OS
#Path to the ICD_10 WHO text file
fileInputPath = adjust_path_based_on_OS('input/ICD_10_CM_WHO/icd102019syst_codes.txt')
fileOutputPath = 'output/'

## Load raw_data
columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

raw_data = pd.read_csv(fileInputPath, sep=';', header=None, names=columns)
## Clean data
cols = ['icd10_code','title_en','parent_title']
clean_data = raw_data[cols]
clean_data=normalizeColumnNames(clean_data, pd)

## save cleaned data to output path
save_to_formats(clean_data, fileInputPath,fileOutputPath, "icd10who_processed.csv")

