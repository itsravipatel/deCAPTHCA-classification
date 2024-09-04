import os
import numpy as np
from PIL import Image, ImageOps

def create_dataset_PIL(img_folder):
    img_data_array = []
    class_name = []

    for file in os.listdir(img_folder):
        image_path = os.path.join(img_folder, file)
        
        # Load and preprocess the image
        preprocessed_image = load_and_preprocess_image(image_path)
        
        # Apply rotations and process each variant
        process_image_variants(preprocessed_image, file, img_data_array, class_name)

    return img_data_array, class_name

def load_and_preprocess_image(image_path):
    """
    Load the image, convert it to grayscale, and invert the colors.
    """
    # Open the image and convert it to grayscale
    image = Image.open(image_path).convert('L')
    
    # Invert the image colors
    inverted_image = ImageOps.invert(image)
    
    return inverted_image

def process_image_variants(image, filename, img_data_array, class_name):
    """
    Apply various rotations to the image, crop and resize it, and then
    add the processed images and corresponding class names to the lists.
    """
    # Define rotation angles
    rotation_angles = [0, 10, 20, 30, -10, -20, -30]
    
    for angle in rotation_angles:
        # Rotate the image by the specified angle
        rotated_image = image.rotate(angle, expand=True)
        
        # Crop and resize the image
        processed_image = crop_and_resize_image(rotated_image)
        
        # Normalize and store the image data
        normalized_image = normalize_image(processed_image)
        img_data_array.append(normalized_image)
        
        # Extract class name from the filename (remove file extension)
        class_name.append(filename[:-4])

def crop_and_resize_image(image):
    """
    Crop the image to remove black borders and resize it to a fixed size.
    """
    # Get the bounding box of the non-black region
    imageBox = image.getbbox()
    
    # Crop the image to this bounding box
    cropped_image = image.crop(imageBox)
    
    # Resize the cropped image to a fixed size of 166x150 pixels
    resized_image = cropped_image.resize((166, 150))
    
    return resized_image

def normalize_image(image):
    """
    Convert the image to a NumPy array, normalize pixel values, and return the result.
    """
    # Convert the image to a NumPy array
    image_array = np.array(image)
    
    # Convert the array to float32 and normalize pixel values to [0, 1]
    image_array = image_array.astype('float32') / 255.0
    
    return image_array
