import os
import shutil

MAIN_FOLDER_NAME = "genai_dataset_generator"
LOCAL_FOLDER_NAME = "local"
USER_FOLDER_NAME = "user"
OUTPUT_FOLDER_NAME = "output"
MODEL_FOLDER_NAME = "base_model"
SOURCE_FOLDER_NAME = "src"
AICAPTIONING_FOLDER_NAME = "aicaptioning"
MANUAL_FILE_NAME = "Manual.txt"
GITHUB_REPOSITORY_LINK = "https://github.com/mercoriog/genai_dataset_generator"
MODEL_URL = r"https://drive.google.com/file/d/1jtMA62FBTn9X86gAl-dtTg81NckAk8A7/view?usp=sharing"
ENV_URL = r""
ENV_FOLDER_NAME = "genaienv"
ZIP_MODEL_NAME = "BlipBaseModel.zip"

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

def getModelURL():
    # Return AI Model URL string.
    return MODEL_URL

def getSourceFolderPath():    
    # Get main folder name.
    main_folder_path = getMainFolderPath()

    # Build 'src' folder path.
    src_folder_path = os.path.join(main_folder_path, SOURCE_FOLDER_NAME)

    # Return 'src' folder path.
    return src_folder_path

def getAiCaptioningFolderPath():
    # Get 'src' folder path.
    src_folder_path = getSourceFolderPath()

    # Build 'aicaptioning' folder path.
    aicapt_folder_path = os.path.join(src_folder_path, AICAPTIONING_FOLDER_NAME)

    # Return 'aicaptioning' folder path.
    return aicapt_folder_path

def getModelFolderPath():
    # Get 'aicaptioning' folder path.
    aicapt_folder_path = getAiCaptioningFolderPath()

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

def getLocalFolderPath():
    # Get main folder name.
    main_folder_path = getMainFolderPath()

    # Build 'local' folder path.
    local_folder_path = os.path.join(main_folder_path, LOCAL_FOLDER_NAME)
    
    # Check if 'local' folder exists:
    if os.path.exists(local_folder_path) == False:
        # Create 'local' folder.
        os.mkdir(local_folder_path)

    # Return 'local' folder path.
    return local_folder_path

def getUserFolderPath():
    # Get 'local' folder path.
    local_folder_path = getLocalFolderPath()
    
    # Build 'user' folder path from 'local' folder.
    user_folder_path = os.path.join(local_folder_path, USER_FOLDER_NAME)
    
    # Check if 'user' folder exists:
    if os.path.exists(user_folder_path) == False:
        # Create 'user' folder.
        os.mkdir(user_folder_path)

    # Return 'user' folder path.
    return user_folder_path

def buildUserFolderFile(file_path):
    # This function build a 'user' folder path from file.
    # It extract the basename (name.ext) from input file path
    # and concatenate it with 'user' folder path.

    # Get user folder path.
    user_folder_path = getUserFolderPath()
    
    # Get basename of input file path.
    basename = extractBasename(file_path)
    
    # Build path with 'user' folder. 
    user_folder_file_path = os.path.join(user_folder_path, basename)
    
    # Return file path in 'user' folder.
    return user_folder_file_path

def getOutputFolderPath():
    # Get 'local' folder path.
    local_folder_path = getLocalFolderPath()
    
    # Build 'output' folder path.
    output_folder_path = os.path.join(local_folder_path, OUTPUT_FOLDER_NAME)

    # check if folder exists:
    if os.path.exists(output_folder_path) == False:
        # Create 'output' folder
        os.mkdir(output_folder_path)

    return output_folder_path

def getManualFilePath():
    # Get main folder name.
    main_folder_path = getMainFolderPath()

    # Build manual file path.
    manual_file_path = os.path.join(main_folder_path, MANUAL_FILE_NAME)

    # Return manual file path.
    return manual_file_path

def initFolders():
    # Set an exception handler:
    try:
        # Get the 'local' folder path.
        local_folder_path = getLocalFolderPath()

        # Remove every files and folders from the 'local' folder.
        shutil.rmtree(local_folder_path)
    
    # An exception occurs:
    except Exception as e: 
        # Print the exception.
        print("[ERROR] " + str(e))
        return False

    # This function returns True only if no Exception occurs.
    return True

def getEnvUrl():
    return ENV_URL

def getEnvFolderPath():
    # Get main folder name.
    main_folder_path = getMainFolderPath()

    # Build 'genainev' folder path.
    genaienv_folder_path = os.path.join(main_folder_path, ENV_FOLDER_NAME)

    # Return 'genaienv' folder path
    return genaienv_folder_path