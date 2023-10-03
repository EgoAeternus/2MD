# txt2md
## Why?

I created this small script to enable me to handwrite my notes on my E-Notebook (Supernote A5 X) and then have those notes accessible in my Obsidian vault. 
If you wish to use it, please feel free to do so. If you want to make improvements, please go ahead. If you have any comments, please don't hesitate to let us know.

## Usage Instructions:

<ol>
    <li><strong>Download the Script (from.txt2.md.exe):</strong> First, download the Python script file.<br> I recommend you to have the file in its own folder since it will create a config.ini file.</li>
    <li><strong>Run the Script:</strong> Double-click the script file to run it. It will open a console window, which will guide you through the process.</li>
    <li><strong>Enter Folders:</strong> When prompted, enter the paths to the source folder (where your .txt files are located) and the destination folder (where the converted .md files will be moved to). You can type or paste the folder paths.<br> The script is made so you
        don't have to set the paths every time you run the program, the script will create a config.ini file in the same directory to store these paths.</li>
    <li><strong>Execution:</strong> The script will then go through the source folder, find all .txt files, convert them to .md files, and move them to the destination folder.</li>
    <li><strong>Completion:</strong> Once the process is completed, the console window will display a message indicating that the process is finished.</li>
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
