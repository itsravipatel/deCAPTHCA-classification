import os
import cv2
import numpy as np
from PIL import Image

def create_dataset_PIL_test(img_folder):
    img_data_array = []
    class_name = []

    lab_fil = os.path.join(img_folder, "labels.txt")
    with open(lab_fil, 'r') as lab_f:
        for file_index in range(2000):
            image_path = os.path.join(img_folder, f"{file_index}.png")
            if not image_path.endswith('t'):
                image = load_and_process_image(image_path)
                label = lab_f.readline().strip().split(",")
                split_and_process_image(image, label, img_data_array, class_name)

    return img_data_array, class_name

def load_and_process_image(image_path):
    """
    Load the image and apply a series of processing steps: convert to HSV, 
    create a mask, and apply erosion.
    """
    # Load image
    image = cv2.imread(image_path)
    
    # Convert the image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Create a mask based on the HSV value of the first pixel
    hsv_lower = np.array(hsv[0, 0])
    hsv_upper = np.array(hsv[0, 0])
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
    mask = 255 - mask
    
    # Apply the mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask)
    
    # Erode the image to reduce noise
    kernel = np.ones((10, 10), np.uint8)
    erosion = cv2.erode(result, kernel, iterations=1)
    
    # Normalize the image
    erosion = erosion.astype('float32') / 255.0
    
    return erosion

def split_and_process_image(image, labels, img_data_array, class_name):
    """
    Split the image into three parts (left, middle, right), process each part,
    and append the results to img_data_array and class_name.
    """
    # Split the image into left, middle, and right sections
    l_im = image[:, :166]
    m_im = image[:, 167:333]
    r_im = image[:, 334:500]
    im_arr = [l_im, m_im, r_im]

    # Process each section
    for i in range(3):
        cropped_image = crop_and_resize_image(im_arr[i])
        img_data_array.append(cropped_image)
        class_name.append(labels[i])

def crop_and_resize_image(image):
    """
    Convert the image to grayscale, crop to remove black borders, 
    and resize to a fixed size.
    """
    # Convert the image array to a PIL image and then to grayscale
    image = Image.fromarray((image * 255).astype(np.uint8)).convert('L')
    
    # Crop the image to remove black borders
    imageBox = image.getbbox()
    cropped = image.crop(imageBox)
    
    # Resize the cropped image to a fixed size of 42x38
    resized_image = cropped.resize((42, 38))
    
    # Convert the image back to a NumPy array and return it
    return np.array(resized_image)
