from repository import user
import shutil

def copyFolder(folder):
    # This function take a list of files' path and copy them in 'local\user' folder.
    # This function returns the list of copied files' path.
    
    # Build a new list to store copied files' path.
    local_folder = []

    # For each file in input folder:
    for file in folder:
        # Define new path for the current file using its basename. 
        local_filename = user.buildUserFolderFile(file)
        
        # Create a copy of the current file and store it in 'local\user' folder.
        shutil.copy(file, local_filename)
        
        # Add copied file's path in <local_folder> list.
        local_folder.append(local_filename)

    # Return a list of copied filed stored in 'local\user' folder.
    return local_folder