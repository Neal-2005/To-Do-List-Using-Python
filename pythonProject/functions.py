def get_todo(filepath = "todo_list.txt"):
    """
        Reading text file and return list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todo(todos_arg,filepath = "todo_list.txt"):
    """
        Write to-do items list in text file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
