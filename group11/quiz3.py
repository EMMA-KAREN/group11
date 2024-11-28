# The program accepts two integers from the user, ensures the range works irrespective of the order of the inputs.
# It iterates through all numbers in the range,skips numbers divisible by 7 using the modulo operator %.
# It prints the valid numbers in a single line, separated by spaces.
def print_numbers_skipping_sevens(start, end):
    # Adjust the range to ensure it works regardless of input order
    if start > end:
        start, end = end, start

    print(f"Numbers between {start} and {end} (excluding those divisible by 7):")
    for number in range(start, end + 1):
        if number % 7 != 0:
            print(number, end=" ")
    print()  # Print a newline at the end

# Get user input
try:
    start = int(input("Enter the first number: "))
    end = int(input("Enter the second number: "))
    print_numbers_skipping_sevens(start, end)
except ValueError:
    print("Please enter valid integers.")
