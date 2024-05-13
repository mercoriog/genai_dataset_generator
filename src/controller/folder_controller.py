from repository import local
import os
import shutil

def initFolders():
    # This function ensure that 'local' folder is empty.
    # Set an exception handler:
    try:
        # Get the 'local' folder path.
        local_folder_path = local.getLocalFolderPath()

        # Remove every files and folders from the 'local' folder.
        shutil.rmtree(local_folder_path)
    
    # An exception occurs:
    except Exception as e: 
        # Print the exception.
        print("[ERROR] " + str(e))
        # Return False if error occurs.
        return False

    # This function returns True only if no Exception occurs.
    return True