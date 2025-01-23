import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key = "todo")
add_button = sg.Button("Add")

window = sg.Window("To-Do App",
                   layout=[[label] ,[input_box, add_button]],
                   font=("Helvetica", 20))

while True:

    event,value = window.read()
    print(event)
    print(value)
    match event:
        case 'Add':
            todos = functions.get_todo()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todo(todos)

        case sg.WIN_CLOSED:
            break


window.close()
