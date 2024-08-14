import os
import shutil
import subprocess

# Path to the PRINTS folder
PRINTS_FOLDER = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\ALL PRINTS'

# Path to the NEW LAKES folder
NEW_LAKES_FOLDER = r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\NEW LAKES'

# File to store the record of completed lakes
COMPLETED_LAKES_FILE = 'completed_lakes.txt'

# List of scripts to run
SCRIPTS = [
    ('Folder Generator', 'Folder_Generator.py'),
    ('Etsy Image Generator', 'Etsy_Image_Generator.py'),
    ('Shopify Image Generator', 'Shopify_Image_Generator.py'),
    ('Shopify Product Generator', 'Shopify_Product_Generator.py')
]

def get_completed_lakes():
    if os.path.exists(COMPLETED_LAKES_FILE):
        with open(COMPLETED_LAKES_FILE, 'r') as file:
            completed_lakes = set(file.read().splitlines())
            return completed_lakes
    print("Completed lakes file not found.")
    return set()

def save_completed_lakes(lakes):
    with open(COMPLETED_LAKES_FILE, 'w') as file:
        file.write('\n'.join(sorted(lakes)))

def scan_lakes():
    completed_lakes = get_completed_lakes()
    
    if not os.path.exists(PRINTS_FOLDER):
        print(f"Error: PRINTS_FOLDER does not exist.")
        return set()
    
    current_files = os.listdir(PRINTS_FOLDER)
    print(f"Files found in PRINTS folder: {len(current_files)}")
    
    new_lakes = set(current_files) - set(completed_lakes)

    print(f"Total completed lakes in completed_lakes.txt: {len(completed_lakes)}")
    print(f"New lakes detected: {len(new_lakes)}")
    
    return new_lakes

def run_script(script_name):
    print(f"Running {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{script_name} completed successfully.")
    else:
        print(f"Error: {script_name} failed with error:\n{result.stderr}")
        return False
    return True

def main():
    new_lakes = scan_lakes()
    
    if not new_lakes:
        print("No new lakes found or all detected lakes have been processed.")
        return

    # Create the NEW LAKES folder if it doesn't exist
    if not os.path.exists(NEW_LAKES_FOLDER):
        os.makedirs(NEW_LAKES_FOLDER)

    # Copy new lakes to the NEW LAKES folder
    for lake_file in new_lakes:
        src = os.path.join(PRINTS_FOLDER, lake_file)
        dst = os.path.join(NEW_LAKES_FOLDER, lake_file)
        shutil.copy2(src, dst)

    # Sort and display new lakes
    new_lakes_sorted = sorted(new_lakes)
    print("\nNew lakes detected:\n")
    for lake in new_lakes_sorted:
        print(" " + lake)
    
    print("\nSelect the scripts to run:")
    print("1: All scripts")
    for i, (name, script) in enumerate(SCRIPTS):
        print(f"{i + 2}: {script}")

    selections = input("Enter numbers separated by commas (e.g., 1 for all, 2,3 for specific): ")
    selected_indices = [int(num.strip()) - 1 for num in selections.split(',')]

    if 0 in selected_indices:
        # Run all scripts if 'All scripts' option is selected
        for _, script in SCRIPTS:
            if not run_script(script):
                print("Stopping further execution due to script failure.")
                return
    else:
        # Run selected scripts
        for index in selected_indices:
            if index < len(SCRIPTS):  # Ensure the index is within range
                if not run_script(SCRIPTS[index - 1][1]):
                    print("Stopping further execution due to script failure.")
                    return

    # Ask the user to confirm adding new file names to completed_lakes.txt
    print("\nNew file names to be added to completed_lakes.txt:")
    for lake in new_lakes_sorted:
        print(lake)
    
    confirm = input("\nDo you want to add these new file names to completed_lakes.txt? (y/n): ").strip().lower()
    if confirm == 'y':
        save_completed_lakes(get_completed_lakes().union(new_lakes))
        print("New file names added to completed_lakes.txt.")
    else:
        print("New file names were not added to completed_lakes.txt.")
    

    delete_folders = input("\nDo you want to delete the contents of the 'Lake Folders with Images' Folder? \nIf not, there may be issues if you try to generate these images again. (y/n): ")

    if delete_folders == 'y':
        for filename in os.listdir(r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\Lake Folders with Images'):
            file_path = os.path.join(r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\Lake Folders with Images', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove the file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove the directory and its contents
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print("\nContents of 'Lake Folders with Images' Directory retained.")

    delete_new_lakes = input("\nAll images generated. Would you like to delete the contents of the 'NEW LAKES' Directory? (y/n): ")

    if delete_new_lakes == 'y':
        for filename in os.listdir(r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\NEW LAKES'):
            file_path = os.path.join(r'C:\Users\bnorm\iCloudDrive\IMAGE GENERATOR\NEW LAKES', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)  # Remove the file or link
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)  # Remove the directory and its contents
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print("\nContents of 'NEW LAKES' Directory retained.")

    print("Process completed.")



if __name__ == '__main__':
    main()
