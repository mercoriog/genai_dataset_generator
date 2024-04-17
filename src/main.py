from gui import gui_builder as build

if __name__ == "__main__":
    # controlla i try catch statement
	demo = build.buildGUI()
	demo.launch(share = False)
