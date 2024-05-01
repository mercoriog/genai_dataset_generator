import os

MAIN_FOLDER_NAME = "genai_dataset_generator"
LOCAL_FOLDER_NAME = "local"
USER_FOLDER_NAME = "user"
OUTPUT_FOLDER_NAME = "output"
MODEL_FOLDER_NAME = "base_model"
SOURCE_FOLDER_NAME = "src"
AICAPTIONING_FOLDER_NAME = "aicaptioning"
README_FILE_NAME = "README.txt"
GITHUB_REPOSITORY_LINK = "https://github.com/mercoriog/genai_dataset_generator"
MODEL_URL = r"https://drive.google.com/file/d/1jtMA62FBTn9X86gAl-dtTg81NckAk8A7/view?usp=sharing"
ZIP_MODEL_NAME = "BlipBaseModel.zip"

def extractBasename(filename):
    path_to, basename = os.path.split(filename)
    return basename

def getModelURL():
    # Return AI Model URL string.
    return MODEL_URL

def getSourceFolderPath():    
    # Build 'src' folder path.
    src_folder_path = os.path.join(os.getcwd(), MAIN_FOLDER_NAME, SOURCE_FOLDER_NAME)

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
    # Build 'local' folder path.
    local_folder_path = os.path.join(os.getcwd(), MAIN_FOLDER_NAME, LOCAL_FOLDER_NAME)
    
    # Check if 'local' folder exists:
    if os.path.exists(local_folder_path) == False:
        # Create 'local' folder:
        os.mkdir(local_folder_path)

    # Return 'local' folder path.
    return local_folder_path




def getLocalFilename(filename):
    user_folder = getUserFolderPath()
    basename = extractBasename(filename)
    return f"{user_folder}\\{basename}"

def getUserFolderPath():
    # build user folder path from local folder
    user_folder_path = f"{getLocalFolderPath()}\\{USER_FOLDER_NAME}" 
    
    # check if folder exists
    if os.path.exists(user_folder_path) == False:
        # if user folder don't exists then create it
        os.mkdir(user_folder_path)

    return user_folder_path

def getOutputFolderPath():
    # build output data folder from local folder
    out_folder_path = f"{getLocalFolderPath()}\\{OUTPUT_FOLDER_NAME}"

    # check if folder exists
    if os.path.exists(out_folder_path) == False:
        # if out folder don't exists then create it
        os.mkdir(out_folder_path)

    return out_folder_path

def getReadmeFile():
    # build readme filepath
    readme_file_path = f"{MAIN_FOLDER_NAME}\\{README_FILE_NAME}"

    # check if file exists
    if os.path.exists(readme_file_path) == False:
        # if readme file don't exists then create it
        with open(readme_file_path, 'r') as readme_file:
            readme_file.write(
                f"This file is created as original README.txt file is missing.\n \
                Check out at {GITHUB_REPOSITORY_LINK}")

    return readme_file_path

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
