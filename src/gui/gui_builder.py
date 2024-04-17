import gradio as gr

def compgetPresentation():
	presentation = gr.Markdown('''
		# Dataset generator.
		Upload your data directory and select the resize options.
		Generate and download the output folder containing
		the processed images. 
	''')
	return presentation

def compgetFolderUploader():
	folder_uploader = gr.File(
		file_count = "directory",
		file_types = ["image"],
		label = "Select the folder containing images to be processed",
		show_label = True,
		interactive = True
	)

# GUI Builder method:
def buildGUI():
	with gr.Blocks(title = "Dataset generator") as demo:
		presentation = compgetPresentation()
		folder_uploader = compgetFolderUploader()
		# [NEW] HORIZONTAL LAYOUT:
			# [NEW] VERTICAL LAYOUT:
			# [END] VERTICAL LAYOUT.
		# [END] HORIZONTAL LAYOUT.
		return demo