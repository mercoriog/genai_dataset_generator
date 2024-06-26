from aicaptioning import image_captioning as aicapt
from repository import output
from pathlib import Path
import os

def extractNameNoExt(filename):
    # This function extract the exact name of the file (without extension).
    return Path(filename).stem

def createTxtFile(filename, token, ai_generated_caption, every_caption):
    # This function creates a text file named as input <filename>,
    # which contains <token> string as first part,
    # <ai_generated_caption> string as second part and
    # <every_caption> string as final part of text written.
    
    # This function returns the generated text file's path.
    
    # Get 'output' folder's path.
    out_folder_path = output.getOutputFolderPath()
    
    # Build file.txt basename.
    txt_file_basename = f"{filename}.txt"

    # Build the .txt file path combining 'output' folder path with filename and .txt extension.
    txt_file_path = os.path.join(out_folder_path, txt_file_basename)
    
    # Create new .txt file.
    txt_file = open(txt_file_path, "w")

    # Write the <token> string.
    txt_file.write(f"{token}")
    
    # Check <ai_generated_caption> length:
    if len(ai_generated_caption) > 0:
    # Write <ai_generated_caption> string.
        txt_file.write(f", {ai_generated_caption}")
    
    # Check <every_caption> length:
    if len(every_caption) > 0:
        # Write <every_caption> string. 
        txt_file.write(f", {every_caption}")
    
    # Close the generated text file.
    txt_file.close()

    # Return the generated text file's path wich contains provided captions.
    return txt_file_path

def imageCaptioning(folder, token, use_ai, every_caption):
    # This function gets as parameters:
    # - folder: a list of images' path;
    # - token: a string formatted as keyword used for renaming and captioning operations;
    # - use_ai: a boolean value that define if the use of AI is allowed or not;
    # - every_captions: a string that will be written in each captioning text file produced by captioning operation.

    # This function create a text file for each image in input <folder> which contains the correspondent caption.
    # This function returns a list of generated text files' path.

    # Build a list to store generated text files' path.
    txt_folder = []
    
    # Initialize an empty AI generated caption string.
    ai_generated_caption = ""
    
    # If AI model usage is is enabled, then it is required to load the AI model before use it:
    if use_ai == True:
        # Get the setup objects for AI model usage.
        model, processor = aicapt.setup()    

    # For each image path in folder:
    for image in folder:
        # Extract the absolute filename (no path, no extension) from the current image.
        filename = extractNameNoExt(image)

        # Check if AI model usage is enabled:
        if use_ai == True:
            # Generate caption for the current image with AI model.
            ai_generated_caption = aicapt.extractCaptionFromImage(image, model, processor)
        
        # Generate the text file associated to current image. 
        txt_file_path = createTxtFile(filename, token, ai_generated_caption, every_caption)

        # Add the generated text file's path to <text_folder> list. 
        txt_folder.append(txt_file_path)

    # Return a list of text files' path containing captions for each input folder's image.
    return txt_folder