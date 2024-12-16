def md_to_text(input_md_file, output_txt_file):
    """
    Converts a Markdown (.md) file to a plain text file.
    """
    try:
        with open(input_md_file, 'r', encoding='utf-8') as md_file, \
                open(output_txt_file, 'w', encoding='utf-8') as txt_file:
            txt_file.write(md_file.read())
        
        print(f"Successfully converted {input_md_file} to {output_txt_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
