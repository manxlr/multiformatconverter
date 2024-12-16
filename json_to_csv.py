import json
import csv

def json_to_csv(input_json_file, output_csv_file):
    """
    Converts a JSON file to a CSV file.
    """
    try:
        with open(input_json_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        print(f"Successfully converted {input_json_file} to {output_csv_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
