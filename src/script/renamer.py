from repository import output
import shutil
import os 

def findPadding(num):
    # This function returns the number of necessary digits in order to enumerate files, 
    # depending on files' number passed as input.
    if num < 100:
        return 3
    elif num < 1000:
        return 4
    elif num < 10000:
        return 5
    elif num < 100000:
        return 6
    else: return 7

def getPaddedString(padding, value):
    # This function returns a padded string depending on:
    # - padding: the length of the entire digit sequence;
    # - value: the value to pad.
    
    # <fill> is the nuber of '0' characters to print.
    fill = padding - len(str(value))

    # Concatenate 0 digits with the value to pad.
    padded_str = f"{'0' * fill}{str(value)}"

    # Return a padded string like '031' or '00xyz'
    return padded_str

def renameImages(folder, token):
    # This function gets as input parameters:
    # - folder: a list of files' path;
    # - token: a string.
    # This function returns a list of renamed files' path.

    # Build a list for renamed files' path.
    renamed_folder = []
    
    # Caluclate padding in order to format strings like 'filename-0xx.ext'.
    padding = findPadding(len(folder))
    
    # Inizialize a counter for enumaration.
    count = 0
    
    # Get the output folder's path where to store renamed folder's files.
    out_folder_path = output.getOutputFolderPath()

    # For each file in input folder's list:
    for file in folder:
        # Update counter.
        count += 1

        # Get padded string to go from 'filename.ext' to 'filename-00xx.ext'. 
        padded_str = getPaddedString(padding, count)
        
        # Build formatted filename with .png extension
        new_basename = f"{token}-{padded_str}.png"

        # Build the correct filename (basename + path).
        new_filename = os.path.join(out_folder_path, new_basename)
        
        # Create a copy of current file reanamed as new formatted name.
        shutil.copy(file, new_filename)
        
        # Add renamed file's path in <renamed_folder> list.
        renamed_folder.append(new_filename)

    # Return a list of files' path.
    return renamed_folder