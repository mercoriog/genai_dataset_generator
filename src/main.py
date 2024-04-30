from gui import gui_builder as build
from script import scheduler as sched

if __name__ == "__main__":
	# Start scheduler.
	sched.start()

	# Build GUI.
	demo = build.buildGUI()

	# Start GUI.
	demo.launch(share = False)
