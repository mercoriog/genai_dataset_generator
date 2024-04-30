from script import downloader as down
from script import folder_controller as foldc
import shutil
import os

def checkModel():
    # Get Model folder path.
    model_folder_path = foldc.getModelFolderPath()

    # List all Model folder file.
    model_folder_files = os.listdir(model_folder_path)

    # If Model folder is empty:
    if len(model_folder_files) == 0:
        # Return False
        return False

    # This function returns True if Model is not empty.
    return True

def initGUI():
    # Notify initialization.
    print("[PREP] Start GUI initialization...")

    # Get Model folder path.
    model_folder_path = foldc.getModelFolderPath()
    
    # Check if Model is loaded.
    model = checkModel()

    # If Model is not loaded:
    if not model:
        # Notify Model not loaded.
        print("[PREP] Model NOT loaded.")

        # Get path where to store the ZIP Model file.  
        zip_model_path = foldc.getZIPModelPath()
        
        # Get ZIP Model URL.
        zip_model_URL = foldc.getModelURL()
        
        # Download ZIP Model and unzip to get it ready to use.
        # Set 'delete_when_unzipped=True' param to delete ZIP file after unzip operation.
        model = down.downloadAndUnzip(zip_model_URL, zip_model_path, True)

    # Check if initialization done:
    if model == True:
        # Notify initialization done.
        print("[PREP] GUI initialization done.")

    # This function returns True if Model is loaded.
    # If any error occurs, <model> value is False.
    return model


def initFolders():
    # Set an exception handler:
    try:
        # Get the 'local' folder path.
        local_folder_path = foldc.getLocalFolderPath()

        # Remove every files and folders from the 'local' folder.
        shutil.rmtree(local_folder_path)
    
    # An exception occurs:
    except Exception as e: 
        # Print the exception.
        print("[ERROR] " + str(e))
        return False

    # This function returns True only if no Exception occurs.
    return True

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

def initGenerator(folder, size, token, use_ai, every_caption):
    # This function ensures that parameters of 'script.generator' modue are correctly loaded, 
    # ensures that operations' folders are ready to use
    # and, if allowed, it ensures that AI model is correctly loaded.

    # Call the parameters checker function.
    params = checkParams(folder, size, token, use_ai, every_caption)
    # If there are issues with paramteres, <params> is False:
    if not params:
        # Notify issues.
        return False
    
    # Call the folder initializer function.
    folders = initFolders()
    # If there are issues with folder initialization, <folders> is False:
    if not folders:
        # Notify issues.
        return False

    # Check if AI Model usage is allowed: 
    if use_ai is True:
        # Call the AI Model checker function.
        model = checkModel()
        # If there are issues with AI Model, <model> is False:
        if not model:
            # Notify issues.
            return False

    # This function returns True if there are no issues with parameters,
    # operations' folders initialization 
    # and, if allowed, no issues with AI Model.
    return True