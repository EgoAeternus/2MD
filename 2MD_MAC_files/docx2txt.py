import os
from docx import Document

# Function to extract text from a .docx file
def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return '\n'.join(text)

# Function to process a folder and convert .docx to .txt
def docx_2_txt(source_folder):
    counter = 0
    # Iterate over files in the folder
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Check if the file is a .docx file
        if filename.endswith(".docx"):
            counter += 1
            # Extract text from the .docx file
            text = extract_text_from_docx(file_path)

            # Create a corresponding .txt file with the same content
            new_txt_file = os.path.splitext(file_path)[0] + ".txt"
            with open(new_txt_file, "w", encoding="utf-8") as txt_file:
                txt_file.write(text)

            # Delete the original .docx file
            os.remove(file_path)

            print(f'\n#{counter}: "{filename}" converted to "{os.path.basename(new_txt_file)}" original removed.')
    print("\n*************************************")
    if counter != 0:
        if counter > 1:
            print(f"{counter} files converted from .docx to .txt.")
        elif counter == 1:
            print(f"{counter} file converted from .docx to .txt.")
        print("*************************************")
