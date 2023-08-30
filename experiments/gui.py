import function
import PySimpleGUI as sg
import time

sg.theme("DarkAmber")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todos(), key='todos',
                      enable_events=True, size=[45, 15])
edit_button = sg.Button("Edit")
remove_buton = sg.Button("Remove")
exit_Button = sg.Button("Exit")


window = sg.Window("My Todo App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, remove_buton],
                           [exit_Button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%d %b %y  %H:%M:%S"))

    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]

                new_todo = values['todo']

                todos = function.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                function.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("select a value")


        case "Remove":
            try:
                todo_to_remove = values['todos'][0]
                todos = function.get_todos()
                todos.remove(todo_to_remove)
                function.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                print("select a value")

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()