import gc
import pandas as pd
import os
import zipfile  # Import the zipfile library to handle compression
import gc as gc

# GitHub's file size limit in bytes
github_limit_bytes = 100 * 1024 * 1024
# This function will create third column with the current date and return data with the column renamed as follows:
# Code - first Column
# Description - Second Column
# Load_Date - third column with current date
# If there are more than two columns, it will rename them as follows:
def normalizeColumnNames(input_df: pd.DataFrame, input_pd: pd) -> pd.DataFrame:
    ## Rename columns and add last_updated column with current date
    numColumn =len(input_df.columns)
    match numColumn:
        case 2:
            ## Rename columns
            ## Assuming the input dataframe has exactly two columns
            input_df=input_df.rename (columns={
            ''+input_df.columns[0]+'':'code',
            ''+input_df.columns[1]+'':'description',
            })
            print("Two columns found")
        case 3:
            ## Rename columns
            ## Assuming the input dataframe has exactly three columns
            input_df=input_df.rename (columns={
            ''+input_df.columns[0]+'':'code',
            ''+input_df.columns[1]+'':'description',
            ''+input_df.columns[2]+'':'category',
            })
            print("Three columns found")
        case 4:
            ## Rename columns
            ## Assuming the input dataframe has exactly four columns
            input_df=input_df.rename (columns={
            ''+input_df.columns[0]+'':'code',
            ''+input_df.columns[1]+'':'description',
            ''+input_df.columns[2]+'':'category',
            ''+input_df.columns[3]+'':'active',
            })
            print("Four columns found")
        case 5:
            ## Rename columns
            ## Assuming the input dataframe has exactly four columns
            input_df=input_df.rename (columns={
            ''+input_df.columns[0]+'':'code',
            ''+input_df.columns[1]+'':'description',
            ''+input_df.columns[2]+'':'category',
            ''+input_df.columns[3]+'':'active',
            ''+input_df.columns[4]+'':'effective_datetime',
            })
            print("Five columns found")
        case _:
             raise ValueError("Input dataframe must have at least two columns.")
            
    ## Add last_updated column with current date
    input_df['last_updated'] = input_pd.Timestamp.today().normalize()
    return input_df
## This function saves the dataframe to csv format and compresses it if it exceeds GitHub's file size limit
def save_to_formats(input_df: pd.DataFrame, fileInputPath: str, fileOutputPath: str, filename: str):
    # Check if the output directory exists
    if not os.path.exists(fileOutputPath):
        print(f"The file '{fileOutputPath}' does not exist.")
        os.makedirs(fileOutputPath)
        print(f"Created new directory '{fileOutputPath}' .")
    # Construct the full output file pathS
    output_file_path = fileOutputPath+"/"+filename
    print(f"Output file path: {output_file_path}")
    # Save the DataFrame to CSV
    input_df.to_csv(output_file_path, index = False)
  
    print(f"Successfully parsed {len(input_df)} records from {fileInputPath}")
    print(f"Saved to {output_file_path}")  
    print(f"\nMemory usage (MB): {input_df.memory_usage().sum() / 1024**2:.2f}")

    # Get the file size *after* saving
    file_size = os.path.getsize(output_file_path)

    # Check if the file size exceeds the limit 100 MB
    if file_size > github_limit_bytes:
        print("The file is too large to be published to GitHub directly, compressing file.")
        compressed_file_path = output_file_path .replace (".csv", ".zip")
        print (f"Compressed file path: {compressed_file_path}")
        try:
            input_df.to_csv(compressed_file_path, index=False, compression='zip')
            
            print(f"Successfully parsed {len(input_df)} records from {fileInputPath}")
            print(f"Saved to {compressed_file_path} (compressed)")
            # remove the original uncompressed file to save space
            os.remove(output_file_path)
        except Exception as e:
             print(f"Error during compression: {e}")
    gc.collect()  # Force garbage collection to free up memory
    input_df.flush()
    print(f"\nView of the first 5 rows:")
    print(input_df.head())  
# Adjust file path for Linix/Mac operating systems
def adjust_path_based_on_OS(file_path:str):
    # Adjust file path for Mac if necessary
    if os.uname() == 'Darwin':
        print("This is Linux or Mac OS."+ os.uname())
        file_path = file_path.replace('/','\\')
    return file_path
def main():
    # Load loinc data into the 'loinc' DataFrame
    loinc = pd.read_csv('input/LOINC/Loinc.csv', usecols=[0,1,2])
    
    # Print head for verification (optional)
    print(loinc.head())
    
    #Path to the LOINC csv file
    fileInputPath = adjust_path_based_on_OS('input/LOINC/Loinc.csv')
    fileOutputPath='output'

    #load raw_data
    raw_data = pd.read_csv(fileInputPath,low_memory=False)
    cols = ['LOINC_NUM', 'COMPONENT', 'CLASSTYPE', 'STATUS']

    #clean data
    clean_data = raw_data [cols]
    clean_data=normalizeColumnNames(clean_data, pd)

    ## save cleaned data to output path
    save_to_formats(clean_data, fileInputPath,fileOutputPath, "loinc2025_processed.csv")

if __name__ == "__main__":
    main()

    