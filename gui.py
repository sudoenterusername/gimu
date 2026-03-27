from functions import *
import FreeSimpleGUI as FSG
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

FSG.theme("GreenMono")

clock = FSG.Text("", key = "clock")
label = FSG.Text("Gimu")
input_box = FSG.InputText(tooltip="Enter todo", key = "todo")
add_button = FSG.Button("Add")
list_box = FSG.Listbox(values = [line.strip() for line in get_todos()], key = "todos",
                       enable_events= True, size = (45, 10))
edit_button = FSG.Button("Edit")
complete_button = FSG.Button("Complete")
exit_button = FSG.Button("Exit")

window = FSG.Window("Gimu",
                    layout = [[clock],
                              [label],
                              [input_box, add_button],
                              [list_box, edit_button, complete_button],
                              [exit_button]],
                    font = ('Helvetica', 15))
while True:
    event, values = window.read(timeout=1000)
    if event == FSG.WIN_CLOSED:
        break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = get_todos()
            todo = values["todo"] + "\n"
            todos.append(todo)
            write_todos(todos)
            todos = [line.strip() for line in todos]
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = [line.strip() for line in get_todos()]
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos([line + "\n" for line in todos])
                window["todos"].update(values=todos)
            except IndexError:
                FSG.popup("Select an item to edit.", font = ('Helvetica', 15))
        case "Complete":
            try:
                todos = [line.strip() for line in get_todos()]
                todo_to_complete = values["todos"][0]
                todos.remove(todo_to_complete)
                write_todos([line + "\n" for line in todos])
                window["todos"].update(values=todos)
                window["todo"].update(value = "")
            except IndexError:
                FSG.popup("Select an item to complete.", font=('Helvetica', 15))
        case "todos":
            try:
                window["todo"].update(value=values["todos"][0])
            except IndexError:
                FSG.popup("Add an item to select.", font=('Helvetica', 15))
        case "Exit":
            break
window.close()