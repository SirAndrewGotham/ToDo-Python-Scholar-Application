# a function to verify that user's input was an integer
def check_if_number(n):
    try:
        val = int(n)
        return True
    except ValueError:
        return False

# a function to verify that requested todo exists
def check_exists(n):
    file = open('todos.txt', 'r')
    length = len(file.readlines())
    file.close()
    # check if the number provided corresponds to an existing index
    if 0 < n <= length:
        return True
    else:
        return False

def get_todos():
    with open('todos.txt', 'r') as file_local:
        file_todos = file_local.readlines()
    return file_todos
