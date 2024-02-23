import os
from PIL import Image

def flip_images_in_folder(folder_path='.'):
    # List all files in the directory
    for filename in os.listdir(folder_path):
        # Check if the file is an image (add or modify extensions as needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            # Open the image
            with Image.open(file_path) as img:
                # Flip the image horizontally
                flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
                # Save the flipped image, you can change the format if needed
                flipped_img.save(os.path.join(folder_path, filename))
                print(f"Flipped {filename} successfully.")

if __name__ == "__main__":
    # Run the function for the current directory
    flip_images_in_folder()