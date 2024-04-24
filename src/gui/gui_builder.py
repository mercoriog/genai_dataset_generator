import gradio as gr
import shutil
from .script import generator as gen

def compgetPresentation():
	presentation = gr.Markdown('''
		# Dataset generator
		Upload your data directory and select the resize options.\n
		Generate and download the output folder containing
		the processed images. 
	''')
	return presentation

def compgetFolderUploader():
	folder_uploader = gr.File(
		file_count = "directory",
		label = "Select the folder containing images to be processed",
		show_label = True,
		interactive = True
	)
	return folder_uploader

def compgetTokenTextBox():
    token_textbox = gr.Textbox(
        lines = 1,
        label = "Token",
        placeholder = "Type the token associate to the dataset's content. Use a keyword.",
        show_copy_button = True,
        interactive = True
    )
    return token_textbox

def compgetHeightInput():
    height_input = gr.Number(
        value = 0,
        label = "Height",
        info = "Select height in pixels for resize",
        show_label = True,
        interactive = True,
        precision = 0,
        minimum = 0,
        maximum = 1024
    )
    return height_input

def compgetWidthInput():
    width_input = gr.Number(
        value = 0,
        label = "Width",
        info = "Select width in pixels for resize",
        show_label = True,
        interactive = True,
        precision = 0,
        minimum = 0,
        maximum = 1024
    )
    return width_input

def compgetCustomImageCaption():
	customCaption_textbox = gr.Textbox(
		lines = 2,
        label = "Caption for every image",
        placeholder = "Type the caption to set to every image. Leave blank to not use.",
        show_copy_button = True,
        interactive = True
	)
	return customCaption_textbox

def compgetAICaptioning():
	aiCaptioning_checkbox = gr.Checkbox(
		value = False,
		label = "Use AI for Image Captioning",
		info = "Activate to use AI Model to automate image captioning.",
		show_label = True,
		interactive = True
	)
	return aiCaptioning_checkbox

def compgetGenerateButton():
    generate_button = gr.Button(
        value = "Generate dataset",
        variant = "primary"
    )
    return generate_button

def compgetDownloadButton():
	download_button = gr.DownloadButton(
		label = "Download dataset folder",
		variant = "secondary",
		size = "lg", # or 'sm' or None
		interactive = True,
	)
	return download_button

# generator request function:
def genRequest(folder, height, width, token, use_ai, captions):
	# calling the generateDataset function that bring a list of file path as 'folder' param [type: list], /
	# a 'size' param [type: couple] to resize files,
	# a 'token' param [type: string] for renaming the 'folder' files.
	# It returns an archive file path
	return gen.generateDataset(folder, (width, height), token, use_ai, captions)

# GUI Builder method:
def buildGUI():
	with gr.Blocks(title = "Dataset generator") as demo:
		presentation = compgetPresentation()
		folder_uploader = compgetFolderUploader()

		# [NEW] DYNAMIC SECTION:
		with gr.Accordion(label = "Resize images", open = False):
			# [NEW] HORIZONTAL LAYOUT:
			with gr.Row():
				width_input = compgetWidthInput()
				height_input = compgetHeightInput()
			# [END] HORIZONTAL LAYOUT.		
		# [END] DYNAMIC SECTION.

		token_textbox = compgetTokenTextBox()

		# [NEW] DYNAMIC SECTION:
		with gr.Accordion(label = "Image Captioning", open = False):
			# [NEW] HORIZONTAL LAYOUT:
			with gr.Row():
				# [NEW] VERTICAL LAYOUT:
				with gr.Column(scale = 1):
					aiCaptioning_checkbox = compgetAICaptioning()
				# [END] VERTICAL LAYOUT

				# [NEW] VERTICAL LAYOUT:
				with gr.Column(scale = 2):
					customCaption_textbox = compgetCustomImageCaption()
				# [END] VERTICAL LAYOUT.
			# [END] HORIZONTAL LAYOUT.
		# [END] DYNAMIC SECTION.		
		
		generate_button = compgetGenerateButton()
		download_button = compgetDownloadButton()

		# define event listener
		generate_button.click(
			fn = genRequest,
			inputs = [
				folder_uploader, 
				height_input, 
				width_input, 
				token_textbox,
				aiCaptioning_checkbox,
				customCaption_textbox
			],
			outputs = [download_button],
			scroll_to_output = True,
			show_progress = 'full'
		)

		return demo