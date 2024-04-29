import shutil
from script import folder_controller as foldc

def checkParams(folder, size, token, use_ai, every_caption):
    # This function is a parameters checker for 'script.generator' module.
    # This function returns True if none of the following conditions is satisfied.

    # Check the None value for each input parameter.
    if folder == None or size == None or token == None or use_ai == None or every_caption == None:
        return False

    # Check if <folder> list is empty.
    if len(folder) == 0:
        return False

    # Check if <token> string is empty.
    if token == "":
        return False

    # Return True as default value.
    return True

def initialize():
    # This function ensures that the operations' folders are ready to use.
    # This function returns True if no exception occurs.

    # Set an exception handler:
    try:
        # Get the 'local' folder path.
        local_folder_path = foldc.getLocalFolderPath()

        # Remove every files and folders from the 'local' folder.
        shutil.rmtree(local_folder_path)

    # An exception occurs:
    except:
        return False

    return True