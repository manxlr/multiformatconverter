from md_to_text import md_to_text
from text_to_pdf import txt_to_pdf

def md_to_pdf(input_md_file, output_pdf_file):
    """
    Converts a Markdown file to a PDF by converting it to text first.
    """
    try:
        temp_txt_file = "temp_md_to_txt.txt"
        md_to_text(input_md_file, temp_txt_file)
        txt_to_pdf(temp_txt_file, output_pdf_file)
        
        print(f"Successfully converted {input_md_file} to {output_pdf_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
