import json

def json_to_text(input_json_file, output_txt_file):
    """
    Converts a JSON file to a text file with 'key: value' pairs.
    """
    try:
        with open(input_json_file, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        with open(output_txt_file, 'w', encoding='utf-8') as txt_file:
            for key, value in data.items():
                txt_file.write(f"{key}: {value}\n")
        
        print(f"Successfully converted {input_json_file} to {output_txt_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
