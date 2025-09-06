import pandas as pd

fileInputPath ='input/LOINC/Loinc.csv'
fileOutpuPath='output/loinc_2025.csv'

#load raw_data
raw_data = pd.read_csv(fileInputPath,low_memory=False)
cols = ['LOINC_NUM', 'COMPONENT', 'CLASSTYPE', 'STATUS']

#clean data
clean_data = raw_data [cols]
clean_data=clean_data.rename (columns={
    'LOINC_NUM':'code',
    'COMPONENT':'description',
    'CLASSTYPE':'category',
    'STATUS':'status',
    })

## hardcode current date value on last_updated column
clean_data[['last_updated']] = pd.Timestamp.today().normalize()

#save clean data to output
clean_data.to_csv(fileOutpuPath)


"""
def load_loinc_data(fileInputPath): 
    #Load raw loinc data file to dataframe
    raw_data = pd.read_csv(fileInputPath,low_memory=False)
    return raw_data

def clean_loinc_data(raw_data):
    # Clean and standardize LOIN codes retrive CODE, DESCRIPTION, CATEGORY, STATUS
    # Column list  = LOINC_NUM, COMPONENT, CLASSTYPE, STATUS
    #-`code`: The primary identifier
    #- `description`: Human-readable description
    #- `category`: High-level grouping (where applicable)
    #- `status`: Active/Inactive/Retired
    #- `effective_date`: When code became effective
    #- `last_updated`: Processing timestamp
    
    cols = ['LOINC_NUM', 'COMPONENT', 'CLASSTYPE', 'STATUS']
    clean_data = raw_data [cols]
    #Rename data columns
    clean_data=clean_data.rename (columns={
    'LOINC_NUM':'code',
    'COMPONENT':'description',
    'CLASSTYPE':'category',
    'STATUS':'status',
    })

    #add hardcoded date to extract file
    clean_data[['last_updated']] = pd.Timestamp.today().normalize()
    return clean_data
def save_to_formats(clean_data, fileOutputPath):
    clean_data.to_csv(fileOutputPath)

if __name__ == "__main__":
    import logging
    fileInputPath ='input/LOINC/Loinc.csv'
    fileOutpuPath='output/loinc_2025.csv'
    logging.basicConfig(level=logging.INFO)
    
    # Load raw data
    raw_data = load_loinc_data(fileInputPath)
    
    # Clean and process
    clean_data = clean_loinc_data(raw_data)

    # Save outputs
    save_to_formats(clean_data, fileOutpuPath)
    
    logging.info("Loinc processing completed")
    main()

"""