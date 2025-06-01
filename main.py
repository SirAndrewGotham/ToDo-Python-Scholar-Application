# TO DO learning application
# programmed by Sir. Andrew Gotham
# Copyright Sir Andrew Gotham, 2025
# https://github.com/SirAndrewGotham

from functions import check_if_number, check_exists

# just for fun user prompt with commands extracted to a variable
user_prompt = 'Type "add", "show", "edit", "complete" or "exit": '

# infinite loop, do not forget to exit! :)
while True:
    # take user input and strip out [possible] empty spaces, then convert to lower case
    user_action = input(user_prompt).strip().lower()

    # redirect user to a chosen action or warn about wrong command
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # with open('todos.txt', 'r') as file:
            #     todos = file.readlines()
            #
            # todos.append(todo)
            #
            # with open('todos.txt', 'w') as file:
            #     file.writelines(todos)
            with open('todos.txt', 'a') as file:
                file.writelines(todo)
        case 'show':
            # show todos list
            print("Your todos so far:")

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # using the same for loop as before to be able to format output to the likings
            # list comprehension to remove excessive carrier return at the end
            # won;t use it here in favor of stripping elements directly in the for loop
            # todos = [item.strip('\n') for item in todos]
            for index, element in enumerate(todos):
                print(f"{index+1}. {element.strip('\n')}")
        case "edit":
            # ask user about to-do to edit and take the input
            n = input("Which one? Give me the number of a todo: ")
            # verify that the input is of type int
            # if user input is integer, goon with editing, else break with appropriate notification
            if check_if_number(n) == True:
                n = int(n)
                # make it 1 number less due to indexes starting at 0
                num = int(n)-1
            else:
                print("I can accept numbers only. Please try again.")
                continue
            # verify existence of the requested to-do
            if check_exists(n) == True:
                with open('todos.txt', 'r') as file:
                    todos = file.readlines() # read the "list"
                    # notice to the user, what is being edited
                print(f"You are editing todo:\n{num+1}. {todos[num].strip('\n')}\n(todo number is not a part of your todo)")
                # prompt for a new to-do content
                new_text = input("What it should be now? ")
                # replace old to-do with the new one
                todos[num] = new_text + '\n'

                # write changes to the file
                with open('todos.txt', 'w') as file:
                    file.writelines(todos)
            else: # if requested to-do # does not exist
                print(f"There's no todo with the number {num+1}. Please try again.")
                continue
        case 'complete':
            n = input(f"Which one todo you want to mark as read and delete from the list?\nPlease give me the number of a todo: ")
            if check_if_number(n) == True:
                n = int(n)
                # make it 1 number less due to indexes starting at 0
                num = int(n)-1
            else:
                print("I can accept numbers only. Please try again.")
                continue
            # TODO - existance verification via function
            if check_exists(n) == True:
                with open('todos.txt', 'r') as file: # open file for reading
                    todos = file.readlines()

                confirm = input(f"Please type 'yes' (without quotes) to confirm that you really want to delete todo:\n{todos[n-1].strip('\n')}\nYou won't be able to restore it other then by typing again. > ").lower().strip()
                if confirm == "yes":
                    print(f"You have just completed your todo\n{todos[n-1].strip('\n')}\nIt has been successfully deleted from your todos list.")
                    todos.pop(n-1)
                    with open('todos.txt', 'w') as file:
                        file.writelines(todos)
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

