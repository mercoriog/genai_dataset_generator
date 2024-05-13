from repository import main
import os

ENV_URL = r"https://drive.google.com/file/d/1GazpS6-wgh8lJzuZu6S20XrkgihelfUe/view?usp=sharing"
ENV_FOLDER_NAME = "genaienv"
ZIP_ENV_NAME = "genaienv.zip"

def getEnvURL():
    return ENV_URL

def getEnvFolderPath():
    # Get main folder name.
    main_folder_path = main.getMainFolderPath()

    # Build 'genainev' folder path.
    env_folder_path = os.path.join(main_folder_path, ENV_FOLDER_NAME)

    # check if folder exists:
    if os.path.exists(env_folder_path) == False:
        # Create 'output' folder
        os.mkdir(env_folder_path)

    # Return 'genaienv' folder path
    return env_folder_path

def getZIPEnvPath():
    # Get environment folder path.
    env_folder_path = main.getMainFolderPath()

    # Build .zip env file path.
    zip_env_path = os.path.join(env_folder_path, ZIP_ENV_NAME)

    # Return .zip environment file path.
    return zip_env_path