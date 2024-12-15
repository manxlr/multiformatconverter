import PySimpleGUI as sg
import os
import time

# Define supported input formats
SUPPORTED_INPUT_FORMATS = [".pdf", ".csv", ".json", ".md", ".txt"]

# Suppress the PySimpleGUI registration prompt
#sg.set_options(show_register_popup=False)

# Define the layout of the GUI
layout = [
    [sg.Text("MultiFormatConverter", font=("Helvetica Bold", 20), justification="center", expand_x=True)],
    [sg.Text("Select File(s):"), sg.Input(key="-FILE_PATHS-", enable_events=True, readonly=True), sg.FilesBrowse()],
    [sg.Text("Choose Output Formats:")],
    [sg.Checkbox("PDF", key="-PDF-"), sg.Checkbox("Excel (CSV)", key="-EXCEL-"),
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
        window["-EXCEL-"].update(True)
        window["-JSON-"].update(True)
        window["-MARKDOWN-"].update(True)
        window["-TXT-"].update(True)

    if event == "-DESELECT_ALL-":
        window["-PDF-"].update(False)
        window["-EXCEL-"].update(False)
        window["-JSON-"].update(False)
        window["-MARKDOWN-"].update(False)
        window["-TXT-"].update(False)

    if event == "-CONVERT-":
        file_paths = values["-FILE_PATHS-"].split(";")
        selected_formats = [
            "PDF" if values["-PDF-"] else None,
            "Excel (CSV)" if values["-EXCEL-"] else None,
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
                    new_file = os.path.join(folder, f"{base}.{fmt.lower().replace(' ', '_')}")
                    print(f"Creating {new_file}")

                    with open(new_file, "w") as f:
                        f.write(f"{fmt} content for {file}")

window.close()
