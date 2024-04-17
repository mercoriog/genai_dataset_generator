from PIL import Image as image
import os

TRAINING_RESOLUTION = (512, 512)

def resizeImages(dataset):
    dataset["pixel_values"] = [image.convert("RGB").resize(TRAINING_RESOLUTION) for image in dataset["image"]]
    return dataset

def getFilesPath(folder):
    files = os.listdir(folder)
    # filtro le immagini 
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files = [os.path.join(folder, im) for im in image_files]
    return image_files

def generateDatset():
    pass
