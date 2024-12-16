# main_gui.py
import PySimpleGUI as sg
import os
import time
from converters import convert_text_to_pdf,convert_pdf_to_text,convert_csv_to_text,convert_text_to_csv  # Import the conversion functions

# Define supported input formats
SUPPORTED_INPUT_FORMATS = [".pdf", ".csv", ".json", ".md", ".txt"]

# Define the layout of the GUI
layout = [
    [sg.Text("MultiFormatConverter", font=("Helvetica Bold", 20), justification="center", expand_x=True)],
    [sg.Text("Select File(s):"), sg.Input(key="-FILE_PATHS-", enable_events=True, readonly=True), sg.FilesBrowse()],
    [sg.Text("Choose Output Formats:")],
    [sg.Checkbox("PDF", key="-PDF-"), sg.Checkbox("CSV", key="-CSV-"),
     sg.Checkbox("JSON", key="-JSON-"), sg.Checkbox("Markdown", key="-MARKDOWN-"), sg.Checkbox("TXT", key="-TXT-")],
    [sg.Button("Select All", key="-SELECT_ALL-"), sg.Button("Deselect All", key="-DESELECT_ALL-")],
    [sg.Button("Convert", key="-CONVERT-", size=(10, 1)), sg.Button("Exit", key="-EXIT-", size=(10, 1))],
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-')],
    [sg.Output(size=(80, 20), key="-LOG_OUTPUT-")],
]

# Create the window
window = sg.Window("MultiFormatConverter", layout, resizable=True, finalize=True, background_color="#F0F4F8")

# Function to simulate subtle "fade-in" animation effect
def fade_in_effect():
    window['-LOG_OUTPUT-'].update("Loading Interface...")
    time.sleep(1)

fade_in_effect()

current_input_format = None

# Main event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "-EXIT-":
        break

    if event == "-SELECT_ALL-":
        window["-PDF-"].update(True)
        window["-CSV-"].update(True)
        window["-JSON-"].update(True)
        window["-MARKDOWN-"].update(True)
        window["-TXT-"].update(True)

    if event == "-DESELECT_ALL-":
        window["-PDF-"].update(False)
        window["-CSV-"].update(False)
        window["-JSON-"].update(False)
        window["-MARKDOWN-"].update(False)
        window["-TXT-"].update(False)

    if event == "-CONVERT-":
        file_paths = values["-FILE_PATHS-"].split(";")
        selected_formats = [
            "PDF" if values["-PDF-"] else None,
            "CSV" if values["-CSV-"] else None,
            "JSON" if values["-JSON-"] else None,
            "Markdown" if values["-MARKDOWN-"] else None,
            "TXT" if values["-TXT-"] else None
        ]
        selected_formats = [f for f in selected_formats if f]

        if not file_paths[0]:
            print("Error: No files selected.")
        elif not selected_formats:
            print("Error: No output format selected.")
        else:
            for file in file_paths:
                folder, base = os.path.split(file)
                ext = os.path.splitext(file)[1].lower()

                if ext not in SUPPORTED_INPUT_FORMATS:
                    print(f"{file} has an unsupported input format.")
                    continue

                current_input_format = ext
                print(f"Input File: {file}")
                print(f"Available Output Formats (excluding {ext}): {selected_formats}")

                for fmt in selected_formats:
                    if fmt == "PDF" and ext == ".txt":
                        new_pdf_file = os.path.join(folder, f"{os.path.splitext(base)[0]}.pdf")
                        print(f"Creating {new_pdf_file}")
                        
                        # Call the converter function for PDF
                        convert_text_to_pdf(file, new_pdf_file)

                    elif fmt == "TXT" and ext == ".pdf":
                        new_txt_file = os.path.join(folder, f"{os.path.splitext(base)[0]}.txt")
                        print(f"Creating {new_txt_file}")
                        # Call the converter function for converting PDF to text
                        convert_pdf_to_text(file, new_txt_file)

                    elif fmt == "TXT" and ext == ".csv":
                        new_txt_file = os.path.join(folder, f"{os.path.splitext(base)[0]}.txt")
                        print(f"Creating {new_txt_file}")
                        # Call the converter function for converting CSV to text
                        convert_csv_to_text(file, new_txt_file)

                    elif fmt == "CSV" and ext == ".txt":
                        new_csv_file = os.path.join(folder, f"{os.path.splitext(base)[0]}.csv")
                        print(f"Creating {new_csv_file}")
                        # Call the converter function for converting text to CSV
                        convert_text_to_csv(file, new_csv_file)

                    else:
                        print(f"Conversion not supported for the combination of {fmt} and {ext}.")
                    # For other formats (e.g., JSON, etc.), add their conversion logic here.
                    # This part of your code can be extended as needed.

window.close()
