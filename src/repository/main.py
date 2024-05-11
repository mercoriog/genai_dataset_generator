import os

MAIN_FOLDER_NAME = "genai_dataset_generator"

def extractBasename(filename):
    path_to, basename = os.path.split(filename)
    return basename

def getMainFolderPath():
    current_path = os.getcwd()
    basename = extractBasename(current_path)
    
    if basename == "src":
        os.chdir("..")
        current_path = os.getcwd()
    
    return current_path