import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in your to-do")
input_box = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")
# edit_button =
# complete_button =

windows = sg.Window("My Scholar Python To-Do App", layout=[[label, input_box, add_button]])
windows.read()
windows.close()
