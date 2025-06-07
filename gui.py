import functions
import re
import FreeSimpleGUI as sg

label = sg.Text("Type in your to-do or pick one from the list below for editing or completing")
# pick_label = sg.Text("Pick a todo from the list below for editing or completing, please.")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
add_button = sg.Button("Add new todo")
save_button = sg.Button("Save changes")
complete_button = sg.Button("Complete todo")
close_button = sg.Button("Close")

layout = [
    [label],
    [input_box],
    [add_button, save_button, complete_button],
    # [pick_label],
    [list_box],
    [close_button]
]

window = sg.Window("My Scholar Python To-Do App",
                    layout=layout,
                    font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todos"])
    print(4, values["todo"])
    match event:
        case "Add new todo":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Save changes":
            '''
            strip out duplicate while spaces using "re" library, get rid of the line breaks (in the middle of the file if any exists (old strings read from files have those), and add new line break at the end, then save to the file
            '''
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = re.sub(' +', ' ', new_todo.replace('\n', ' ').replace('\r', '')) + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete todo":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todo_to_remove = todos.index(todo_to_complete)
            todos.pop(todo_to_remove)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Close":
            break
        case sg.WIN_CLOSED:
            break

window.close()
