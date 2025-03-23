FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Reads a text file and returns a list of to-do items."""
    with open(filepath, 'r') as file_local:  # when using with, you don't need to close the file
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):  # default parameter should come after non-default one
    """ Writes to-do items in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# print(__name__)
if __name__ == '__main__':  # this script is true when this file is executed directly
    print('Hello')
