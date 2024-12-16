import os
from text_to_pdf import txt_to_pdf  # Import the function from text_to_pdf.py
from pdf_to_text import pdf_to_text  # Import the function from pdf_to_text.py

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

def convert_pdf_to_text(input_pdf_file, output_txt_file):
    """
    Converts a PDF file to a text file.
    """
    try:
        if not os.path.exists(input_pdf_file):
            raise FileNotFoundError(f"The file {input_pdf_file} does not exist.")
        
        # Call the pdf_to_text function
        pdf_to_text(input_pdf_file, output_txt_file)
        
    except Exception as e:
        print(f"Error during conversion: {e}")
