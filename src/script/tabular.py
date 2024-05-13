from repository import output
import os
import csv

def extractBasename(filename):
    path_to, basename = os.path.split(filename)
    return basename

def getCSVFilePath():
	# Get 'output' folder path.
	output_folder_path = output.getOutputFolderPath()

	# Build .csv file path.
	csv_file_path = os.path.join(output_folder_path, "datset.csv")

	return csv_file_path

def initCSVContent():
	# Create an empty list for .csv writing operation.
	csv_content = []

	# Create the columns' name row.
	columns = ["id", "name", "label"]

	# Add columns' name row to .csv content.
	csv_content.append(columns)

	# This function return a table with one row and three columns.
	return csv_content

def loadText(textfile, data):
	# Set an exception handler:
	try:
		# Get text content:
		with open(textfile, "r") as file:
			# Read content from file.
			content = file.read()
			
			# Add text content to data.
			data.append(content)

	# An error occurs:
	except Exception as e:
		# Print the exception.
		print("[ERROR] " + str(e))
        # Error in open textfile. Use empty string as 'label'
		data.append("")

	# Return updated data.
	return data

def loadName(imagefile, data):
	# Extract basename from image file path stored in <imagefile>
	basename = extractBasename(imagefile)

	# Add basename to data.
	data.append(basename)

	# Return updated data.
	return data

def loadIndex(index, data):
	# Add index to data.
	data.append(index)
	
	# Return updated data.	
	return data

def loadDataInCSV(csv_content, directory):
	# Both lists in <directory> has the same length.
	# Split lists in <directory> and store in separated variables. 
	images = directory[0]
	texts = directory[1]

	# Start a counter from zero.
	index = 0

	# Iterate for each image (for each text is the same)
	for imagefile in images:
		# Create an empty data list that represent one row of .csv file
		data = [] 
		
		# Load index from current index. 
		data = loadIndex(index, data)

		# Load image name from image file.
		data = loadName(imagefile, data)

		# Get correspondent text file.
		textfile = texts[index]

		# Load text content from text file. 
		data = loadText(textfile, data)

		# Update index.
		index += 1

		# Add the current row stored as <data> in .csv content variable.
		csv_content.append(data)

	# Return the updated content with loaded data.
	return csv_content

def createCSV(content, filepath):
	# This function write content in new .csv file.
	# Set an exception handler:
	try:
		# Open the file in write mode:
		with open(filepath, mode='w', newline='') as file:
		    # Create a csv.writer object.
		    writer = csv.writer(file)
		    
		    # Write data to the CSV file.
		    writer.writerows(content)

	# An error occurs:
	except Exception as e:
		# Print the exception.
		print("[ERROR] " + str(e))
		# Notify error.
		return False
    
    # If no error occurs return True.
	return True

def createCSVFile(directory):
	# This function takes as input a list of two separated list:
	# one list for .png files' path and one list for .txt files' path.
	# There is one text file for each image file and
	# both .png and .txt file has formatted name like "name-00xy.ext".

	# This function creates a .csv file which contains three column:
	# <id>: an enumerational number of .png file;
	# <name>: the basename string of .png file;
	# <label>: the content of correspondent .txt file.

	# This function returns the created .csv filepath.
	
	# Set an exception handler:
	try:
		# Create an itialized .csv content variable.
		csv_content = initCSVContent()

		# Load data from directory in initialized .csv content.
		csv_content = loadDataInCSV(csv_content, directory)
		
		# Get .csv file path.	
		csv_file_path = getCSVFilePath()
		
		# Create .csv file.
		csv_file = createCSV(csv_content, csv_file_path)
	
	# An error occurs:
	except Exception as e:
		# Print the exception.
		print("[ERROR] " + str(e))
		# Notify error.
		return False

	# This function returns True if no error occurs in .csv file creation.
	return csv_file