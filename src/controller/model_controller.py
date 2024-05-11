from service import downloader as down
from repository import model as modellib
import os

def loadModel():
    # This function download the model from web and store it in Model folder.
    # Get path where to store the ZIP Model file.  
    zip_model_path = modellib.getZIPModelPath()
    
    # Get ZIP Model URL.
    zip_model_URL = modellib.getModelURL()
    
    # Download ZIP Model and unzip to get it ready to use.
    # Set 'delete_when_unzipped=True' param to delete ZIP file after unzip operation.
    model = down.downloadAndUnzip(zip_model_URL, zip_model_path, True)

    # This function returns True if Model is loaded.
    # If any error occurs, <model> value is False.
    return model

def checkModel():
    # This function checks if Model is ready to use.
    # Model is expected to be downloaded and stored in Model folder.
    
    # Get Model folder path.
    model_folder_path = modellib.getModelFolderPath()

    # List all Model folder file.
    model_folder_files = os.listdir(model_folder_path)

    # If Model folder is empty:
    if len(model_folder_files) == 0:
        # Return False
        return False

    # This function returns True if Model is not empty.
    return True

def initModel():
    # Get Model folder path.
    model_folder_path = modellib.getModelFolderPath()
    
    # Check if Model is loaded.
    model = checkModel()

    # If Model is not loaded:
    if not model:
        # Notify Model not loaded.
        print("[PREP] Model NOT loaded.")

        model = loadModel()

        # Check if Model loading is done:
        if model == True:
            # Notify initialization done.
            print("[PREP] Model loaded with no errors.")

    # This function returns True if Model is loaded.
    # If any error occurs, <model> value is False.
    return model
