import sys
sys.path.append(r"c:\users\armsapphire\appdata\local\programs\python\python313\lib\site-packages")

import FreeSimpleGUI as sg
from zip_creator import make_archive

layout= [  [sg.Text('Select files to compress')],
            [sg.Input(), sg.FilesBrowse('Browse')],
            
            [sg.Text('Select folder path')],
            [sg.Input(), sg.FolderBrowse('Select')],
            
            [sg.Button('Compress'), sg.Text(key='output')]
        ]
        
window = sg.Window('Window title', layout)

while True:
    event, values = window.read()
    filepaths = values['Browse'].split(';')
    folderpath = values['Select']
    make_archive(filepaths, folderpath)
    window['output'].update(value='Compession completed')

window.close()