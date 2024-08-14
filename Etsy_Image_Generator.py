import os
import json
from PIL import Image
from tqdm import tqdm

def place_image_on_frame(base_image_path, overlay_image_path, output_path, area_coords):
    base_image = Image.open(base_image_path)
    overlay_image = Image.open(overlay_image_path)
    
    # Resize the overlay image to fit within the specified area
    area_width, area_height = area_coords[2], area_coords[3]
    overlay_image.thumbnail((area_width, area_height), Image.LANCZOS)
    
    # Calculate position to paste the overlay image centered in the area
    x = area_coords[0] + (area_width - overlay_image.width) // 2
    y = area_coords[1] + (area_height - overlay_image.height) // 2
    
    # Paste the overlay image onto the base image
    base_image.paste(overlay_image, (x, y), overlay_image if overlay_image.mode == 'RGBA' else None)
    
    # Save the image with a 10MB size cap after overlaying
    save_image_with_size_cap(base_image, output_path)

def determine_orientation(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return "portrait" if height > width else "landscape"

def save_image_with_size_cap(image, output_path, max_size=10 * 1024 * 1024):
    quality = 95
    while True:
        image.save(output_path, format='PNG', quality=quality)
        if os.path.getsize(output_path) <= max_size or quality <= 10:
            break
        quality -= 5

def generate_etsy_mockups(config_landscape, config_portrait, source_folder, output_folder):
    with open(config_landscape, 'r') as file:
        mockups_landscape = json.load(file)
    
    with open(config_portrait, 'r') as file:
        mockups_portrait = json.load(file)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    lake_count = sum(1 for name in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, name)))
    total_images = lake_count * 6  # 3 Main + 3 themes
    
    with tqdm(total=total_images, desc="Generating Etsy mockups") as pbar:
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
                mockup_folder = os.path.join(r"C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\ETSY MOCKUPS", orientation.capitalize())
                mockups = mockups_landscape if orientation == "landscape" else mockups_portrait

                themes = ['Light', 'Dark', 'Lines']

                # Generate images for Main.png with Light, Dark, and Lines themes
                main_base_image_path = os.path.join(mockup_folder, "Main.png")
                main_area_coords = next((m["area_coords"] for m in mockups if m["base_image_path"] == "Main.png"), None)

                for theme_index, theme in enumerate(themes, start=1):
                    overlay_image_filename = f"{lake_folder_name}{theme_index}.png"
                    overlay_image_path = os.path.join(lake_folder_path, overlay_image_filename)
                    
                    main_output_filename = f"{theme_index}_Main_{theme}.png"
                    main_output_path = os.path.join(lake_output_folder, main_output_filename)
                    
                    if main_area_coords:
                        place_image_on_frame(main_base_image_path, overlay_image_path, main_output_path, main_area_coords)
                    
                    pbar.update(1)

                # Generate images for Light.png, Dark.png, and Lines.png
                for theme_index, theme in enumerate(themes, start=1):
                    overlay_image_filename = f"{lake_folder_name}{theme_index}.png"
                    overlay_image_path = os.path.join(lake_folder_path, overlay_image_filename)
                    
                    base_image_path = os.path.join(mockup_folder, f"{theme}.png")
                    area_coords = next((m["area_coords"] for m in mockups if m["base_image_path"] == f"{theme}.png"), None)
                    plain_output_filename = f"{theme_index + 3}_{theme}.png"
                    plain_output_path = os.path.join(lake_output_folder, plain_output_filename)
                    
                    if area_coords:
                        place_image_on_frame(base_image_path, overlay_image_path, plain_output_path, area_coords)
                    
                    pbar.update(1)

source_folder = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\Lake Folders with Images'
output_folder = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\Completed Etsy Mockups'
landscape_config = 'config/etsy_config_landscape.json'
portrait_config = 'config/etsy_config_portrait.json'

generate_etsy_mockups(landscape_config, portrait_config, source_folder, output_folder)
