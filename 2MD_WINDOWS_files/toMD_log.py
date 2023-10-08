import sys
import os
from datetime import datetime
# ********************************************
# Get the current date with the name of the month
current_date = datetime.now().strftime("%B-%d-%Y-%H%M%S")
# Function to save the prints in the program as a log
def md_program_log(folder_path):
    log_file_name = f"{current_date} 2MD_progam_log.txt"
    log_file_path = os.path.join(folder_path, log_file_name)

    # Create a file object for writing
    log_file = open(log_file_path, "w")

    # Redirect stdout to the log file
    sys.stdout = log_file
    
    return log_file
