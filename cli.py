# TO DO learning application
# programmed by Sir. Andrew Gotham
# Copyright Sir Andrew Gotham, 2025
# https://github.com/SirAndrewGotham
# encoding: utf-8
"""
This is a scholar To-do application written in Python.
Initially developed as a command-line program, it might eventually grow
to the one having Desktop, Web and Mobile interfaces/implementations.
All in all, nothing special, just usual and trivial staff.
I am learning on it! :)
"""

import time
from functions import check_if_number, check_exists, get_todos, write_todos

now = time.strftime('%b %d, %Y %H:%M:%S')
print(f"Today is {time.strftime('%b %d, %Y %H:%M:%S')}")
# just for fun user prompt with commands extracted to a variable
user_prompt = f'Please type "add", "show", "edit", "complete", "help" or "exit" command. : '

# infinite loop, remember to exit at some point! :)
while True:
    # take user input and strip out [possible] empty spaces, then convert to lower case
    user_action = input(user_prompt).strip()
    # convert command at the beginning to lower case to prevent command mistyping
    user_action = user_action[:user_action.find(' ')].lower() + user_action[user_action.find(' '):]

    # redirect user to a chosen action or warn about wrong command
    if user_action.startswith("add") or user_action.startswith("new"):
        if user_action[4:] == '':
            todo = input("Enter a todo: ") + "\n"
        else:
            todo = user_action[4:] + "\n"

        with open('todos.txt', 'a') as file:
            file.writelines(todo)
    elif user_action.startswith("show") or user_action.startswith("list"):
        # show to-dos list
        print("Your todos so far:")

        todos = get_todos()

        # using the same for loop as before to be able to format output to the likings
        # list comprehension to remove excessive carrier return at the end
        # won;t use it here in favor of stripping elements directly in the for loop
        # todos = [item.strip('\n') for item in todos]
        for index, element in enumerate(todos):
            print(f"{index+1}. {element.strip('\n')}")
    elif user_action.startswith("edit") or user_action.startswith("change"):
        # FIRST, get number after EDIT command, if exists, then check
        if user_action[5:] == '':
            # ask user about to-do to edit and take the input
            n = input("Which one? Give me the number of a todo: ")
        else:
            n = user_action[5:]

        # verify that the input is of type int
        # if user input is integer, goon with editing, else break with appropriate notification
        if check_if_number(n):
            n = int(n)
            # make it 1 number less due to indexes starting at 0
            num = int(n)-1
        else:
            print("I can accept numbers only for editing todo items. Please try again.")
            continue
        # verify existence of the requested to-do
        if check_exists(n):
            todos = get_todos() # get them from file
                # notice to the user, what is being edited
            print(f"You are editing todo:\n{num+1}. {todos[num].strip('\n')}\n(todo number is not a part of your todo)")
            # prompt for a new to-do content
            new_text = input("What it should be now? ")
            # replace old to-do with the new one
            todos[num] = new_text + '\n'

            # write changes to the file
            write_todos(todos_local=todos)

            print(f"Todo {num+1} changed successfully")
        else: # if requested to-do # does not exist
            print(f"There's no todo with the number {num+1}. Please try again.")
            continue
    elif user_action.startswith("complete"):
        # FIRST, get number after the COMPLETE command, if exists, then check
        if user_action[9:] == '':
            # ask user about to-do to complete and take the input
            n = input(f"Which one todo you want to mark as read and delete from the list?\nPlease give me the number of a todo: ")
        else:
            n = user_action[9:]

        if check_if_number(n):
            n = int(n)
            # make it 1 number less due to indexes starting at 0
            index = int(n)-1
        else:
            print("I can accept numbers only to complete todos. Please try again.")
            continue
        if check_exists(n):
            todos = get_todos()
            todo_to_remove = todos[index]

            confirm = input(f"Please type 'yes' (without quotes) to confirm that you really want to delete todo:\n{todos[index].strip('\n')}\nYou won't be able to restore it other then by typing again. > ").lower().strip()
            if confirm == "yes":
                print(f"You have just completed your todo\n{todo_to_remove.strip('\n')}\nIt has been successfully deleted from your todos list.")
                todos.pop(n-1)

                write_todos(todos_local=todos)
            else:
                print("You didn't confirm by typing 'yes' (without quotation marks), nothing has been deleted from your todos list.")
            continue
        else: # if requested to-do # does not exist
            print(f"There's no todo with the number {n}. Please try again.")
            continue
    elif user_action == "help":
        print()
        print(
            """
            The program accepts several commands typed in exactly and performs corresponding actions:
            - "add" or "new": to create new todo
            - "show" or "list": to display a list of existing todos
            - "edit": to edit an existing todo
            - "complete": to complete a todo and delete it from the list
            - "help": this help
            - "exit": to interrupt execution and exit the program.
            You can add new items and edit or complete existing ones immediately
            by typing them right after the "add", "edit" or "complete" command, all in one line,
            like so: "add New todo" or "edit 7" (for example).
            """)
        print()
        continue
    # if a user chooses to exit
    elif user_action.startswith("exit"):
        print("Goodbye!")
        break
    # if a user types an unsupported command
    else:
        print('Wrong input, expected are "add", "show" or "exit", please try again.')

