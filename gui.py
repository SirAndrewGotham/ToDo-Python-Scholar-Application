import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in your to-do")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
# edit_button =
# complete_button =
close_button = sg.Button("Close")

window = sg.Window("My Scholar Python To-Do App",
                    layout=[
                        [label, input_box, add_button],
                        [close_button]
                    ],
                    font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Close":
            break
        case sg.WIN_CLOSED:
            break

window.close()
