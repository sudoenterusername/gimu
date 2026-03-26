from functions import *
import FreeSimpleGUI as FSG

label = FSG.Text("todo")
input_box = FSG.InputText(tooltip="Enter todo", key = "todo")
add_button = FSG.Button("Add")
list_box = FSG.Listbox(values = get_todos(), key = "todos",
                       enable_events= True, size = (45, 10))
edit_button = FSG.Button("Edit")

window = FSG.Window("Gimu",
                    layout = [[label],
                              [input_box, add_button],
                              [list_box, edit_button]],
                    font = ('Helvetica', 15))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = get_todos()
            todo = values["todo"] + "\n"
            todos.append(todo)
            write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"]
            todos = get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case FSG.WIN_CLOSED:
            break
window.close()
