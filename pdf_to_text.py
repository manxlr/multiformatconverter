import fitz  # PyMuPDF

def pdf_to_text(input_pdf_file, output_txt_file):
    """
    Converts a PDF file to a text file.
    """
    try:
        # Open the PDF file
        pdf_document = fitz.open(input_pdf_file)
        
        # Initialize an empty string to store the text
        text = ""
        
        # Loop through each page in the PDF
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)  # Load the page
            text += page.get_text()  # Extract the text from the page
        
        # Write the extracted text to the output file
        with open(output_txt_file, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)
        
        print(f"Successfully converted {input_pdf_file} to {output_txt_file}")
    
    except Exception as e:
        print(f"Error during conversion: {e}")
