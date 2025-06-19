import sys
sys.path.append(r"c:\users\armsapphire\appdata\local\programs\python\python313\lib\site-packages")

import FreeSimpleGUI as sg
import functions

label=sg.Text('Type in a To-Do')
input_box=sg.InputText(tooltip='Enter to-do')
add_button=sg.Button('Add')

window=sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()