"""
Program functions moved out of the main program for the DRY and organizational purposes.
"""

FILEPATH = 'todos.txt'

# functions
def check_if_number(n):
    """ Check if the requested n is a number and return True if so or False otherwise for further processing """
    try:
        val = int(n)
        return True
    except ValueError:
        return False

# a function to verify that requested todo exists
def check_exists(n):
    """ Check if requested index exists in the file returning True if it does and False otherwise for a corresponding further processing """
    file = open(FILEPATH, 'r')
    length = len(file.readlines())
    file.close()
    # check if the number provided corresponds to an existing index
    if 0 < n <= length:
        return True
    else:
        return False

def get_todos(filepath=FILEPATH):
    """ Returns a list of all todos in the file specified defaulting to todos.txt in case filename is not provided. """
    with open(filepath, 'r') as file_local:
        file_todos = file_local.readlines()
    return file_todos

def write_todos(todos_local, filepath=FILEPATH):
    """ Writes todos to the file list provided as a parameter to the file and returns nothing.
     Filepath defaults to todos.txt but can be provided as a parameter if something else is desired. """
    with open(filepath, 'w') as file:
        file.writelines(todos_local)
