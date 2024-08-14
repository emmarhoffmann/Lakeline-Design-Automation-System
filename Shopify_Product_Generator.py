import os
import requests
import base64
import json
from dotenv import load_dotenv

load_dotenv()

# Shopify API credentials
api_key = os.getenv('SHOPIFY_API_KEY')
shop_name = 'lakeline-design.myshopify.com'
api_version = '2024-07'

# Headers for the API request
headers = {
    'Content-Type': 'application/json',
    'X-Shopify-Access-Token': api_key
}

# Define base path to lake folders
base_path = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\Completed Shopify Mockups'

# Define the image order and alt text mappings
image_order = [
    "1_light.png", "2_dark.png", "3_lines.png",
    "4_additional_product_1.png", "5_additional_product_2.png", "6_additional_product_3.png", "7_additional_product_4.png",
    "8_light_black_thin_frame.png", "9_light_silver_thin_frame.png", "10_light_gold_thin_frame.png",
    "11_light_wood_thin_frame.png", "12_light_white_thin_frame.png",
    "13_light_black_flat_frame.png", "14_light_grey_flat_frame.png", "15_light_silver_flat_frame.png",
    "16_light_champagne_flat_frame.png", "17_light_wood_flat_frame.png", "18_light_white_flat_frame.png",
    "19_light_black_box_frame.png", "20_light_wood_box_frame.png", "21_light_white_box_frame.png",
    "22_light_unframed_print.png", "23_light_black_floating_frame.png", "24_light_truffle_floating_frame.png",
    "25_light_champagne_floating_frame.png", "26_light_silver_floating_frame.png", "27_light_wood_floating_frame.png",
    "28_light_white_floating_frame.png", "29_light_unframed_canvas.png",
    "30_dark_black_thin_frame.png", "31_dark_silver_thin_frame.png", "32_dark_gold_thin_frame.png",
    "33_dark_wood_thin_frame.png", "34_dark_white_thin_frame.png",
    "35_dark_black_flat_frame.png", "36_dark_grey_flat_frame.png", "37_dark_silver_flat_frame.png",
    "38_dark_champagne_flat_frame.png", "39_dark_wood_flat_frame.png", "40_dark_white_flat_frame.png",
    "41_dark_black_box_frame.png", "42_dark_wood_box_frame.png", "43_dark_white_box_frame.png",
    "44_dark_unframed_print.png", "45_dark_black_floating_frame.png", "46_dark_truffle_floating_frame.png",
    "47_dark_champagne_floating_frame.png", "48_dark_silver_floating_frame.png", "49_dark_wood_floating_frame.png",
    "50_dark_white_floating_frame.png", "51_dark_unframed_canvas.png",
    "52_lines_black_thin_frame.png", "53_lines_silver_thin_frame.png", "54_lines_gold_thin_frame.png",
    "55_lines_wood_thin_frame.png", "56_lines_white_thin_frame.png",
    "57_lines_black_flat_frame.png", "58_lines_grey_flat_frame.png", "59_lines_silver_flat_frame.png",
    "60_lines_champagne_flat_frame.png", "61_lines_wood_flat_frame.png", "62_lines_white_flat_frame.png",
    "63_lines_black_box_frame.png", "64_lines_wood_box_frame.png", "65_lines_white_box_frame.png",
    "66_lines_unframed_print.png", "67_lines_black_floating_frame.png", "68_lines_truffle_floating_frame.png",
    "69_lines_champagne_floating_frame.png", "70_lines_silver_floating_frame.png", "71_lines_wood_floating_frame.png",
    "72_lines_white_floating_frame.png", "73_lines_unframed_canvas.png"
]

