import csv
import json

def csv_to_json(input_csv_file, output_json_file):
    """
    Converts a CSV file to a JSON file.
    """
    try:
        with open(input_csv_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]
        
        with open(output_json_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"Successfully converted {input_csv_file} to {output_json_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
