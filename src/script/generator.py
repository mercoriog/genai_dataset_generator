from PIL import Image as image
import os
from datasets import Dataset, Image

TRAINING_RESOLUTION = (512, 512)
DATASET_FOLDER = os.path.abspath(".\\Desktop\\Dataset\\train")

def resizeImages(dataset):
    dataset["pixel_values"] = [image.convert("RGB").resize(TRAINING_RESOLUTION) for image in dataset["image"]]
    return dataset

def getFilesPath():
    files = os.listdir(DATASET_FOLDER)
    # filtro le immagini 
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files = [os.path.join(DATASET_FOLDER, im) for im in image_files]
    return image_files

image_files = getFilesPath()
