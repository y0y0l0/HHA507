import pandas as pd
import os
import zipfile  # Import the zipfile library (though it's usually not needed)

# GitHub's file size limit in bytes
github_limit_bytes = 100 * 1024 * 1024
# This function will create third column with the current date and return data with the column renamed as follows:
# Code - first Column
# Description - Second Column
# Load_Date - third column with current date
def normalizeColumnNames(input_df, input_pd):
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

def save_to_formats(input_df, fileInputPath,fileOutputPath, filename):
   
    # Check if the output directory exists
    if not os.path.exists(fileOutputPath):
        print(f"The file '{fileOutputPath}' does not exist.")
        os.makedirs(fileOutputPath)
        print(f"Created new directory '{fileOutputPath}' .")
    # Construct the full output file path
    print(fileOutputPath+"/"+filename) 
    output_file_path = fileOutputPath+"/"+filename
    print(f"Output file path: {output_file_path}")
    # Save the DataFrame to CSV
    input_df.to_csv(output_file_path)
    print(f"Successfully parsed {len(input_df)} records from {fileInputPath}")
    print(f"Saved to {output_file_path}")  
    
    # Get the file size *after* saving
    file_size = os.path.getsize(output_file_path)

    # Check if the file size exceeds the limit
    if file_size > github_limit_bytes:
        print("The file is too large to be published to GitHub directly, compressing file.")
        compressed_file_path = output_file_path + ".zip"
        try:
            input_df.to_csv(compressed_file_path, index=False, compression='zip')
            print(f"Successfully parsed {len(input_df)} records from {fileInputPath}")
            print(f"Saved to {compressed_file_path} (compressed)")
            # remove the original uncompressed file to save space
            os.remove(output_file_path)
        except Exception as e:
             print(f"Error during compression: {e}")

    print(f"\nFirst 5 rows:")
    print(input_df.head())     
def main():
 ## Load loinc data to dataframe
 loinc = pd.read_csv('input/LOINC/Loinc.csv', usecols=[0,1,2])
 loinc.head()

 fileInputPath='input/LOINC/Loinc.csv'
 fileOutputPath='output'
 filename = 'Loinc_test.csv'
 ## save to csv format
 save_to_formats(pd,fileInputPath,fileOutputPath,filename)

if __name__ == "__main__":
   main()

    