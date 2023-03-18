import os
from PyPDF4 import PdfFileMerger

# Get a list of all PDF files in the directory
pdf_files = [f for f in os.listdir('.') if f.endswith('.pdf')]

# Create a PDF file merger object
pdf_merger = PdfFileMerger()

# Loop through the PDF files and add them to the merger object
for pdf_file in pdf_files:
    with open(pdf_file, 'rb') as f:
        pdf_merger.append(f)

# Save the merged PDF file to disk
with open('merged.pdf', 'wb') as output:
    pdf_merger.write(output)
