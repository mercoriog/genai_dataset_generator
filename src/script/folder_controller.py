import os

MAIN_FOLDER_NAME = "genai_dataset_generator"
LOCAL_FOLDER_NAME = "local"
USER_FOLDER_NAME = "user"
OUTPUT_FOLDER_NAME = "output"
README_FILE_NAME = "README.txt"
GITHUB_REPOSITORY_LINK = "https://github.com/mercoriog/genai_dataset_generator"

def extractBasename(filename):
    path_to, basename = os.path.split(filename)
    return basename

def getLocalFilename(filename):
    user_folder = getUserFolderPath()
    basename = extractBasename(filename)
    return f"{user_folder}\\{basename}"

def getLocalFolderPath():
    # build the local folder path where to store data
    local_folder_path = f"{os.getcwd()}\\{MAIN_FOLDER_NAME}\\{LOCAL_FOLDER_NAME}"
    
    # check if folder exists
    if os.path.exists(local_folder_path) == False:
        # if local folder don't exists then create it
        os.mkdir(local_folder_path)

    return local_folder_path

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