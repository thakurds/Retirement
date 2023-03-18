from PIL import Image
from PyPDF2 import PdfFileReader, PdfMerger
import os
#import fitz

# Set directory containing JPG files
jpg_directory ="."
pdf_directory ="."

# Create empty list to store converted PDF files
pdf_files = []

# Loop through all JPG files in directory and convert to PDF
for filename in os.listdir(jpg_directory):
    if filename.endswith(".jpeg"):
        print (filename)
        with Image.open(os.path.join(jpg_directory, filename)) as img:
            pdf_filename = filename[:-4] + ".pdf"
            img.save(pdf_filename, "PDF")
            pdf_files.append(pdf_filename)






