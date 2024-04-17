from PIL import Image
import os
import numpy as np

def renameImages(folder, token):
    return folder

def imageCaptioning(folder, token):
    return folder

def resizeImages(folder, size):
    folder = [np.array(Image(f)) for f in folder]
    #folder = [im.convert("RGB").resize(size) for im in folder]
    return folder

def generateDataset(folder, size, token):
    folder = renameImages(folder, token)
    folder = imageCaptioning(folder, token)
    folder = resizeImages(folder, size)
    return folder