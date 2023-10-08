import os
import sys
import win32com.client as win32

# Function to convert .doc to .txt
def extract_txt_from_doc(doc_file):
    # Initialize Word application
    word = win32.gencache.EnsureDispatch("Word.Application")

    # Open the .doc file
    doc = word.Documents.Open(doc_file)

    # Extract text from the document
    text = doc.Content.Text

    # Close the document and Word application
    doc.Close()
    word.Quit()

    return text

# Function to convert .doc files into .txt files
def doc_2_txt(source_folder):
    counter = 0
    # Iterate through files in the folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".doc"):
            counter += 1
            # Create the full path to the .doc file
            doc_file = os.path.join(source_folder, filename)

            # Convert .doc to .txt
            text = extract_txt_from_doc(doc_file)

            # Create the .txt file path
            new_txt_file = os.path.splitext(doc_file)[0] + ".txt"

            # Write the extracted text to the .txt file
            with open(new_txt_file, "w", encoding="utf-8") as txt_file:
                txt_file.write(text)

            # Delete the .doc file
            os.remove(doc_file)

            print(f'\n#{counter}: "{filename}" converted to "{os.path.basename(new_txt_file)}" original removed.')
    print("\n*************************************")
    if counter != 0:
        if counter > 1:
            print(f"{counter} files converted from .doc to .txt.")
        elif counter == 1:
            print(f"{counter} file converted from .doc to .txt.")
        print("*************************************")


