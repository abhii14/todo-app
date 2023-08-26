# from function import get_todos, write_todos alt for line 2
import function
import time
time = time.strftime("%d %b %y  %H:%M:%S")
print("date and time is -", time)


todos = []
while True:
    user_action = input("type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        # file = open('todo.txt', 'r')
        # todos = file.read lines(todos)
        # file.close() -- alternative of line 14

        # with open('todo.txt', 'r') as file:
        # todos = file.read lines() alt of line 21 without def fun.

        todos = function.get_todos(filepath='todo.txt')

        todos.append(todo + '\n')

        # file = open('todo.txt', 'w')
        # file.writelines(todos)
        # file.close() -- alternative of line 16

        # with open('todo.txt', 'w') as file:
        # file.writelines(todos)

        function.write_todos(filepath="todo.txt", todos_arg=todos)


    elif user_action.startswith("show"):

        todos = function.get_todos()

        print(todos)

        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        for index, item in enumerate(new_todos):
            print(f"{index + 1}-{item}")
        print(f"length is {index + 1}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[4:])
            print(number)

            number = number - 1

            todos = function.get_todos()

            new_todo = input("enter new todo")
            todos[number] = new_todo + '\n'

            function.write_todos(todos)

        except ValueError:
            print("your command is not valid")
        except IndexError:
            print("not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = function.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            function.write_todos(todos)

            message = f"TODO '{todo_to_remove}' was removed from the list."
            print(message)

        except IndexError:
            print("item is not present with that number")
        except ValueError:
            print("not valid")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("wrong")
print("bye")
