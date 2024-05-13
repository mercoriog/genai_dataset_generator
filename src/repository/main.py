import os

MAIN_FOLDER_NAME = "genai_dataset_generator"

def getMainFolderPath():
    # Project tree is 'genai_dataset_generator/src/repository/main.py'.

    # Get root path of this file 'main.py'.
    # So <ROOT_PATH> is the path to 'repository' folder.
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

    # Get main folder path going back to 'genai_dataset_generator' folder.
    main_folder_path = os.path.join(ROOT_PATH, "..", "..")
    
    # Return main folder path.
    return main_folder_path