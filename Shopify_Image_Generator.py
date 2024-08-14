import json
import os
import shutil
from PIL import Image
from tqdm import tqdm

def place_image_on_frame(base_image_path, overlay_image_path, output_path, area_coords):
    base_image = Image.open(base_image_path)
    overlay_image = Image.open(overlay_image_path)
    
    area_width, area_height = area_coords[2], area_coords[3]
    overlay_image.thumbnail((area_width, area_height), Image.LANCZOS)
    
    x = area_coords[0] + (area_width - overlay_image.width) // 2
    y = area_coords[1] + (area_height - overlay_image.height) // 2
    
    base_image.paste(overlay_image, (x, y), overlay_image if overlay_image.mode == 'RGBA' else None)
    
    base_image.save(output_path)

def determine_orientation(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return "portrait" if height > width else "landscape"

def copy_additional_images(source_folder, destination_folder, start_number):
    for i, filename in enumerate(sorted(os.listdir(source_folder)), start=start_number):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, f"{i}_additional_product_{i - start_number + 1}.png")
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_file)

def process_mockups(config_landscape, config_portrait, source_folder, output_folder):
    with open(config_landscape, 'r') as file:
        mockups_landscape = json.load(file)
    
    with open(config_portrait, 'r') as file:
        mockups_portrait = json.load(file)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    themes = ['light', 'dark', 'lines']
    additional_images_count = 4
    total_mockup_count = 22
    lake_count = sum(1 for name in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, name)))

    with tqdm(total=(lake_count * (3 + additional_images_count + total_mockup_count * 3)), desc="Processing images") as pbar:
        for lake_folder_name in os.listdir(source_folder):
            lake_folder_path = os.path.join(source_folder, lake_folder_name)
            
            if os.path.isdir(lake_folder_path):
                lake_output_folder = os.path.join(output_folder, lake_folder_name)
                if not os.path.exists(lake_output_folder):
                    os.makedirs(lake_output_folder)
                
                first_image_path = next((os.path.join(lake_folder_path, f) for f in os.listdir(lake_folder_path) if f.endswith('.png')), None)
                if first_image_path is None:
                    continue
                
                orientation = determine_orientation(first_image_path)
                mockup_folder = os.path.join(r"C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\SHOPIFY MOCKUPS", orientation.capitalize())
                mockups = mockups_landscape if orientation == "landscape" else mockups_portrait

                # Generate the first three images (light, dark, lines) on their respective mockups
                for theme_index, theme in enumerate(themes):
                    overlay_image_filename = f"{lake_folder_name}{theme_index + 1}.png"
                    overlay_image_path = os.path.join(lake_folder_path, overlay_image_filename)
                    
                    # Mockup for the plain theme
                    base_image_path = os.path.join(mockup_folder, mockups[theme_index]["base_image_path"])
                    area_coords = tuple(mockups[theme_index]["area_coords"])
                    plain_output_filename = f"{theme_index + 1}_{theme}.png"
                    plain_output_path = os.path.join(lake_output_folder, plain_output_filename)
                    
                    if os.path.exists(base_image_path):
                        place_image_on_frame(base_image_path, overlay_image_path, plain_output_path, area_coords)
                    else:
                        print(f"Warning: Base image {base_image_path} does not exist.")
                    pbar.update(1)

                # Copy additional product images
                copy_additional_images(additional_images_folder, lake_output_folder, start_number=4)
                pbar.update(additional_images_count)

                # Generate 22 mockup images for each theme (excluding plain themes)
                image_number = 8
                for theme_index, theme in enumerate(themes):
                    for num, mockup_config in enumerate(mockups[3:], start=1):  # Skipping the first three, which are for plain images
                        overlay_image_filename = f"{lake_folder_name}{theme_index + 1}.png"
                        overlay_image_path = os.path.join(lake_folder_path, overlay_image_filename)

                        base_image_path = os.path.join(mockup_folder, mockup_config["base_image_path"])
                        area_coords = tuple(mockup_config["area_coords"])

                        output_filename = f"{image_number}_{theme}_{mockup_config['output_path_suffix'].lower().replace(' ', '_')}.png"
                        output_path = os.path.join(lake_output_folder, output_filename)
                        
                        if os.path.exists(base_image_path):
                            place_image_on_frame(base_image_path, overlay_image_path, output_path, area_coords)
                        else:
                            print(f"Warning: Base image {base_image_path} does not exist.")
                        
                        image_number += 1
                        pbar.update(1)

source_folder = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\Lake Folders with Images'
output_folder = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\Completed Shopify Mockups'
additional_images_folder = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\ADDITIONAL PRODUCT IMAGES'

process_mockups('config/shopify_config_landscape.json', 'config/shopify_config_portrait.json', source_folder, output_folder)
