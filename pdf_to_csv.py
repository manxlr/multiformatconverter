import csv
from pdf_to_text import pdf_to_text

def pdf_to_csv(input_pdf_file, output_csv_file, delimiter=" "):
    """
    Converts a PDF file to a CSV file.
    """
    try:
        temp_txt_file = "temp_pdf_to_txt.txt"
        pdf_to_text(input_pdf_file, temp_txt_file)
        
        with open(temp_txt_file, 'r', encoding='utf-8') as txt_file, \
                open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            for line in txt_file:
                csv_writer.writerow(line.strip().split(delimiter))
        
        print(f"Successfully converted {input_pdf_file} to {output_csv_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
