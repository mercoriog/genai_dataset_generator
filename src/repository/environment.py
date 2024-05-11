from controller import folder_controller as foldc
import os

ENV_URL = r""
ENV_FOLDER_NAME = "genaienv"

def getEnvUrl():
    return ENV_URL

def getEnvFolderPath():
    # Get main folder name.
    main_folder_path = foldc.getMainFolderPath()

    # Build 'genainev' folder path.
    genaienv_folder_path = os.path.join(main_folder_path, ENV_FOLDER_NAME)

    # Return 'genaienv' folder path
    return genaienv_folder_path