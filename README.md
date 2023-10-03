# txt2md
## Why?

I created this small script to enable me to handwrite my notes on my E-Notebook (Supernote A5 X) and then have those notes accessible in my Obsidian vault. 
If you wish to use it, please feel free to do so. If you want to make improvements, please go ahead. If you have any comments, please don't hesitate to let us know.

## Usage Instructions:

<ol>
    <li>**Download the Script:** First, download the Python script file.</li>
    <li>**Run the Script:** Double-click the script file to run it. It will open a console window, which will guide you through the process.</li>
    <li>**Enter Folders:** When prompted, enter the paths to the source folder (where your .txt files are located) and the destination folder (where the converted .md files will be moved to). You can type or paste the folder paths.</li>
    <li>**Repeat or Save Configuration (Optional):** If you plan to use the same folders repeatedly, you can choose to save the configuration. This way, you won't have to enter the folder paths each time you run the script. The script will create a config.ini file in the same directory to store these paths.</li>
    <li>**Execution:** The script will then go through the source folder, find all .txt files, convert them to .md files, and move them to the destination folder. You will see messages indicating the progress of the process.</li>
    <li>**Completion:** Once the process is completed, the console window will display a message indicating that the process is finished.</li>
</ol>


## Explanation of the Code:

### This Python script performs the following tasks:

<ul>
    <li>It imports necessary modules: os, shutil, and configparser.</li>
    <li>It checks if a configuration file (config.ini) exists. If it does, it reads the source and destination folder paths from it. If not, it prompts the user to input these paths and saves them in the configuration file for future use.</li>
    <li>It iterates through all files in the source folder.</li>
    <li>For each file with a .txt extension in the source folder, it constructs the full path to the source file and generates a new filename with a .md extension.</li>
    <li>It constructs the full path to the destination file in the destination folder.</li>
    <li>It uses shutil.move() to move the source file to the destination file with the new extension, effectively converting and transferring the file.</li>
    <li>It prints a message for each file processed, indicating the conversion and movement.</li>
    <li>Finally, it displays a message in the console when the process is complete.</li>
</ul>

#### This script allows you to easily convert and move multiple .txt files to .md files while saving the folder paths for future use, making it a convenient tool for file management tasks.
