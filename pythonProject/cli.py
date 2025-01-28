import functions
#import time

while True:
    #current_time = time.strftime("%b %d, %Y %H:%M:%S")
    #print(current_time)
    user_action = input("Choose if you want to add, show, edit ,complete or exit:")
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4::].title() + '\n'


        todos = functions.get_todo()

        todos.append(todo)

        functions.write_todo(todos)
    elif user_action.startswith('show'):
        todos = functions.get_todo()

        new_todos=[]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1} :- {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5::])
            number =  number - 1

            todos = functions.get_todo('todo_list.txt')

            new_todo = input("Enter new to-do:")
            todos[number] = new_todo.title() + '\n'
            functions.write_todo(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todo()
            number = int(user_action[9::])
            complete_todo = todos[number-1]



            index=number-1
            removed_todo = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todo(todos)

            print(f"{removed_todo} is completed")

        except IndexError:
            print("There is no todo with that number")
            continue

        except ValueError:
            print("Enter todo number and not  the todo name")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid. Please enter a valid command")

print("Thank you")