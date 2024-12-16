import os
# Import all the conversion functions
from text_to_pdf import txt_to_pdf
from pdf_to_text import pdf_to_text
from csv_to_text import csv_to_text
from text_to_csv import text_to_csv
from text_to_json import text_to_json
from json_to_text import json_to_text
from pdf_to_csv import pdf_to_csv
from csv_to_pdf import csv_to_pdf
from md_to_text import md_to_text
from text_to_md import text_to_md
from csv_to_json import csv_to_json
from json_to_csv import json_to_csv
from pdf_to_md import pdf_to_md
from md_to_pdf import md_to_pdf

def convert_text_to_pdf(input_txt_file, output_pdf_file):
    try:
        if not os.path.exists(input_txt_file):
            raise FileNotFoundError(f"The file {input_txt_file} does not exist.")
        txt_to_pdf(input_txt_file, output_pdf_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_pdf_to_text(input_pdf_file, output_txt_file):
    try:
        if not os.path.exists(input_pdf_file):
            raise FileNotFoundError(f"The file {input_pdf_file} does not exist.")
        pdf_to_text(input_pdf_file, output_txt_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_csv_to_text(input_csv_file, output_txt_file):
    try:
        if not os.path.exists(input_csv_file):
            raise FileNotFoundError(f"The file {input_csv_file} does not exist.")
        csv_to_text(input_csv_file, output_txt_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_text_to_csv(input_txt_file, output_csv_file, delimiter=" "):
    try:
        if not os.path.exists(input_txt_file):
            raise FileNotFoundError(f"The file {input_txt_file} does not exist.")
        text_to_csv(input_txt_file, output_csv_file, delimiter)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_text_to_json(input_txt_file, output_json_file):
    try:
        if not os.path.exists(input_txt_file):
            raise FileNotFoundError(f"The file {input_txt_file} does not exist.")
        text_to_json(input_txt_file, output_json_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_json_to_text(input_json_file, output_txt_file):
    try:
        if not os.path.exists(input_json_file):
            raise FileNotFoundError(f"The file {input_json_file} does not exist.")
        json_to_text(input_json_file, output_txt_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_pdf_to_csv(input_pdf_file, output_csv_file):
    try:
        if not os.path.exists(input_pdf_file):
            raise FileNotFoundError(f"The file {input_pdf_file} does not exist.")
        pdf_to_csv(input_pdf_file, output_csv_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_csv_to_pdf(input_csv_file, output_pdf_file):
    try:
        if not os.path.exists(input_csv_file):
            raise FileNotFoundError(f"The file {input_csv_file} does not exist.")
        csv_to_pdf(input_csv_file, output_pdf_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_md_to_text(input_md_file, output_txt_file):
    try:
        if not os.path.exists(input_md_file):
            raise FileNotFoundError(f"The file {input_md_file} does not exist.")
        md_to_text(input_md_file, output_txt_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_text_to_md(input_txt_file, output_md_file):
    try:
        if not os.path.exists(input_txt_file):
            raise FileNotFoundError(f"The file {input_txt_file} does not exist.")
        text_to_md(input_txt_file, output_md_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_csv_to_json(input_csv_file, output_json_file):
    try:
        if not os.path.exists(input_csv_file):
            raise FileNotFoundError(f"The file {input_csv_file} does not exist.")
        csv_to_json(input_csv_file, output_json_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_json_to_csv(input_json_file, output_csv_file):
    try:
        if not os.path.exists(input_json_file):
            raise FileNotFoundError(f"The file {input_json_file} does not exist.")
        json_to_csv(input_json_file, output_csv_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_pdf_to_md(input_pdf_file, output_md_file):
    try:
        if not os.path.exists(input_pdf_file):
            raise FileNotFoundError(f"The file {input_pdf_file} does not exist.")
        pdf_to_md(input_pdf_file, output_md_file)
    except Exception as e:
        print(f"Error during conversion: {e}")

def convert_md_to_pdf(input_md_file, output_pdf_file):
    try:
        if not os.path.exists(input_md_file):
            raise FileNotFoundError(f"The file {input_md_file} does not exist.")
        md_to_pdf(input_md_file, output_pdf_file)
    except Exception as e:
        print(f"Error during conversion: {e}")
