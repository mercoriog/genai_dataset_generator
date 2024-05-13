import gradio as gr
from script import generator as gen
from pathlib import Path

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
        label = "Set necessary token to perform dataset generation",
        placeholder = "Use a keyword.",
        show_copy_button = True,
        interactive = True
    )
    return token_textbox

def compgetLabelCheckBox():
	label_checkbox = gr.Checkbox(
		value = True,
		label = "Enable Labelling",
		info = "Turn on to generate a text file for each dataset image with token label. Check 'Image Captioning' section for more.\nTurn off to deactivate.",
		show_label = True,
		interactive = True
	)
	return label_checkbox

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

def compgetLabellingLabel():
	labelling_label = gr.Label(
		value = "Set this options only if 'Labelling' is enable.",
		label = "*** READ BEFORE CONTINUING ***",
		show_label = True,
		color = 'red'
	)
	return labelling_label

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
		label = "Use AI for feature extraction",
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

def compgetDatasetFile():
	datasetFile = gr.File(
		label = "Generated dataset",
		show_label = True,
		interactive = False,
	)
	return datasetFile

def compgetDownloadButton():
	download_button = gr.DownloadButton(
		label = "Download file",
		variant = "secondary",
		size = "lg", # or 'sm' or None
		interactive = True,
	)
	return download_button

# generator request function:
def genRequest(folder, height, width, token, label, use_ai, every_caption):
	# calling the generateDataset function that bring 
	# a <folder> param [type: list] containing a list of file path;
	# a <size> param [type: couple] to resize files;
	# a <token> param [type: string] for renaming the 'folder' files;
	# a <label> param [type: bool] to enable/disable text file generation for labelling;
	# a <use_ai> param [type: bool] to enable/disable ai caption generation;
	# a <every_caption> param [type: string] to insert the caption in each generated text file.
	# It returns an archive file path.
	generated_file = gen.generateDataset(folder, (width, height), token, label, use_ai, every_caption)

	# Change generated file output name
	output_file = Path(generated_file).name
	
	# Return two times to fill File component and Download button component.
	return generated_file, output_file

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

		# [NEW] GROUP LAYOUT:
		with gr.Group():
			label_checkbox = compgetLabelCheckBox()

			# [NEW] DYNAMIC SECTION:
			with gr.Accordion(label = "Image Captioning.", open = False):
				labelling_label = compgetLabellingLabel()
				
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
		# [END] GROUP LAYOUT.

		generate_button = compgetGenerateButton()
		datasetFile = compgetDatasetFile()
		download_button = compgetDownloadButton()

		# Define event listener for generation.
		generate_button.click(
			fn = genRequest,
			inputs = [
				folder_uploader, 
				height_input, 
				width_input, 
				token_textbox,
				label_checkbox,
				aiCaptioning_checkbox,
				customCaption_textbox
			],
			outputs = [datasetFile, download_button],
			scroll_to_output = True,
			show_progress = 'full'
		)

		return demo