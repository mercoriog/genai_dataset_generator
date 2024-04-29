import cv2

def resizeImages(folder, size):
    # build a resized folder list to access every resized file path
    resized_folder_list = []

    # for each file in the input folder 
    for file in folder:
        # load image as array
        img = cv2.imread(file)
        
        # if size is (0,0) don't resize
        if size != (0,0):
            # resize the image
            img = cv2.resize(img, size)

        # save resized image
        cv2.imwrite(file, img)

        # add the file path in resized folder list
        resized_folder_list.append(file)
    
    # return a list of resized files' path
    return resized_folder_list