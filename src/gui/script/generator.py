from PIL import Image
from pathlib import Path
import os
import cv2
import shutil
import numpy as np
from .aicaptioning import image_captioning as aicapt

MAIN_FOLDER_NAME = "genai_dataset_generator"
LOCAL_FOLDER_NAME = "local"
USER_FOLDER_NAME = "user"
OUTPUT_FOLDER_NAME = "output"
README_FILE_NAME = "README.txt"
GITHUB_REPOSITORY_LINK = "https://github.com/mercoriog/genai_dataset_generator"

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

def extractBasename(filename):
    path_to, basename = os.path.split(filename)
    return basename

def extractNameNoExt(filename):
    return Path(filename).stem

def getLocalFilename(filename):
    user_folder = getUserFolderPath()
    basename = extractBasename(filename)
    return f"{user_folder}\\{basename}"

def copyFolder(folder):
    # take a folder list that contains files' path and copy them in 'local\user' folder
    # build a new list to store copied files' path
    local_folder = []
    # for each file in input folder
    for file in folder:
        # define new path for file using its basename and store it in local\user folder
        local_filename = getLocalFilename(file)
        # create a copy of file
        shutil.copy(file, local_filename)
        # add to local folder list
        local_folder.append(local_filename)
    # return a list of copied filed stored in 'local\user'
    return local_folder

def findPadding(dim):
    # return the number of digit for enumerate files, depending on files' number
    if dim < 100:
        return 3
    elif dim < 1000:
        return 4
    elif dim < 10000:
        return 5
    elif dim < 100000:
        return 6
    else: return 7

def getPaddedString(padding, num):
    # calculate the number of '0' character to print for padding
    fill = padding - len(str(num))
    # return a formatted string like '00x' or '0xx'
    return f"{'0' * fill}{str(num)}"

def renameImages(folder, token):
    # build a list for renamed files' path
    renamed_folder = []
    # caluclate padding for formatting string like 'filename-00xx.ext'
    padding = findPadding(len(folder))
    # pick a counter for enamurate
    count = 0
    # get the output folder path where to store renamed folder
    out_folder_path = getOutputFolderPath()
    # for each file in input folder list
    for file in folder:
        # update counter
        count += 1
        # get padded string to go from 'filename.ext' to 'filename-00xx.ext' 
        padded_str = getPaddedString(padding, count)
        # build the formatted filename
        new_filename = f"{out_folder_path}\\{token}-{padded_str}.png"
        # create a copy of current file reanamed as new formatted name
        shutil.copy(file, new_filename)
        # add copied file in renamed folder list
        renamed_folder.append(new_filename)

    # return a list of files path about copied and renamed version of folder list's files provided as input
    return renamed_folder

def extractCaptions(file):
    aicapt.load_model()
    return "ai"

def createTxtFile(filename, token, user_captions, ai_generated_captions):
    # get output folder from disk folder path
    out_folder_path = getOutputFolderPath()
    # build the correct .txt file path
    txt_file_path = f"{out_folder_path}\\{filename}.txt"
    
    # create new .txt file
    txt_file = open(txt_file_path, "w")
    txt_file.write(f"{token}")
    
    # insert user captions if provided 
    if len(user_captions) > 0:
        txt_file.write(f", {user_captions}")
    
    # insert ai generated captions if provided
    if len(ai_generated_captions) > 0:
        txt_file.write(f", {ai_generated_captions}")
    
    txt_file.close()
    return txt_file_path

def imageCaptioning(folder, token, use_ai, user_captions):
    # build a list that contains .txt files' path
    txt_folder = []
    # for each file path in folder input, extract the absolute name (no extension)
    # then extract captions from the image with ai if it is enabled
    # then create the correspondent .txt file with same absolute name which contains
    # the provided token as input, the provided captions as input and 
    # (eventually) the captions provided by ai model 
    for file in folder:
        # extract the absolute filename (no path, no extension)
        filename = extractNameNoExt(file)

        ai_generated_captions = ""
        # check if ai model's use is enabled
        if use_ai == True:
            # generate captions with ai model
            ai_generated_captions = extractCaptions(file)
        
        # generate the .txt file with token and captions 
        txt_file_path = createTxtFile(filename, token, user_captions, ai_generated_captions)

        # add the .txt file path to folder list 
        txt_folder.append(txt_file_path)

    # return a list of .txt file containing captions for each input folder's image
    return txt_folder

def resizeImages(folder, size):
    # build a resized folder list to access every resized file path
    resized_folder_list = []

    # for each file in the input folder 
    for file in folder:
        # load image as array
        img = cv2.imread(file)
        
        # if size is (0,0) don't resize
        if size != (0,0):
            # resize the image
            img = cv2.resize(img, size)

        # save resized image
        cv2.imwrite(file, img)

        # add the file path in resized folder list
        resized_folder_list.append(file)
    
    # return a list of resized files' path
    return resized_folder_list    

def combineFolders(folder_1, folder_2):
    # create a copy of folder_1 list
    combined_folders = [file for file in folder_1]
    
    # append every folder_2 file in combined list
    for file in folder_2:
        combined_folders.append(file)
    
    # return a list containing both folder_1 and folder_2 files
    return combined_folders

def createArchiveFile():
    # get the output folder path
    out_folder_path = getOutputFolderPath()

    # building the path where to save the archive file:
    # starting from the 'local' folder, add a new subfolder named 'dataset' 
    archive_folder_path = f"{getLocalFolderPath()}\\dataset"
    
    # building the actual archive file containing files from the output folder 
    shutil.make_archive(archive_folder_path, 'zip', out_folder_path)
    
    # build the actual archive file path
    archive_file_path = f"{archive_folder_path}.zip" 
    
    # return the archive file path
    return archive_file_path

def checkParams(folder, size, token, use_ai, captions):
    # check the input params
    if folder == None or size == None or token == None or use_ai == None or captions == None:
        return False

    # check if input folder list is empty
    if len(folder) == 0:
        return False

    # check if token is empty
    if token == "":
        return False

def generateDataset(folder, size, token, use_ai, captions):
    # check the input params 
    if checkParams(folder, size, token, use_ai, captions) == False:
        # return readme file
        return getReadmeFile()
    
    # guarantee that the local folder is empty
    shutil.rmtree(getLocalFolderPath())    

    # copy the uploaded folder in local system folder
    local_folder = copyFolder(folder) 
    
    # both txt-file-generation and resizing refers to this virtual folder 
    renamed_folder = renameImages(folder, token)

    # txt_folder will be one virtual folder apart
    txt_folder = imageCaptioning(renamed_folder, token, use_ai, captions)

    # resized_folder will be one virtual folder apart
    resized_folder = resizeImages(renamed_folder, size)
    
    # at the end both virtual folder are merged
    new_folder = combineFolders(resized_folder, txt_folder)
    
    # create an archive file from the new folder
    archive_file = createArchiveFile()

    # return the archive file path
    return archive_file