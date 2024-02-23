import os
from PIL import Image

def crop_transparent_space(image_path, save_path):
    """
    Crop the transparent space from a PNG image and save the cropped image.
    """
    with Image.open(image_path) as img:
        # Convert to RGBA if not already
        img = img.convert("RGBA")
        
        # Get the bounding box
        bbox = img.getbbox()
        if bbox:
            # Crop the image
            cropped_img = img.crop(bbox)
            cropped_img.save(save_path)
            print(f"Cropped and saved: {save_path}")
        else:
            print(f"No need to crop: {image_path}")

def crop_images_in_folder(folder_path='.'):
    """
    Crop the transparent space from all PNG images in the specified folder.
    """
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            file_path = os.path.join(folder_path, filename)
            save_path = os.path.join(folder_path, f"cropped_{filename}")
            crop_transparent_space(file_path, save_path)

if __name__ == "__main__":
    # Adjust the folder path as needed
    folder_path = '.'  # Current directory
    crop_images_in_folder(folder_path)