alt_text_mapping = {
    "1_light.png": "Light Blues",
    "2_dark.png": "Dark Blues",
    "3_lines.png": "Lines",
    "4_additional_product_1.png": "Additional Image 1",
    "5_additional_product_2.png": "Additional Image 2",
    "6_additional_product_3.png": "Additional Image 3",
    "7_additional_product_4.png": "Additional Image 4",
    "8_light_black_thin_frame.png": "Black Thin Frame",
    "9_light_silver_thin_frame.png": "Silver Thin Frame",
    "10_light_gold_thin_frame.png": "Gold Thin Frame",
    "11_light_wood_thin_frame.png": "Wood Thin Frame",
    "12_light_white_thin_frame.png": "White Thin Frame",
    "13_light_black_flat_frame.png": "Black Flat Frame",
    "14_light_grey_flat_frame.png": "Grey Flat Frame",
    "15_light_silver_flat_frame.png": "Silver Flat Frame",
    "16_light_champagne_flat_frame.png": "Champagne Flat Frame",
    "17_light_wood_flat_frame.png": "Wood Flat Frame",
    "18_light_white_flat_frame.png": "White Flat Frame",
    "19_light_black_box_frame.png": "Black Box Frame",
    "20_light_wood_box_frame.png": "Wood Box Frame",
    "21_light_white_box_frame.png": "White Box Frame",
    "22_light_unframed_print.png": "Unframed Print",
    "23_light_black_floating_frame.png": "Black Floating Frame",
    "24_light_truffle_floating_frame.png": "Truffle Floating Frame",
    "25_light_champagne_floating_frame.png": "Champagne Floating Frame",
    "26_light_silver_floating_frame.png": "Silver Floating Frame",
    "27_light_wood_floating_frame.png": "Wood Floating Frame",
    "28_light_white_floating_frame.png": "White Floating Frame",
    "29_light_unframed_canvas.png": "Unframed Canvas",
    "30_dark_black_thin_frame.png": "Black Thin Frame ",
    "31_dark_silver_thin_frame.png": "Silver Thin Frame ",
    "32_dark_gold_thin_frame.png": "Gold Thin Frame ",
    "33_dark_wood_thin_frame.png": "Wood Thin Frame ",
    "34_dark_white_thin_frame.png": "White Thin Frame ",
    "35_dark_black_flat_frame.png": "Black Flat Frame ",
    "36_dark_grey_flat_frame.png": "Grey Flat Frame ",
    "37_dark_silver_flat_frame.png": "Silver Flat Frame ",
    "38_dark_champagne_flat_frame.png": "Champagne Flat Frame ",
    "39_dark_wood_flat_frame.png": "Wood Flat Frame ",
    "40_dark_white_flat_frame.png": "White Flat Frame ",
    "41_dark_black_box_frame.png": "Black Box Frame ",
    "42_dark_wood_box_frame.png": "Wood Box Frame ",
    "43_dark_white_box_frame.png": "White Box Frame ",
    "44_dark_unframed_print.png": "Unframed Print ",
    "45_dark_black_floating_frame.png": "Black Floating Frame ",
    "46_dark_truffle_floating_frame.png": "Truffle Floating Frame ",
    "47_dark_champagne_floating_frame.png": "Champagne Floating Frame ",
    "48_dark_silver_floating_frame.png": "Silver Floating Frame ",
    "49_dark_wood_floating_frame.png": "Wood Floating Frame ",
    "50_dark_white_floating_frame.png": "White Floating Frame ",
    "51_dark_unframed_canvas.png": "Unframed Canvas ",
    "52_lines_black_thin_frame.png": "Black Thin Frame  ",
    "53_lines_silver_thin_frame.png": "Silver Thin Frame  ",
    "54_lines_gold_thin_frame.png": "Gold Thin Frame  ",
    "55_lines_wood_thin_frame.png": "Wood Thin Frame  ",
    "56_lines_white_thin_frame.png": "White Thin Frame  ",
    "57_lines_black_flat_frame.png": "Black Flat Frame  ",
    "58_lines_grey_flat_frame.png": "Grey Flat Frame  ",
    "59_lines_silver_flat_frame.png": "Silver Flat Frame  ",
    "60_lines_champagne_flat_frame.png": "Champagne Flat Frame  ",
    "61_lines_wood_flat_frame.png": "Wood Flat Frame  ",
    "62_lines_white_flat_frame.png": "White Flat Frame  ",
    "63_lines_black_box_frame.png": "Black Box Frame  ",
    "64_lines_wood_box_frame.png": "Wood Box Frame  ",
    "65_lines_white_box_frame.png": "White Box Frame  ",
    "66_lines_unframed_print.png": "Unframed Print  ",
    "67_lines_black_floating_frame.png": "Black Floating Frame  ",
    "68_lines_truffle_floating_frame.png": "Truffle Floating Frame  ",
    "69_lines_champagne_floating_frame.png": "Champagne Floating Frame  ",
    "70_lines_silver_floating_frame.png": "Silver Floating Frame  ",
    "71_lines_wood_floating_frame.png": "Wood Floating Frame  ",
    "72_lines_white_floating_frame.png": "White Floating Frame  ",
    "73_lines_unframed_canvas.png": "Unframed Canvas  "
}

# Dictionary mapping state abbreviations to full names
state_abbreviations = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming"
}

