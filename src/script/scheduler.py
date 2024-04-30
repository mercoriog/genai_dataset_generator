from script import preprocesser as prep

def start():
	# Initialize.
	init = prep.initGUI()

	# Check if GUI is initialized:
	if not init:
		print("[ERROR] Initialization failed.")