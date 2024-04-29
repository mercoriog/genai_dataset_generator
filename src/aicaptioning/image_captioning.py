from PIL import Image
import requests
from transformers import BlipProcessor, BlipForConditionalGeneration

MODEL_PATH = ".\\genai_dataset_generator\\src\\aicaptioning\\large_model" 

def setup():
	# This function load the pretrained Blip model and it's processor from MODEL_PATH.
	processor = BlipProcessor.from_pretrained(MODEL_PATH)
	model = BlipForConditionalGeneration.from_pretrained(MODEL_PATH)
	
	# return the BlipModel and BlipProcessor.
	return model, processor

def imageCaptioningFromFile(image, model, processor): 
	# This function gets as input parameters an image-to-text <model> 
	# and its <processor> to preprocess image before passing it to model. 
	
	# Load the raw image with RGB color scale.
	raw_image = Image.open(image).convert('RGB')
	
	# Process the image with processor.
	inputs = processor(raw_image, return_tensors="pt")
	
	# Use model to generate an encoded text output, setting a maximum output dimension.
	encoded_caption = model.generate(**inputs, max_new_tokens=1000)

	# Decode the output to get readable image caption. 
	decoded_caption = processor.decode(encoded_caption[0], skip_special_tokens=True)
	
	# Return the AI generated caption of the input image.
	return decoded_caption

def extractCaptionFromImage(image):
	# Load BlipModel and BlipProcessor.
	model, processor = setup()
	
	# Generate caption using BlipModel.
	generated_caption = imageCaptioningFromFile(image, model, processor)
	
	# Return input image's generated caption using BlipModel.
	return generated_caption