import csv
import os
from pdf_to_text import pdf_to_text

def pdf_to_csv(input_pdf_file, output_csv_file, delimiter=" "):
    """
    Converts a PDF file to a CSV file.
    """
    temp_txt_file = "temp_pdf_to_txt.txt"
    try:
        # Convert PDF to temporary text file
        pdf_to_text(input_pdf_file, temp_txt_file)
        
        # Read the text file and write the CSV
        with open(temp_txt_file, 'r', encoding='utf-8') as txt_file, \
             open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            for line in txt_file:
                csv_writer.writerow(line.strip().split(delimiter))
        
        print(f"Successfully converted {input_pdf_file} to {output_csv_file}")
    
    except Exception as e:
        print(f"Error during conversion: {e}")
    
    finally:
        # Ensure the temporary text file is deleted after the process
        if os.path.exists(temp_txt_file):
            os.remove(temp_txt_file)
            print(f"Temporary file {temp_txt_file} deleted.")
