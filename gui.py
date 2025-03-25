import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

sg.theme("LightPurple")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo_inputbox")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

button_column = sg.Column([[edit_button], [complete_button]])
# each list of the outer list layout represents a row.
# so, when placed in the same list, they will be shown in the same row.
layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, button_column],
          [exit_button]]

window = sg.Window('My To-Do App',
                   layout=layout,
                   font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo_inputbox'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)  # so that the list is updated with new list

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo_inputbox']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select and item first.', font=('Helvetica', 20))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo_inputbox'].update(value='')
            except IndexError:
                sg.popup('Please select and item first.', font=('Helvetica', 20))

        case 'Exit':
            break
        case 'todos':  # when the user selects on sth in the list
            window['todo_inputbox'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
window.close()
