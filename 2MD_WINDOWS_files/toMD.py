# Program created by Samael Tártaro
# Website: https://tartaro.lat
# Github: https://github.com/EgoAeternus/
# Email: samael@tartaro.lat

import os
import sys
import configparser
from docx2txt import docx_2_txt
from txt2md import txt_2_md
from toMD_log import md_program_log

# ********************************************
# Create or load the configuration file
config = configparser.ConfigParser()

# Try to load existing configuration if the file exists
if os.path.exists('config.ini'):
    config.read('config.ini')
    log_folder = config.get('Paths', 'log_folder')
    source_folder = config.get('Paths', 'source_folder')
    destination_folder = config.get('Paths', 'destination_folder')
else:
    # If the configuration file doesn't exist, prompt the user for the paths
    print("The logs will have all the information from each time this program runs.")
    log_folder = input("\nLog foler (where the logs will be saved) :")
    source_folder = input("\nSource folder (where .txt files are located): ")
    destination_folder = input("\nDestination folder (where .md files will be moved): ")
    
    # Save the paths in the configuration file
    config.add_section('Paths')
    config.set('Paths', 'log_folder', log_folder)
    config.set('Paths', 'source_folder', source_folder)
    config.set('Paths', 'destination_folder', destination_folder)
    
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

# ********************************************
# Redirect stdout to the log file
log_file = md_program_log(log_folder)

# ********************************************
# Importing modules
docx_2_txt(source_folder)
txt_2_md(source_folder, destination_folder)

# ********************************************
# Restore stdout back to the terminal
sys.stdout = sys.__stdout__

# Close the log file
log_file.close()
