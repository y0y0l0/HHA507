import pandas as pd
import platform as platform
import gc as gc
import os as os

# GitHub's file size limit in bytes
github_limit_bytes = 100 * 1024 * 1024  # 100 MB
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
    print(f"\nView of the first 5 rows:")
    print(input_df.head())  
# Adjust file path for Linix/Mac operating systems
def adjust_path_based_on_OS(file_path: str) -> str:
    """Adjusts file path separators for the current operating system."""
    # This is the correct, cross-platform way to check the OS
    if platform.system() == 'Windows':
        return file_path.replace('/', '\\')
    else:
        return file_path.replace('\\', '/')
def adjust_path_based_on_OS(file_path: str) -> str:
    """Adjusts file path separators for the current operating system."""
    # This is the correct, cross-platform way to check the OS
    if platform.system() == 'Windows':
        return file_path.replace('/', '\\')
    else:
        print(f"Operating System: {os.uname()}")
        return file_path.replace('\\', '/')