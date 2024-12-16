def text_to_md(input_txt_file, output_md_file):
    """
    Converts a text file to a Markdown (.md) file.
    """
    try:
        with open(input_txt_file, 'r', encoding='utf-8') as txt_file, \
                open(output_md_file, 'w', encoding='utf-8') as md_file:
            md_file.write(txt_file.read())
        
        print(f"Successfully converted {input_txt_file} to {output_md_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
