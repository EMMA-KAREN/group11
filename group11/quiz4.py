# Question 4

# function to check for the maximum value from the user input list
def find_max():
    user_input = []
    counter = 1

    # while loop to collect the user input and append it in a list
    while len(user_input) < 5:

        number = int(input(f"Enter number {counter} : "))
        user_input.append(number)
        counter += 1

    # finding the maximum value from the list using the built-in max function in Python and printing it to the console.
    max_number = max(user_input)
    print(f"The maximum value is : {max_number}")

find_max()
