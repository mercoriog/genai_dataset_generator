from PIL import Image
from pathlib import Path
import os
import cv2
import shutil
import numpy as np

def getLocalDataPath():
    # local folder path
    return f"{os.getcwd()}\\genai_dataset_generator\\local"

def getUserDataPath():
    # user folder path from local folder
    return f"{getLocalDataPath()}\\user" 

def getOutputDataPath():
    # output data folder from local folder
    return f"{getLocalDataPath()}\\out"

def extractBasename(filename):
    path_to, basename = os.path.split(filename)
    return basename

def extractNameNoExt(filename):
    return Path(filename).stem

def getLocalFilename(filename):
    user_folder = getUserDataPath()
    basename = extractBasename(filename)
    return f"{user_folder}\\{basename}"

def copyFolder(folder):
    local_folder = []
    for file in folder:
        local_filename = getLocalFilename(file)
        # load image as array
        img = cv2.imread(file)
        # save current file's local copy
        cv2.imwrite(local_filename, img)
        # add to local folder list
        local_folder.append(local_filename)
    return local_folder

def findPadding(dim):
    if dim < 100:
        return 3
    elif dim < 1000:
        return 4
    elif dim < 10000:
        return 5
    else: return 6

def getPaddedString(padding, num):
    fill = padding - len(str(num))
    return f"{'0' * fill}{str(num)}"

def renameImages(folder, token):
    renamed_folder = []
    padding = findPadding(len(folder))
    count = 0
    for file in folder:
        count += 1
        padded_str = getPaddedString(padding, count)
        data_path = getOutputDataPath()
        new_filename = f"{data_path}\\{token}-{padded_str}.png"
        os.rename(file, new_filename)
        renamed_folder.append(new_filename)
    return renamed_folder

def extractCaptions(file):
    # TODO:
    return "jacket, Giorgio Armani"

def createTxtFile(filename, token, captions):
    # data folder from disk folder path
    data_path = getOutputDataPath()
    txt_file_path = f"{data_path}\\{filename}.txt"
    
    # create new .txt file
    txt_file = open(txt_file_path, "w")
    txt_file.write(f'{token}, {captions}')
    txt_file.close()

    return txt_file_path

def imageCaptioning(folder, token):
    txt_folder = []
    for file in folder:
        filename = extractNameNoExt(file)
        captions = extractCaptions(file)
        txt_file_path = createTxtFile(filename, token, captions)
        txt_folder.append(txt_file_path)
    return txt_folder

def resizeImages(folder, size):
    resized_folder = []
    for file in folder:
        # load image as array
        img = cv2.imread(file)
        # do resize operation
        img = cv2.resize(img, size)
        # save resized image
        cv2.imwrite(file, img)
        resized_folder.append(file)
    return resized_folder

def combineFolders(folder_1, folder_2):
    combined_folder = [f1 for f1 in folder_1]
    for f2 in folder_2:
        combined_folder.append(f2)
    return combined_folder

def generateDataset(folder, size, token):
    # copy the uploaded folder in local system folder
    # local_folder = copyFolder(folder) 
    
    # both txt-file-generation and resizing refers to this virtual folder 
    renamed_folder = renameImages(folder, token)

    # txt_folder will be one virtual folder apart
    txt_folder = imageCaptioning(renamed_folder, token)

    # resized_folder will be one virtual folder apart
    resized_folder = resizeImages(renamed_folder, size)
    
    # at the end both virtual folder are merged
    new_folder = combineFolders(resized_folder, txt_folder)
    return new_folder