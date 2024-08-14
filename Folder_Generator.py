import os
import shutil
from tqdm import tqdm

def process_filename(filename):
    """
    Replace underscores with spaces in the filename except for the underscore
    that is the 6th-to-last character.
    """
    if len(filename) >= 6 and filename[-6] == '_':
        return filename[:-6].replace('_', ' ') + filename[-6:]
    else:
        return filename.replace('_', ' ')

def organize_lake_images(source_folder, destination_folder):
    """
    Organize images into folders based on lake names and rename files.

    Parameters:
    - source_folder (str): Path to the folder containing the images.
    - destination_folder (str): Path to the new folder where organized images will be stored.
    """
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    files = os.listdir(source_folder)

    lake_names = set()

    for file in files:
        if file.endswith('.png'):
            # Process the filename to replace underscores appropriately
            processed_name = process_filename(file[:-4])
            lake_name = processed_name[:-1]  # Remove the last character (number)
            lake_names.add(lake_name)

    # Initialize progress bar
    with tqdm(total=len(files), desc="Organizing images") as pbar:
        for lake_name in lake_names:
            lake_folder = os.path.join(destination_folder, lake_name)

            if not os.path.exists(lake_folder):
                os.makedirs(lake_folder)

            for file in files:
                # Process the filename to replace underscores appropriately
                processed_name = process_filename(file[:-4])
                new_filename = processed_name + '.png'
                if processed_name.startswith(lake_name) and file.endswith('.png'):
                    source_file = os.path.join(source_folder, file)
                    new_source_file = os.path.join(source_folder, new_filename)
                    destination_file = os.path.join(lake_folder, new_filename)
                    
                    # Rename the source file
                    if source_file != new_source_file:
                        os.rename(source_file, new_source_file)
                    
                    # Copy the renamed file to the destination folder
                    shutil.copy(new_source_file, destination_file)
                    pbar.update(1)

source_folder = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\NEW PRINTS'
destination_folder = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\Lake Folders with Images'
organize_lake_images(source_folder, destination_folder)
