from script import preprocesser as prep
from gui import gui_builder as build

def start():
	# Initialize.
	init = prep.initGUI()

	# Check if GUI is initialized:
	if not init:
		# Notify initialization failure.
		print("[ERROR] Initialization failed.")
	
	# Build GUI.
	demo = build.buildGUI()

	# Start GUI.
	demo.launch(share = False)
