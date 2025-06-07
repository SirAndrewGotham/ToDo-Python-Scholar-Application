import time

import functions
import re
import FreeSimpleGUI as sg

# Choose a Theme for the Layout
sg.theme('DarkTeal9')

clock = sg.Text("", key="clock")
label = sg.Text("Type in your to-do or pick one from the list below for editing or completing")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[65, 10])
add_button = sg.Button("Add new todo", key="add")
save_button = sg.Button("Save changes", key="save")
complete_button = sg.Button("Complete todo", key="complete")
close_button = sg.Button("Close")

layout = [
    [clock],
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
    event, values = window.read(timeout=200)
    window["clock"].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    # development printouts:
    # print(1, event)
    # print(2, values)
    # print(3, values["todos"])
    # print(4, values["todo"])
    match event:
        case "add":
            '''
            Using if-else here as I want to block inputs with any number of empty spaces, rather then just no input at all as in case of try-except seen in the "complete" case, where there is no input field used
            '''
            if values['todo'].strip(' ') == '':
                sg.popup("Please write something meaningful. Empty todos are not a way to go.", font=("Helvetica", 20))
            else:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
        case "save":
            '''
            strip out duplicate while spaces using "re" library, get rid of the line breaks (in the middle of the file if any exists (old strings read from files have those), and add new line break at the end, then save to the file
            '''
            if values['todo'].strip(' ') == '':
                sg.popup("Please write something meaningful. Empty todos are not a way to go.", font=("Helvetica", 20))
            else:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = re.sub(' +', ' ', new_todo.replace('\n', ' ').replace('\r', '')) + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
        case "complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a todo to complete first.", font=("Helvetica", 20))
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Close":
            break
        case sg.WIN_CLOSED:
            break

window.close()
