import json

def text_to_json(input_txt_file, output_json_file):
    """
    Converts a text file to a JSON file.
    Assumes each line in the text file contains 'key: value' pairs.
    """
    try:
        with open(input_txt_file, 'r', encoding='utf-8') as txt_file:
            data = {}
            for line in txt_file:
                key, value = line.strip().split(':', 1)
                data[key.strip()] = value.strip()
        
        with open(output_json_file, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"Successfully converted {input_txt_file} to {output_json_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
