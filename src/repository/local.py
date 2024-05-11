from repository import source
import os

LOCAL_FOLDER_NAME = "local"

def getLocalFolderPath():
    # Get main folder name.
    main_folder_path = source.getMainFolderPath()

    # Build 'local' folder path.
    local_folder_path = os.path.join(main_folder_path, LOCAL_FOLDER_NAME)
    
    # Check if 'local' folder exists:
    if os.path.exists(local_folder_path) == False:
        # Create 'local' folder.
        os.mkdir(local_folder_path)

    # Return 'local' folder path.
    return local_folder_path