from repository import source
import os

AICAPTIONING_FOLDER_NAME = "aicaptioning"

def getAiCaptioningFolderPath():
    # Get 'src' folder path.
    src_folder_path = source.getSourceFolderPath()

    # Build 'aicaptioning' folder path.
    aicapt_folder_path = os.path.join(src_folder_path, AICAPTIONING_FOLDER_NAME)

    # Return 'aicaptioning' folder path.
    return aicapt_folder_path

