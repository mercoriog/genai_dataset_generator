import cv2

def resizeImages(folder, size):
    # This function gets as input parameters:
    # - folder: a list of images' path;
    # - size: a couple made 'height' and 'width' values.
    
    # This function returns a list of resized images' path.
    
    # Build a resized folder list.
    resized_folder_list = []

    # For each file in the input folder: 
    for file in folder:
        # Load image as array.
        image = cv2.imread(file)
        
        # If size is (0,0) don't resize.
        if size != (0,0):
            # Resize the image.
            image = cv2.resize(image, size)

        # Save the resized image with same original name.
        cv2.imwrite(file, image)

        # Add the file path in resizedfolder list.
        resized_folder_list.append(file)
    
    # Return a list of resized files' path.
    return resized_folder_list