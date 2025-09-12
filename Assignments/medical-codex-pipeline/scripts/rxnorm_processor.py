import polars as pl
import pandas as pd
from utils.common_functions import normalizeColumnNames, save_to_formats,adjust_path_based_on_OS
#Path to the RxNorm RRF file
fileInputPath = adjust_path_based_on_OS('input/RxNorm/RXNATOMARCHIVE.RRF')
fileOutputPath ='output'

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

raw_data= pl.read_csv(
    fileInputPath,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)
cols = ['code', 'str', 'rxaui','sab','last_released']
#clean data
clean_data=raw_data [cols].to_pandas()
clean_data=normalizeColumnNames(clean_data,pd)
## save cleaned data to output path
save_to_formats(clean_data, fileInputPath,fileOutputPath, "rxnorm2025_processed.csv")