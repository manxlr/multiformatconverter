import csv

def csv_to_text(input_csv_file, output_txt_file):
    """
    Converts a CSV file to a text file.
    """
    try:
        # Open the CSV file
        with open(input_csv_file, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Initialize an empty string to store the text
            text = ""
            
            # Loop through each row in the CSV
            for row in csv_reader:
                # Join each column in the row with a space or other separator
                text += " ".join(row) + "\n"
        
        # Write the extracted text to the output file
        with open(output_txt_file, "w", encoding="utf-8") as txt_file:
            txt_file.write(text)
        
        print(f"Successfully converted {input_csv_file} to {output_txt_file}")
    
    except Exception as e:
        print(f"Error during conversion: {e}")
