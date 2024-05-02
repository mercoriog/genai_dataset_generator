from controller import folder_controller as foldc

def createManualFile():
    # This function create a manual file 
    # and store it as input file path.

    # Get manual file path.
    manual_file_path = foldc.getManualFilePath()

    # Set an exception handler:
    try:
        # Open a new file with input file path.
        manual_file = open(manual_file_path, 'w')
        
        # Write the text.
        manual_file.write(f"This file is created as original README.txt file is missing. Check out at {GITHUB_REPOSITORY_LINK}")
        
        # Close manual file
        manual_file.close()

    # An error occurs:
    except Exception as e:
        # Notify error.
        print(f"[ERROR] Creating manual file failed. Message: ", e)

def getManualFile():
    # Get manual file path.
    manual_file_path = foldc.getManualFilePath()

    # Check if manual file exists:
    if os.path.exists(manual_file_path) == False:
        # Create manual file:
        manual = createManualFile()

    # Return manual file path.
    return manual_file_path
