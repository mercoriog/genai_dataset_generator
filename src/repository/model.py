from repository import aicaptioning as aicapt
import os

MODEL_FOLDER_NAME = "base_model"
MODEL_URL = r"https://drive.google.com/file/d/1Kg4Iz5WN3pLKYl15yCqEHAIi4xVpVxaR/view?usp=sharing"
ZIP_MODEL_NAME = "BlipBaseModel.zip"

def getModelURL():
    # Return AI Model URL string.
    return MODEL_URL

def getModelFolderPath():
    # Get 'aicaptioning' folder path.
    aicapt_folder_path = aicapt.getAiCaptioningFolderPath()

    # Build Model folder path.
    model_folder_path = os.path.join(aicapt_folder_path, MODEL_FOLDER_NAME)

    # Check if Model folder exists:
    if os.path.exists(model_folder_path) == False:
        # Create Model folder:
        os.mkdir(model_folder_path)

    # Return Model folder path.
    return model_folder_path

def getZIPModelPath():
    # Get Model folder path.
    model_folder_path = getModelFolderPath()

    # Build ZIP Model file path.
    zip_model_path = os.path.join(model_folder_path, ZIP_MODEL_NAME)

    # Return ZIP Model file path.
    return zip_model_path