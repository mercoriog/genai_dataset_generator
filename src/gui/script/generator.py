from PIL import Image
from pathlib import Path
import os
import cv2
import shutil
import numpy as np

def getLocalFolderPath():
    # local folder path
    return f"{os.getcwd()}\\genai_dataset_generator\\local"

def getUserFolderPath():
    # user folder path from local folder
    return f"{getLocalFolderPath()}\\user" 

def getOutputFolderPath():
    # output data folder from local folder
    return f"{getLocalFolderPath()}\\out"

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
        out_folder_path = getOutputFolderPath()
        new_filename = f"{out_folder_path}\\{token}-{padded_str}.png"
        os.rename(file, new_filename)
        renamed_folder.append(new_filename)
    return renamed_folder

def extractCaptions(file):
    # TODO:
    return "jacket, Giorgio Armani"

def createTxtFile(filename, token, captions):
    # output folder from disk folder path
    out_folder_path = getOutputFolderPath()
    txt_file_path = f"{out_folder_path}\\{filename}.txt"
    
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
    # build a resized folder list to access every resized file path
    resized_folder = []

    # for each file in the input folder 
    for file in folder:
        # load image as array
        img = cv2.imread(file)
        
        # resize the image
        img = cv2.resize(img, size)
        
        # save resized image
        cv2.imwrite(file, img)

        # add the file path in resized folder list
        resized_folder_list.append(file)
    
    # return a list of resized files' path
    return resized_folder_list    

def createArchiveFile():
    # get the output folder path
    out_folder_path = gen.getOutputFolderPath()

    # building the path where to save the archive file:
    # starting from the 'local' folder, add a new subfolder named 'dataset' 
    archive_folder_path = f"{gen.getLocalFolderPath()}\\dataset"
    
    # building the actual archive file containing files from the output folder 
    shutil.make_archive(archive_folder_path, 'zip', out_folder_path)
    
    # build the actual archive file path
    archive_file_path = f"{archive_path}.zip" 
    
    # return the archive file path
    return archive_file_path

def generateDataset(folder, size, token):
    # guarantee that the local folder is empty
    shutil.rmtree(getLocalFolderPath())

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
    
    # create an archive file from the new folder
    archive_file = createArchiveFile()

    # return the archive file path
    return archive_file