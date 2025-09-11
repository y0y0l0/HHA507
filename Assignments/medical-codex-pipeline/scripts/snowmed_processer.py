import polars as pl
import pandas as pd
import os as os
from pathlib import Path
from utils.common_functions import normalizeColumnNames, save_to_formats,adjust_path_based_on_OS
#Path to the SnowMed text file
#fileInputPath= Path(adjust_path_based_on_OS('input/SnowMed/sct2_Description_Full-en_US1000124_20250301.txt'))
fileInputPath= adjust_path_based_on_OS('input/SnowMed/sct2_Description_Full-en_US1000124_20250301.txt')
print (f"File input path: {fileInputPath}")
fileOutputPath ='output'

raw_data = pl.read_csv(
    fileInputPath,
    separator='\t',
    has_header=True,
    quote_char=None,
    encoding='utf8-lossy',
    truncate_ragged_lines=True,
    dtypes={
        'id': pl.Utf8,
        'effectiveTime': pl.Utf8,
        'active': pl.Int32,
        'moduleId': pl.Utf8,
        'conceptId': pl.Utf8,
        'languageCode': pl.Utf8,
        'typeId': pl.Utf8,
        'term': pl.Utf8,
        'caseSignificanceId': pl.Utf8
    }
)
cols = ['conceptId', 'term','moduleId','active', 'effectiveTime' ]
#clean data
clean_data = raw_data [cols].to_pandas()
clean_data=normalizeColumnNames(clean_data,pd)
## save cleaned data to output path
save_to_formats(clean_data, fileInputPath,fileOutputPath, "snowmed_2025_processed.csv")