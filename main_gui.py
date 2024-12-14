import PySimpleGUI as sg

# Suppress the PySimpleGUI registration prompt
sg.set_options(show_register_popup=False)

# Define the layout of the GUI
layout = [
    [sg.Text("File Format Converter", font=("Helvetica", 16), justification="center", expand_x=True)],
    [sg.Text("Select File(s):"), sg.Input(key="-FILE_PATHS-", enable_events=True, readonly=True), sg.FilesBrowse()],
    [sg.Text("Choose Output Format:"), sg.Combo(["PDF", "Excel", "JSON", "Markdown"], key="-OUTPUT_FORMAT-", default_value="PDF", readonly=True)],
    [sg.Button("Convert", key="-CONVERT-", size=(10, 1)), sg.Button("Exit", key="-EXIT-", size=(10, 1))],
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-')],
    [sg.Output(size=(80, 20), key="-LOG_OUTPUT-")],
]

# Create the window
window = sg.Window("File Format Converter", layout, resizable=True, finalize=True)

# Main event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "-EXIT-":
        break

    if event == "-CONVERT-":
        file_paths = values["-FILE_PATHS-"].split(";")
        output_format = values["-OUTPUT_FORMAT-"]

        if not file_paths[0]:
            print("Error: No files selected.")
        elif not output_format:
            print("Error: No output format selected.")
        else:
            print(f"Starting conversion to {output_format} for files: {file_paths}")
            # Placeholder for conversion logic
            for file in file_paths:
                print(f"Converting {file} to {output_format}...")
            print("Conversion completed!")

window.close()
