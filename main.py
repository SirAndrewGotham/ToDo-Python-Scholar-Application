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

# just for fun user prompt extracted to a variable
user_prompt = 'Type "add", "show", "edit", "complete" or "exit": '

# initiate empty todos list
todos = []

# infinite loop, do not forget to exit! :)
while True:
    # take user input and strip out [possible] empty spaces, then convert to lower case
    user_action = input(user_prompt).strip().lower()

    # redirect user to a chosen action or warn about wrong command
    match user_action:
        # add new todo
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            # show todos list
            print("Your todos so far:")
            for index, element in enumerate(todos):
                print(f"{index+1}. {element}")
        case "edit":
            # ask user about to-do to edit and take the input
            n = input("Which one? Give me the number of a todo: ")
            # # verify that the input is of type int
            # try:
            #     val = int(n)
            # except ValueError:
            #     # skip the action if input is not an integer with corresponding notice
            #     print("I can accept numbers only. Please try again.")
            #     continue
            int_verification = check_if_number(n)
            if int_verification == True:
                num = int(n)-1
            else:
                print("I can accept numbers only. Please try again.")
                continue
            # if input is integer all right, convert it into integer explicitly
            # make it 1 number less due to indexes starting at 0
            # num = int(n)-1
            # check if inserted number corresponds to an existing index
            if 0 <= num < len(todos):
                print(f"You are editing todo:\n{num+1}. {todos[num]}\n(todo number is not a part of your todo)")
                todos[num] = input("What it should be now? ")
            else:
                # if inserted number has no corresponding index, notify user and skip action
                print(f"There's no todo with the number {num}. Please try again.")
                continue
        # mark as complete to delete a todo
        case 'complete':
            continue
        # if user chooses to exit
        case 'exit':
            print("Goodbye!")
            break
        # if user types an unsupported command
        case _:
            print('Wrong input, expected are "add", "show" or "exit", please try again.')

