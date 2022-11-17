import PySimpleGUI as sg

sg.theme('Dark')

layout = [
    [sg.Text('MICROWAVE', font=("Helvetica", 15, 'bold'), size=(30, 1), justification='center')],
    [sg.Text(' ' * 250, auto_size_text=False, size=(50, 1))],
    [sg.Text((". . . ` ` `") * 6 + (" . . ."), font=("monospaced", 15), auto_size_text=False, justification="center", size=(50, 1))],
    [sg.Text('Upload File', font=("Helvetica", 15), justification='left', size=(9, 1)), sg.InputText(size=(30, 1), key='midifile'), sg.FileBrowse(size=(10, 1), file_types=(("MIDI files", "*.mid")))],
    [sg.Text(("` ` ` . . .") * 6 + (" ` ` `"), font=("monospaced", 15), auto_size_text=False, justification="center", size=(50, 1))],
    [sg.Text(' ' * 250, auto_size_text=False, size=(50, 1))],
    [sg.SimpleButton('PLAY', size=(12, 2), font=("Helvetica", 15), bind_return_key=True), sg.Cancel('CANCEL', size=(12, 2), font=("Helvetica", 15)) ],
]

window = sg.Window('MIDI File Player', auto_size_text=False, default_element_size=(20, 1), font=("Helvetica", 12), element_justification="c").Layout(layout)

window.read()

