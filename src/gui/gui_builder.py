import gradio as gr
from script import generator as gen

def compgetPresentation():
	presentation = gr.Markdown('''
		# Dataset generator.
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

# GUI Builder method:
def buildGUI():
	with gr.Blocks(title = "Dataset generator") as demo:
		presentation = compgetPresentation()
		folder_uploader = compgetFolderUploader()
		generate_button = compgetGenerateButton()
		# define event listener
		generate_button.click(
			fn = gen.generateDataset,
			inputs = [listcomponents], #TODO:
			outputs = [download_button],
			scroll_to_output = True,
			show_progress = 'full'
		)

		download_button = compgetDownloadButton()
		# [NEW] HORIZONTAL LAYOUT:
			# [NEW] VERTICAL LAYOUT:
			# [END] VERTICAL LAYOUT.
		# [END] HORIZONTAL LAYOUT.
		return demo