from functions import *
import FreeSimpleGUI as FSG

label = FSG.Text("todo")
input_box = FSG.InputText(tooltip="Enter todo")
add_button = FSG.Button("Add")

window = FSG.Window("Gimu", layout = [[label], [input_box, add_button]])
window.read()
window.close()