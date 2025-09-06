import pandas as pd
import re

fileInputPath= 'input/ICD_10_CM_US/icd10cm_order_2026.txt'
fileOutputPath ='output/icd10cm_order_2026.csv'


## Load raw_data
# This initializes a blank list to hold the parsed codes (e.g., individual rows from the text file)
codes = []

with open(fileInputPath, 'r', encoding='utf-8') as file:
    for line in file:

        # Remove whitespace and check line length
        line = line.rstrip('\n\r')
        if len(line) < 15:  # Skip lines that are too short
            continue

        # Parse the fixed-length format based on pdf instructions
        order_num = line[0:5].strip()  # Order number, first 6 characters
        code = line[6:13].strip()  # ICD-10-CM code, characters 7-13
        level = line[14:15].strip()  # Level indicator (0 or 1), character 15

        # Parse description and description_detailed that follows
        remaining_text = line[16:]  # Text after position 16
        
        # Split by 4+ consecutive spaces to separate description from description_detailed
        parts = re.split(r'\s{4,}', remaining_text, 1)

        # Extract description and description_detailed
        description = parts[0].strip() if len(parts) > 0 else ""
        description_detailed = parts[1].strip() if len(parts) > 1 else ""

        # Append the parsed data to the codes list
        codes.append({
            'order_num': order_num,
            'code': code,
            'level': level,
            'description': description,
            'description_detailed': description_detailed
        })

## Create a DataFrame from the parsed codes
raw_data = pd.DataFrame(codes)
raw_data
## Clean data
cols = ['code', 'description']
clean_data = raw_data[cols]
## hardcode current date value on last_updated column
clean_data[['last_updated']] = pd.Timestamp.today().normalize()
## Save the DataFrame to a CSV file
clean_data.to_csv(fileOutputPath)


