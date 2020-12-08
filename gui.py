import PySimpleGUI as sg
import wikipedia
# Define the window's contents
layout = [[sg.Text("Enter your command")],
          [sg.Input()],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    popup = values[0]

    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

    wiki_res = wikipedia.summary(popup, sentences=1)

    sg.Popup('Wikipedia Results:'+ wiki_res)
    print(popup)

# Finish up by removing from the screen
window.close()