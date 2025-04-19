import PyPDF2


# List of PDF files to merge
pdffiles = ['file1.pdf', 'file2.pdf']



# Create PDF merger object
merger = PyPDF2.PdfMerger()


    # Append PDFs one by one
for filename in pdffiles:
            with open(filename, 'rb') as pdfFile:
                merger.append(pdfFile)
        
        # Write merged PDF to output file
merger.write('merged.pdf')


    


merger.close()

print("PDF merge completed successfully!")
