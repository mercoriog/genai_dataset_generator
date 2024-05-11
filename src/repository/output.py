from repository import local
import os

OUTPUT_FOLDER_NAME = "output"

def getOutputFolderPath():
    # Get 'local' folder path.
    local_folder_path = local.getLocalFolderPath()
    
    # Build 'output' folder path.
    output_folder_path = os.path.join(local_folder_path, OUTPUT_FOLDER_NAME)

    # check if folder exists:
    if os.path.exists(output_folder_path) == False:
        # Create 'output' folder
        os.mkdir(output_folder_path)

    return output_folder_path
