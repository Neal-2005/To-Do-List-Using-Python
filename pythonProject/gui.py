import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkGreen7")


clock_ = sg.Text("", key = "clock")
label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter To-Do", key = "todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values = functions.get_todo(), key = 'todos',
                      enable_events=True, size=[45,10])
complete_button = sg.Button("Complete")

exit_button  = sg.Button("Exit")
window = sg.Window("To-Do App",
                   layout=[[clock_],
                           [label] ,
                           [input_box, add_button],
                           [list_box,edit_button],
                           [complete_button,exit_button]],
                   font=("Helvetica", 20), finalize=True)
try:
    while True:

        window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
        event,value = window.read(timeout=200)



        match event:
            case 'Add':
                todos = functions.get_todo()
                new_todo = value["todo"] + "\n"
                todos.append(new_todo)
                functions.write_todo(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = "")
            case 'todos':
                window['todo'].update(value = value['todos'][0])

            case 'Edit':
                try:
                    todo_to_edit = value['todos'][0]
                    new_todo = value['todo']
                    todos = functions.get_todo()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todo(todos)
                    window['todos'].update(values = todos)
                except IndexError:
                    sg.popup("Select item first", font = ("Helvetica", 20))


            case 'Complete':
                try:
                    todo_to_complete = value['todos'][0]
                    todos = functions.get_todo()
                    todos.remove(todo_to_complete)
                    functions.write_todo(todos)
                    window['todos'].update(values = todos)
                    window['todo'].update(value = "")
                except IndexError:
                    sg.popup("Select item first", font=("Helvetica", 20))

            case 'Exit':
                break
            case sg.WIN_CLOSED:
                break
except IndexError:
    sg.popup("Enter todo in the list")



#window.close()
