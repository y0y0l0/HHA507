import pandas as pd
import os

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
        case _:
             raise ValueError("Input dataframe must have at least three columns.")
            
    ## Add last_updated column with current date
    input_df['last_updated'] = input_pd.Timestamp.today().normalize()
    return input_df

def save_to_formats(input_df, fileInputPath,fileOutputPath, filename):
    #check if path exists
    if os.path.exists(fileOutputPath):
        input_df.to_csv(fileOutputPath+"/"+filename)
        print(f"Successfully parsed {len(input_df)} records from {fileInputPath}")
        print(f"Saved to {fileOutputPath}/{filename}")
        print(f"\nFirst 5 rows:")
        print(input_df.head())
    else:
        print(f"The file '{fileOutputPath}' does not exist.")
        os.makedirs(fileOutputPath)
        print(f"Created new directory '{fileOutputPath}' .")
        
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

    