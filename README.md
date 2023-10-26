# 2md
## Why?

I created this small script to enable me to handwrite my notes on my E-Notebook (Supernote A5 X) and then have those notes accessible in my Obsidian vault. 
If you wish to use it, please feel free to do so. If you want to make improvements, please go ahead. If you have any comments, please don't hesitate to let us know.

## Usage Instructions:

<ol>
    <li><strong>Download the Script according to your OS.</strong></li>
    <li><strong>Run the Script.</strong></li>
    <li><strong>Enter Folder's Paths.</strong></li>
    <li><strong>Completion (in Windows console will close automatically).</strong></li>
</ol>


## Explanation of the Code:

### This Python script performs the following tasks:

<ul>
    <li>It imports necessary modules.</li>
    <li>It checks if a configuration file (config.ini) exists. If it does, it reads the log, source and destination folder paths from it. If not, it prompts the user to input these paths and saves them in the configuration file for future use.</li>
    <li>It iterates through all files in the source folder.</li>
    <li>For each file with a .docx extension, converts it to .txt extension files.</li>
    <li>For each file with a .txt extension, converts it to .md extension files and move them to the desination folder.</li>
        <ul>
            <li>If the file already exists on destination folder, the content will be appended on destination file.</li>
        </ul>
    <li>After all the files are in the destination folder it will delete the .docx and .txt files from soucer folder to avoid repeated content.</li>
    <li>It creates a log file with all the process that was done.</li>
</ul>

#### This script allows you to easily convert and move multiple .txt files to .md files while saving the folder paths for future use, making it a convenient tool for file management tasks.
