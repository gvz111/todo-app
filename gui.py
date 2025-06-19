import sys
sys.path.append(r"c:\users\armsapphire\appdata\local\programs\python\python313\lib\site-packages")

import FreeSimpleGUI as sg
import functions

label=sg.Text('Type in a To-Do')
add_button=sg.Button('Add')
input_box=sg.InputText(tooltip='Enter to-do', key='todo')

window=sg.Window('My To-Do App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    event, values =window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo= values['todo']+'\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
    
window.close()