import pandas as pd
import re
from utils.common_functions import normalizeColumnNames, save_to_formats,adjust_path_based_on_OS

#Path to the ICD_10 CM US text file
fileInputPath = adjust_path_based_on_OS('input/ICD_10_CM_US/icd10cm_order_2026.txt')
fileOutputPath ='output'

## Load raw_data
# This initializes a blank list to hold the parsed codes (e.g., individual rows from the text file)
codes = []

try:
    # Use a 'with' statement to safely open the file.
    # Specify 'utf-8' encoding. If you get errors, 'latin-1' is another common one.
    with open(fileInputPath, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip any blank lines immediately.
            if not line.strip():
                continue

            # Your slicing logic is correct for this file's fixed-width format.
            order_num = line[0:5].strip()
            code = line[6:13].strip()
            level = line[14:15].strip()
            remaining_text = line[16:].rstrip() # Use rstrip to remove trailing whitespace

            # Splitting by a large gap of spaces is a good way to separate the two descriptions.
            parts = re.split(r'\s{4,}', remaining_text, 1)

            description = parts[0].strip() if len(parts) > 0 else ""
            description_detailed = parts[1].strip() if len(parts) > 1 else ""

            # Append the parsed data as a dictionary to our list.
            codes.append({
                'order_num': order_num,
                'code': code,
                'level': level,
                'description': description,
                'description_detailed': description_detailed
            })

except FileNotFoundError:
    print(f"Error: The file was not found at the path: {fileInputPath}")
    print("Please make sure the file exists and the path is correct.")
    # Exit the script cleanly if the file doesn't exist.
    exit()


# --- DataFrame Creation and Cleaning ---

if not codes:
    print("Warning: No data was parsed from the file. The output will be empty.")
    # Create an empty DataFrame with the correct columns if no data was read.
    clean_data = pd.DataFrame(columns=['code', 'description', 'level'])
else:
    # Create the DataFrame from the list of dictionaries.
    # Pandas automatically uses the dictionary keys as column names.
    raw_data = pd.DataFrame(codes)

    # Select only the columns you need for the final output.
    cols_to_keep = ['code', 'description', 'level']
    clean_data = raw_data[cols_to_keep].copy() # Use .copy() to avoid SettingWithCopyWarning

    # Here you would call your column normalization function.
    # For example: clean_data = normalizeColumnNames(clean_data, pd)
    clean_data.columns = [col.lower().replace(' ', '_') for col in clean_data.columns]


## Create a DataFrame from the parsed codes
raw_data = pd.DataFrame(codes)
print( raw_data.head())

raw_data.columns = ['order_num', 'code', 'level', 'description', 'description_detailed']
print( raw_data.head())
## Clean data
cols = ['code', 'description','level']
clean_data = raw_data[cols]
print(clean_data.head())
## rename columns and add last_updated column with current date
clean_data =normalizeColumnNames(clean_data, pd)

## save clean data to output
save_to_formats(clean_data, fileInputPath,fileOutputPath, "icd10cm_2026_processed.csv")

