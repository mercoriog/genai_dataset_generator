from controller import folder_controller as foldc
import os

def createManualFile():
    # This function create a manual file 
    # and store it as input file path.

    # Get manual file path.
    manual_file_path = foldc.getManualFilePath()

    # Set an exception handler:
    try:
        # Open a new file with input file path.
        manual_file = open(manual_file_path, "w")
        
        # Write the text.
        manual_file.write('''
            If you see this file you are probabily using wrong Genai Dataset Generator app.\n
            Here are NECESSARY steps to follow for a correct use:\n
            1. Upload a folder only containing images.\n
            2. Insert a keyword token.\n
            3. If displayed, wait until file box's countdown ends\n\n
            If you follow this steps and Manual continues to be the generated dataset, there could be a problem with image captioning Model.\n
            If '[PREP]' log message display 'GUI Initialization done.', there are no errors related to Model and problems can be related to uploaded folder.\n 
            ''')
        
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
