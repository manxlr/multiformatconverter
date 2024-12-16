import os
from pdf_to_text import pdf_to_text
from text_to_md import text_to_md

def pdf_to_md(input_pdf_file, output_md_file):
    """
    Converts a PDF file to a Markdown file by converting it to text first.
    """
    temp_txt_file = "temp_pdf_to_txt.txt"

    try:
        # Convert PDF to Text
        pdf_to_text(input_pdf_file, temp_txt_file)
        # Convert Text to Markdown
        text_to_md(temp_txt_file, output_md_file)

        print(f"Successfully converted {input_pdf_file} to {output_md_file}")

    except Exception as e:
        print(f"Error during conversion: {e}")

    finally:
        # Ensure the temporary file is deleted
        if os.path.exists(temp_txt_file):
            os.remove(temp_txt_file)
            print(f"Temporary file {temp_txt_file} has been deleted.")
