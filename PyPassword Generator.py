import string
import random
import PySimpleGUI as psg

psg.theme("BlueMono") # Changes the theme of the GUI
psg.set_options(font = "verdana 15") # Changes the font and font size of the GUI's display to Verdana and 15, respectively

# Creates the layout for the GUI
# The 'Push()' method pushes the block towards the right of the GUI
# The 'size' arguments of the 'Input()' method set the size of the dialog/display boxes. They are set to be the same as the font size: 15
layout = [
    [psg.Text("Uppercase: "), psg.Push(), psg.Input(size = 15, key = "-UP-")],
    [psg.Text("Lowercase: "), psg.Push(), psg.Input(size = 15, key = "-LOW-")],
    [psg.Text("Digits: "), psg.Push(), psg.Input(size = 15, key = "-DIG-")],
    [psg.Text("Symbols: "), psg.Push(), psg.Input(size = 15, key = "-SYM-")],
    [psg.Button("OK"), psg.Button("Cancel")],
    [psg.Text("Password: "), psg.Push(), psg.Multiline(size = 15, no_scrollbar = True, disabled = True, key = "-PASS-")]
]

window = psg.Window("PyPassword Generator", layout)

while True:
    event, values = window.read()
    if event == "OK":
        try:
            user_uppers = int(values["-UP-"])
            uppers = random.sample(string.ascii_uppercase, user_uppers)

            user_lowers = int(values["-LOW-"])
            lowers = random.sample(string.ascii_lowercase, user_lowers)

            user_digits = int(values["-DIG-"])
            digits = random.sample(string.digits, user_digits)

            user_symbols = int(values["-SYM-"])
            symbols = random.sample(string.punctuation, user_symbols)

            unshuffled_password_string = uppers + lowers + digits + symbols

            shuffled_password_string = random.sample(unshuffled_password_string, len(unshuffled_password_string))

            password = "".join(shuffled_password_string)

            window["-PASS-"].update(password) # Displays the password in the GUI's password dialog box
        except ValueError:
            window["-PASS-"].update("Invalid response.") # Displays "Invalid response." when the user doesn't enter a digit into the dialog box
    elif event == "Cancel" or event == psg.WIN_CLOSED:
        break

window.close()
