# converters.py
import os
from text_to_pdf import txt_to_pdf  # Import the function from text_to_pdf.py

def convert_text_to_pdf(input_txt_file, output_pdf_file):
    """
    Converts a text file to a PDF file.
    """
    try:
        if not os.path.exists(input_txt_file):
            raise FileNotFoundError(f"The file {input_txt_file} does not exist.")
        
        # Call the text_to_pdf function
        txt_to_pdf(input_txt_file, output_pdf_file)
        
    except Exception as e:
        print(f"Error during conversion: {e}")
