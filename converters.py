import os
from text_to_pdf import txt_to_pdf  # Import the function from text_to_pdf.py
from pdf_to_text import pdf_to_text  # Import the function from pdf_to_text.py
from csv_to_text import csv_to_text # Import the function from csv_to_text.py
from text_to_csv import text_to_csv  # Import the function from text_to_csv.py

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

def convert_csv_to_text(input_csv_file, output_txt_file):
    """
    Converts a CSV file to a text file.
    """
    try:
        if not os.path.exists(input_csv_file):
            raise FileNotFoundError(f"The file {input_csv_file} does not exist.")
        
        # Call the csv_to_text function
        csv_to_text(input_csv_file, output_txt_file)
        
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_text_to_csv(input_txt_file, output_csv_file, delimiter=" "):
    """
    Converts a text file to a CSV file.
    Assumes the text file uses a specified delimiter (default is space) to separate columns.
    """
    try:
        if not os.path.exists(input_txt_file):
            raise FileNotFoundError(f"The file {input_txt_file} does not exist.")
        
        # Call the text_to_csv function
        text_to_csv(input_txt_file, output_csv_file, delimiter)
        
    except Exception as e:
        print(f"Error during conversion: {e}")
