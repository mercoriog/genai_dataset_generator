from PIL import Image
import requests
from transformers import BlipProcessor, BlipForConditionalGeneration

MODEL_PATH = ".\\genai_dataset_generator\\src\\aicaptioning\\large_model" 

def setup():
	# with transformers, processor and model are downloaded automatically
	processor = BlipProcessor.from_pretrained(MODEL_PATH)
	model = BlipForConditionalGeneration.from_pretrained(MODEL_PATH)
	
	# return the Blip processor and the Blip Model couple
	return processor, model


def imageCaptioningFromFile(image, processor, model): 
	# load the raw image as rgb
	raw_image = Image.open(image).convert('RGB')
	# process the image with Blip Processor
	inputs = processor(raw_image, return_tensors="pt")
	# use Blip Model to generate an encoded output
	out = model.generate(**inputs, max_new_tokens=1000)
	# decode the output to reveal the image captions 
	generated_caption = processor.decode(out[0], skip_special_tokens=True)
	# return the image captioning result
	return generated_caption

def imageCaptioningFromFolder(folder):
	try:
		# load BlipProcessor and BlipModel
		processor, model = loadBlipProcessorAndModel()
		# build a list of image captions
		image_caption_list = []
		# for each image in folder
		for image in folder:
			# generate captions from image using the provided processor and model
			image_caption = generateCaptions(image, processor, model)
			# add the generated image captions to correspondent list
			image_caption_list.append(image_caption)
	except Exception as e: 
		# print the exception
		print("[ERROR] " + str(e))
		# if something wrong build a list of empty-string, one for each file in input folder
		image_caption_list = ["" for file in folder]
	# return a list of image caption, one for each input folder's image
	return image_caption_list
	
def extractCaptionFromImage(image):
	processor, model = setup()
	generated_caption = imageCaptioningFromFile(image, processor, model)
	return generated_caption