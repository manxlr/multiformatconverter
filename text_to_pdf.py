from fpdf import FPDF

# Function to convert text file to PDF
def txt_to_pdf(input_txt_file, output_pdf_file):
    # Create a PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Add a page to the PDF
    pdf.add_page()
    
    # Set font for the PDF (Arial, size 12)
    pdf.set_font('Arial', size=12)
    
    try:
        # Open the input text file
        with open(input_txt_file, 'r', encoding='utf-8') as file:
            # Read the content of the file
            text = file.read()
            
            # Add the text to the PDF (multi-line)
            pdf.multi_cell(0, 10, text)
        
        # Output the PDF to the specified file
        pdf.output(output_pdf_file)
        print(f"PDF created successfully: {output_pdf_file}")
    
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
txt_to_pdf('input.txt', 'output.pdf')
