import os
import time
import shutil
from datetime import datetime

# ********************************************
# Get the current date with the name of the month
current_date = datetime.now().strftime("%B/%d/%Y - %H:%M:%S")
# ********************************************
# Function to convert .txt files into .md files
# If the files already exist in the destination folder
# the function will append the content to the existing file.

def txt_2_md(source_folder, destination_folder):
    counter = 0
    for file_name in os.listdir(source_folder):
        # Check if the file is a .txt file
        if file_name.endswith('.txt'):
            counter += 1
            # Build the full path to the source file
            source_path = os.path.join(source_folder, file_name)
            
            # Generate the new file name with .md extension
            new_file_name = file_name.replace('.txt', '.md')
            
            # Build the full path to the destination file
            destination_path = os.path.join(destination_folder, new_file_name)
            
            # Check if a file with the same name exists in the destination folder
            if os.path.exists(destination_path):
                # If it exists, read the existing .md file
                with open(destination_path, 'r') as existing_md_file:
                    existing_content = existing_md_file.read()

                # Read the new .txt file
                with open(source_path, 'r') as new_txt_file:
                    new_content = new_txt_file.read()

                # Append the current date and new content from .txt to .md while preserving the existing content
                combined_content = existing_content + f' \n\n###### *** UPDATED CONTENT: ({current_date}) ***\n\n' + new_content

                # Write the combined content back to the .md file
                with open(destination_path, 'w') as combined_md_file:
                    combined_md_file.write(combined_content)

                # Delete the .txt file from the source folder
                os.remove(source_path)
                print(f'\n#{counter}: "{file_name}" converted to "{new_file_name}" content appended in the file at destination folder.')

            else:
                # If the .md file doesn't exist, simply move the .txt file to the destination
                shutil.move(source_path, destination_path)
                print(f'\n#{counter}: "{file_name}" converted to "{new_file_name}" moved to destination folder.')
    print("\n****************")
    if counter != 0:
        if counter > 1:
            print(f"From: {source_folder}")
            print(f"{counter} files moved.")
            print(f"In: {destination_folder}")
        elif counter == 1:
            print(f"From: {source_folder}")
            print(f"{counter} file move.")
            print(f"In: {destination_folder}")
    else:
        print(f"No files moved today: {current_date}")
    print("****************")
