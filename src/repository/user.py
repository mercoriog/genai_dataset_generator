from repository import local
import os

USER_FOLDER_NAME = "user"

def getUserFolderPath():
    # Get 'local' folder path.
    local_folder_path = local.getLocalFolderPath()
    
    # Build 'user' folder path from 'local' folder.
    user_folder_path = os.path.join(local_folder_path, USER_FOLDER_NAME)
    
    # Check if 'user' folder exists:
    if os.path.exists(user_folder_path) == False:
        # Create 'user' folder.
        os.mkdir(user_folder_path)

    # Return 'user' folder path.
    return user_folder_path

def extractBasename(filename):
    # This function split file's path in two parts.
    path_to, basename = os.path.split(filename)

    # Return the 'name.ext' of the file.
    return basename

def buildUserFolderFile(file_path):
    # This function build a 'user' folder path from file.
    # It extract the basename (name.ext) from input file path
    # and concatenate it with 'user' folder path.

    # Get user folder path.
    user_folder_path = getUserFolderPath()
    
    # Get basename of input file path.
    basename = extractBasename(file_path)
    
    # Build path with 'user' folder. 
    user_folder_file_path = os.path.join(user_folder_path, basename)
    
    # Return file path in 'user' folder.
    return user_folder_file_path