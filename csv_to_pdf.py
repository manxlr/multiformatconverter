import os
from text_to_pdf import txt_to_pdf
from csv_to_text import csv_to_text

def csv_to_pdf(input_csv_file, output_pdf_file):
    """
    Converts a CSV file to a PDF by converting it to text first.
    """
    temp_txt_file = "temp_csv_to_txt.txt"
    try:
        # Convert CSV to temporary text file
        csv_to_text(input_csv_file, temp_txt_file)
        
        # Convert temporary text file to PDF
        txt_to_pdf(temp_txt_file, output_pdf_file)
        
        print(f"Successfully converted {input_csv_file} to {output_pdf_file}")
    
    except Exception as e:
        print(f"Error during conversion: {e}")
    
    finally:
        # Ensure the temporary text file is deleted after the process
        if os.path.exists(temp_txt_file):
            os.remove(temp_txt_file)
            print(f"Temporary file {temp_txt_file} deleted.")
