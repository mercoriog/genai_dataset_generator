from repository import main
import os

MANUAL_FILE_NAME = "Manual.txt"

def getManualFilePath():
    # Get main folder name.
    main_folder_path = main.getMainFolderPath()

    # Build manual file path.
    manual_file_path = os.path.join(main_folder_path, MANUAL_FILE_NAME)

    # Return manual file path.
    return manual_file_path