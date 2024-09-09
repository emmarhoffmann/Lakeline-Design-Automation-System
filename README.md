# Lakeline Design Automation System

## About
The Lakeline Design Automation System is a comprehensive toolset developed to automate product management and image processing for **Lakeline Design**, a creative business founded by Emma Hoffmann that specializes in lake-inspired artwork. This project, collaboratively created by Emma Hoffmann and Blake Norman, streamlines the process of preparing and managing products across Etsy and Shopify.

## Features
- **Automated Folder Creation**: Automatically organizes lake print designs into structured folders.
- **Image Mockup Generation**: Generates mockup images for Etsy and Shopify products, customized for different platforms and product variations.
- **Product Creation Automation**: Simplifies creating and customizing products on Shopify, including image uploads and variant management.
- **Script Management**: Ensures smooth execution of scripts, handling processes efficiently and checking for errors.

## Project Structure
- `Folder_Generator.py`: Organizes lake print designs into structured folders, setting up the necessary directory structure for further processing.
- `Etsy_Image_Generator.py`: Generates mockup images for Etsy products, overlaying lake print designs onto various mockup backgrounds.
- `Shopify_Image_Generator.py`: Generates mockup images for Shopify products, overlaying lake print designs onto various mockup backgrounds customized for different print design and frame product variations.
- `Shopify_Product_Generator.py`: Automates the creation of new products on Shopify, including duplicating a base product, customizing product details, and uploading images with alt texts for connecting images to product variants.
- `Script_Manager.py`: Manages the execution of individual or all scripts for standard usage, ensuring a smooth and error-checked workflow.
- `etsy_config_portrait.json`, `etsy_config_landscape.json`, `shopify_config_portrait.json`, `shopify_config_landscape.json`: Configuration files for prints, including the base and output paths as well as coordinates for the placement of prints over the base images.
- `completed_lakes.txt`: List of completed lakes for new lake product checking.

## Benefits
This system significantly reduces manual work by automating the process, ensuring consistent and high-quality output for Lakeline Design products across Etsy and Shopify platforms.

## Created By
- **Emma Hoffmann** (GitHub: [emmarhoffmann](https://github.com/emmarhoffmann))
- **Blake Norman** (GitHub: [blakenorman12](https://github.com/blakenorman12))
