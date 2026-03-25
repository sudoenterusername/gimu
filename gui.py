from functions import *
import FreeSimpleGUI as FSG

label = FSG.Text("todo")
input_box = FSG.InputText(tooltip="Enter todo", key = "todo")
add_button = FSG.Button("Add")

window = FSG.Window("Gimu",
                    layout = [[label], [input_box, add_button]],
                    font = ('Helvetica', 15))
while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = get_todos()
            todos.append(values["todo"] + "\n")
            add_button.text = "Add"
            write_todos(todos)
        case FSG.WIN_CLOSED:
            break
window.close()
