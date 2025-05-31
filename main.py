# TO DO learning application
# programmed by Sir. Andrew Gotham
# Copyright Sir Andrew Gotham, 2025
# https://github.com/SirAndrewGotham

# a function to verify that user's input was an integer
def check_if_number(n):
    # verify that the input is of type int
    try:
        val = int(n)
        return True
    except ValueError:
        # skip the action if input is not an integer with corresponding notice
        # print("I can accept numbers only. Please try again.")
        # continue
        return False

# a function to verify that requested todo exists
def check_exists(n):
    # check if the number provided corresponds to an existing index
    if 0 <= num < len(todos):
        return True
    else:
        return False

# just for fun user prompt extracted to a variable
user_prompt = 'Type "add", "show", "edit", "complete" or "exit": '

# infinite loop, do not forget to exit! :)
while True:
    # take user input and strip out [possible] empty spaces, then convert to lower case
    user_action = input(user_prompt).strip().lower()

    # redirect user to a chosen action or warn about wrong command
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            # show todos list
            print("Your todos so far:")

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # using the same for loop as before to be able to format output to the likings
            for index, element in enumerate(todos):
                print(f"{index+1}. {element}", end='')
        case "edit":
            # ask user about to-do to edit and take the input
            n = input("Which one? Give me the number of a todo: ")
            # verify that the input is of type int
            # if user input is integer, goon with editing, else break with appropriate notification
            if check_if_number(n) == True:
                # make it 1 number less due to indexes starting at 0
                num = int(n)-1
            else:
                print("I can accept numbers only. Please try again.")
                continue
            # verify existance of the requested to-do
            if check_exists(n) == True:
                print(f"You are editing todo:\n{num+1}. {todos[num]}\n(todo number is not a part of your todo)")
                todos[num] = input("What it should be now? ")
            else:
                # if inserted number has no corresponding index, notify user and skip action
                print(f"There's no todo with the number {num+1}. Please try again. > ")
                continue
        case 'complete':
            n = input(f"Which one todo you want to mark as read and delete from the list?\nPlease give me the number of a todo: ")
            # TODO  - int verification via function
            n = int(n)-1 # compensation for the difference in numbers
            # TODO - existance verification via function
            confirm = input(f"Please type 'yes' (without quotes) to confirm that you really want to delete todo:\n{todos[n]}\nYou won't be able to restore it other then by typing again. > ").lower().strip()
            if confirm == "yes":
                print(f"You have just completed your todo\n{todos[n]}\nIt has been successfully deleted from your todos list.")
                todos.pop(n)
            else:
                print("You didn't confirm by typing 'yes' (without quotation marks), nothing has been deleted from your todos list.")
            continue
        # if user chooses to exit
        case 'exit':
            print("Goodbye!")
            break
        # if user types an unsupported command
        case _:
            print('Wrong input, expected are "add", "show" or "exit", please try again.')

