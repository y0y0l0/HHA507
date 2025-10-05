import pandas as pd
import os as os
from util.common_functions import adjust_path_based_on_OS

# --- Import CSV files ---
#file resides in the sibling directory "data"
file_input_path = adjust_path_based_on_OS('../data/patient.csv')
# Read the CSV file into a DataFrame
df = pd.read_csv(file_input_path)
df.describe()
