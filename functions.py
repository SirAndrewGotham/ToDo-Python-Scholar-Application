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