# Reverse dictionary to map state names to their abbreviations
state_names = {v: k for k, v in state_abbreviations.items()}

# Function to extract state tags from the title
def add_state_tags(title):
    tags = []  # Initialize the tags list
    parts = title.split(", ")
    state_info = parts[1] if len(parts) > 1 else None

    if state_info:
        state_info_upper = state_info.upper().strip()
        found_states = []

        #print(f"Processing state info: {state_info_upper}")  # Debug print

        # Check if the state_info contains any full state names
        for state_name in state_names:
            if state_name.upper() in state_info_upper:
                found_states.append(state_name)
                state_info_upper = state_info_upper.replace(state_name.upper(), '')
                #print(f"Found full state name: {state_name}")  # Debug print

        # Split remaining state info using underscores and spaces
        abbr_list = [abbr.strip() for abbr in state_info_upper.split('_') if abbr.strip()]
        abbr_list = [abbr for part in abbr_list for abbr in part.split()]

        # Check for state abbreviations
        for abbr in abbr_list:
            if abbr in state_abbreviations:
                found_states.append(state_abbreviations[abbr])
                #print(f"Found state abbreviation: {abbr}")  # Debug print

        # Remove duplicates and add found states to tags
        tags.extend(list(set(found_states)))

        # Debug prints for troubleshooting
        #print(f"Found states: {found_states}")
        #print(f"Tags generated: {tags}")

        # If no valid states were found, provide a default message
        if not tags:
            tags.append("No State")
    else:
        tags.append("No State")

    return tags

# Function to get product details
def get_product(product_id):
    url = f"https://{shop_name}/admin/api/{api_version}/products/{product_id}.json"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request exception: {e}")
        return None

# Function to create a new product with a modified title
def create_new_product(base_product_data, new_title, tags):
    new_product_data = base_product_data.copy()
    new_product_data['title'] = new_title
    new_product_data['handle'] = new_title.lower().replace(' ', ' ')  # Keep spaces as spaces
    new_product_data['product_type'] = "Photo Prints & Canvases"
    new_product_data['tags'] = tags
    new_product_data['status'] = "active"  # Ensure the product is active
    new_product_data['published_scope'] = "global"  # Publish to all sales channels
    new_product_data['published'] = True  # Set the product to be visible
    
    if 'images' in new_product_data:
        new_product_data.pop('images')

    url = f"https://{shop_name}/admin/api/{api_version}/products.json"
    try:
        response = requests.post(url, headers=headers, json={"product": new_product_data})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error creating new product: {e}")
        return None

# Function to upload an image to a Shopify product
def upload_image_to_shopify(product_id, image_path, alt_text):
    try:
        with open(image_path, 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        image_data = {
            'image': {
                'attachment': encoded_image,
                'alt': alt_text
            }
        }

        url = f"https://{shop_name}/admin/api/{api_version}/products/{product_id}/images.json"
        response = requests.post(url, headers=headers, json=image_data)

        print(f"Uploading image: {image_path}")
        print(f"Alt Text: {alt_text}")
        print(f"Response status code: {response.status_code}")
        #print(f"Response text: {response.text}")

        if response.status_code in (200, 201):
            print(f"Successfully uploaded image {image_path}")
            return response.json()
        else:
            print(f"Error uploading image: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Exception during image upload: {e}")
        return None

# Base product ID (the product to duplicate)
base_product_id = '8185972687047'

# Get the base product
base_product = get_product(base_product_id)

if base_product and 'product' in base_product:
    base_product_data = base_product['product']

    # Loop through each folder in the base path
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)
        if os.path.isdir(folder_path):
            new_product_title = folder_name.replace('_', ' ')
            tags = add_state_tags(new_product_title)

            new_product = create_new_product(base_product_data, new_product_title, tags)
            if new_product and 'product' in new_product:
                new_product_id = new_product['product']['id']
                print(f"Created new product: {new_product['product']['title']} with ID: {new_product_id}")

                for image_file in image_order:
                    image_path = os.path.join(folder_path, image_file)
                    if os.path.isfile(image_path):
                        alt_text = alt_text_mapping.get(image_file, "Default Alt Text")
                        uploaded_image = upload_image_to_shopify(new_product_id, image_path, alt_text)
                        if uploaded_image:
                            print(f"Successfully uploaded image {image_file} with alt text '{alt_text}'")
                        else:
                            print(f"Failed to upload image {image_file}")
            else:
                print(f"Failed to create new product for folder {folder_name}.")
else:
    print("Failed to retrieve base product data.")
