from service import downloader as down
from controller import folder_controller as foldc
import os

def checkEnv():
	# Get environment folder path.
	env_folder = foldc.getEnvFolderPath()

	# Check if environment folder exists
	if os.path.exists(env_folder):
		print("[SETUP] Environment found.")
		return True
	else
	print("[SETUP] Environment not found.")
		return False

def setup():
	# Check for environment.
	env = checkEnv()

	if not env:
		# Get environment .zip file url.	
		env_url = foldc.getEnvUrl()

		# Get path where to store environment folder.
		env_folder = foldc.getEnvFolderPath()

		# Download and Unzip environment folder zipfile
		# Delete after unzipping (setting 'delete_when_unzipped'=True)
		downloaded_env = down.downloadAndUnzip(url=env_url, save_path=env_folder, delete_when_unzipped=True)

		if not downloaded_env:
			print("[SETUP] Error in load environment.")
			return
	
	print("[SETUP] Environment loaded with no errors.")
	return

if __name__ == "__main__":
	# Start setup.
	setup()
	return