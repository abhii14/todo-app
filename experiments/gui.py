import function
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todos(), key='todos',
                      enable_events=True, size=[45, 15])
edit_button = sg.Button("Edit")
remove_buton = sg.Button("Remove")
exit_Button = sg.Button("Exit")


window = sg.Window("My Todo App",
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button, remove_buton],
                           [exit_Button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]

            new_todo = values['todo']

            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window['todos'].update(values=todos)

        case "Remove":
            todo_to_remove = values['todos'][0]
            todos = function.get_todos()
            todos.remove(todo_to_remove)
            function.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Exit":
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()