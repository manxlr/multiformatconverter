import csv

def text_to_csv(input_txt_file, output_csv_file, delimiter=" "):
    """
    Converts a text file to a CSV file.
    Assumes the text file uses a specified delimiter (default is space) to separate columns.
    """
    try:
        # Open the text file
        with open(input_txt_file, mode='r', encoding='utf-8') as txt_file:
            # Read all lines from the text file
            lines = txt_file.readlines()
        
        # Prepare data for CSV (split each line into columns using the delimiter)
        rows = [line.strip().split(delimiter) for line in lines]
        
        # Open the output CSV file in write mode
        with open(output_csv_file, mode='w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # Write each row to the CSV
            csv_writer.writerows(rows)
        
        print(f"Successfully converted {input_txt_file} to {output_csv_file}")
    
    except Exception as e:
        print(f"Error during conversion: {e}")
