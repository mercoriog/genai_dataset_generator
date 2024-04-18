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
def genRequest(folder, height, width, token):
	archive_data = gen.generateDataset(folder, (width, height), token)
	data_path = gen.getOutputDataPath()
	archive_path = f"{gen.getLocalDataPath()}\\dataset"
	shutil.make_archive(archive_path, 'zip', data_path)
	return f"{archive_path}.zip"

# GUI Builder method:
def buildGUI():
	with gr.Blocks(title = "Dataset generator") as demo:
		presentation = compgetPresentation()
		folder_uploader = compgetFolderUploader()
		
		# [NEW] HORIZONTAL LAYOUT:
		with gr.Row():
			width_input = compgetWidthInput()
			height_input = compgetHeightInput()
			token_textbox = compgetTokenTextBox()
		# [END] HORIZONTAL LAYOUT.		
		
		generate_button = compgetGenerateButton()
		download_button = compgetDownloadButton()

		# define event listener
		generate_button.click(
			fn = genRequest,
			inputs = [
				folder_uploader, 
				height_input, 
				width_input, 
				token_textbox
			],
			outputs = [download_button],
			scroll_to_output = True,
			show_progress = 'full'
		)

		return demo