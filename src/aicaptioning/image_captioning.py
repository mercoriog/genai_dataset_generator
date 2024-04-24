import requests
from PIL import Image
from transformers import BlipProcessor, TFBlipForConditionalGeneration

def loadBlipProcessorAndModel():
	# with transformers, processor and model are downloaded automatically
	processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
	model = TFBlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
	# return the Blip processor and the Blip Model
	return processor, model
	
def generateCaptions(image, processor, model): 
	# load the raw image as rgb
	raw_image = Image.open(image).convert('RGB')
	# process the image with Blip Processor
	inputs = processor(raw_image, return_tensors="pt")
	# use Blip Model to generate an encoded output
	out = model.generate(inputs)
	# decode the output to reveal the image captions 
	generated_caption = processor.decode(out[0], skip_special_tokens=True)
	# return the image captioning result
	return generated_caption

def imageCaptioningFromFile(file):
	try:
		# load BlipProcessor and BlipModel
		processor, model = loadBlipProcessorAndModel()
		# generate captions from image using the provided processor and model
		image_caption = generateCaptions(file, processor, model)
	except Exception as e: 
		# print the exception
		print("[ERROR] " + str(e))
		# if something wrong in image processing, don't provide a caption
		image_caption = ""
	# return the generated image caption
	return image_caption

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