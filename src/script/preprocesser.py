from controller import folder_controller as foldc
from controller import model_controller as modc
import shutil
import os

def initGUI():
    # Notify initialization.
    print("[PREP] Start GUI initialization...")
    print("[PREP] current dir:" + os.getcwd())

    # Initialize AI Model.
    model = modc.initModel()

    # Check if initialization is done:
    if model == True:
        # Notify initialization done.
        print("[PREP] GUI initialization done.")
    else:
        # Notify initialization failure.
        print("[ERROR] GUI initialization failed.")

    # Return True if no error occurs.
    return model

def checkParams(folder, size, token, label, use_ai, every_caption):
    # This function is a parameters checker for 'script.generator' module.
    # This function returns True if none of the following conditions is satisfied.

    # Check the None value for each input parameter.
    if folder == None or size == None or token == None or label == None or use_ai == None or every_caption == None:
        return False

    # Check if <folder> list is empty.
    if len(folder) == 0:
        return False

    # Check if <token> string is empty.
    if token == "":
        return False

    # Return True as default value.
    return True

def initGenerator(folder, size, token, label, use_ai, every_caption):
    # This function ensures that parameters of 'script.generator' modue are correctly loaded, 
    # ensures that operations' folders are ready to use
    # and, if allowed, it ensures that AI model is correctly loaded.

    # Call the parameters checker function.
    params = checkParams(folder, size, token, label, use_ai, every_caption)
    # If there are issues with paramteres, <params> is False:
    if not params:
        # Notify issues.
        return False
    
    # Call the folder initializer function.
    folders = foldc.initFolders()
    # If there are issues with folder initialization, <folders> is False:
    if not folders:
        # Notify issues.
        return False

    # Check if labelling is allowed and if AI Model usage is allowed: 
    if label is True and use_ai is True:
        # Call the AI Model checker function.
        model = modc.checkModel()
        # If there are issues with AI Model, <model> is False:
        if not model:
            # Notify issues.
            return False

    # This function returns True if there are no issues with parameters,
    # operations' folders initialization 
    # and, if allowed, no issues with AI Model.
    return True