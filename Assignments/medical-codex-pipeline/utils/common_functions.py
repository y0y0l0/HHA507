import pandas as pd
import os

# This function will create third column with the current date and return data with the column renamed as follows:
# Code - first Column
# Description - Second Column
# Load_Date - third column with current date
def renameOutput(input_df):
    
    input_df=input_df.rename (columns={
    ''+input_df.columns[0]+'':'code',
    ''+input_df.columns[1]+'':'description',
    })
    input_df['last_udpated'] = input_df.Timestamp.today().normalize()

def save_to_formats(df, fileOutputPath, filename):
    #check if path exists
    if os.path.exists(fileOutputPath):
        df.to_csv(fileOutputPath+"/"+filename)
    else:
        print(f"The file '{fileOutputPath}' does not exist.")
#if __name__ == "__main__":
def main():
 loinc = pd.read_csv('input/LOINC/Loinc.csv', usecols=[0,1])
 fileOutputPath='output'
 filename = 'Loinc_test.csv'
 renameOutput(loinc)
 save_to_formats(loinc, fileOutputPath,filename)

    