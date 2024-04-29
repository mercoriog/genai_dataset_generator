import shutil
import folder_controller as foldc

def generateArchiveFile(from_folder, to_folder):
    # This function generates an archive file from <from_folder> path 
    # and stores it in <to_folder> path.
    # This function returns the path of the generated archive file.
    
    # Build the archive file's name:
    # starting from <to_folder>, add a new subfolder named 'dataset'. 
    archive_filename = f"{to_folder}\\dataset"
    
    # Generate the archive file. 
    shutil.make_archive(archive_filename, 'zip', from_folder)
    
    # Build the actual archive file path.
    archive_file_path = f"{archive_filename}.zip"

    # Return the archive file path.
    return archive_file_path

def archiveProcessedData():
    # This function creates an archive file from files
    # stored in 'output' folder.
    # The generated archive file will be stored in 'local' folder.

    # Get 'output' folder path.
    out_folder_path = foldc.getOutputFolderPath()

    # Get 'local' folder path.
    local_folder_path = foldc.getLocalFolderPath()
    
    # Build the archive file containing files from the output folder      
    archive_file_path = generateArchiveFile(output_folder_path, local_folder_path)

    # Return the archive file path
    return archive_file_path
