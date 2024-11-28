
def main_menu():
    """Display the main menu and navigate to submenus."""
    while True:  # Infinite loop to continuously show the main menu
        print("\nSIM 1")  # Display "SIM 1" as the header
        print("1. Safaricom")  # Option 1 for Safaricom
        print("2. M-PESA")  # Option 2 for M-PESA
        choice = input("Enter your choice (1 or 2, or 'q' to quit): ").strip()  # Prompt the user for input

        if choice == "1":  # If the user chooses Safaricom
            print("\nYou selected: Safaricom")  # Confirm the user's selection
        elif choice == "2":  # If the user chooses M-PESA
            mpesa_menu()  # Call the M-PESA submenu
        elif choice.lower() == "q":  # If the user chooses to quit
            print("Exiting. Thank you!")  # Display exit message
            break  # Exit the loop to terminate the program
        else:  # Handle invalid input
            print("Invalid choice. Please try again.")  # Prompt the user to enter a valid choice

def mpesa_menu():
    """Display the M-PESA menu and navigate to submenus."""
    while True:  # Infinite loop to continuously show the M-PESA menu
        print("\nSIM 1 - M-PESA")  # Display "SIM 1 - M-PESA" as the header
        print("1. Send Money")  # Option 1 for Send Money
        print("2. Withdraw Cash")  # Option 2 for Withdraw Cash
        print("3. Buy Airtime")  # Option 3 for Buy Airtime
        print("4. Loans and Savings")  # Option 4 for Loans and Savings
        print("5. Lipa na M-PESA")  # Option 5 for Lipa na M-PESA
        print("6. My Account")  # Option 6 for My Account
        print("b. Back to Main Menu")  # Option to go back to the main menu
        choice = input("Enter your choice (1-6, or 'b' to go back): ").strip()  # Prompt the user for input

        if choice == "1":  # If the user selects Send Money
            send_money()  # Call the Send Money submenu
        elif choice == "2":  # If the user selects Withdraw Cash
            print("\nYou selected: Withdraw Cash")  # Confirm the user's selection
        elif choice == "3":  # If the user selects Buy Airtime
            print("\nYou selected: Buy Airtime")  # Confirm the user's selection
        elif choice == "4":  # If the user selects Loans and Savings
            print("\nYou selected: Loans and Savings")  # Confirm the user's selection
        elif choice == "5":  # If the user selects Lipa na M-PESA
            print("\nYou selected: Lipa na M-PESA")  # Confirm the user's selection
        elif choice == "6":  # If the user selects My Account
            print("\nYou selected: My Account")  # Confirm the user's selection
        elif choice.lower() == "b":  # If the user selects to go back
            break  # Exit the loop to return to the main menu
        else:  # Handle invalid input
            print("Invalid choice. Please try again.")  # Prompt the user to enter a valid choice

def send_money():
    """Handle the Send Money menu option."""
    while True:  # Loop to continuously prompt for a valid phone number
        phone_number = input("\nEnter Phone Number (10-13 digits, starting with 07): ").strip()  # Prompt the user for a phone number

        # Validate the phone number
        if len(phone_number) in range(10, 14) and phone_number.isdigit() and phone_number.startswith("07"):
            # If the phone number meets the criteria, proceed
            print(f"\nPhone number {phone_number} accepted.")  # Confirm the phone number
            confirm = input("Confirm to send money to this number? (y/n): ").strip().lower()  # Ask for confirmation
            if confirm == "y":  # If the user confirms
                print("Money sent successfully!")  # Display success message
                break  # Exit the loop
            elif confirm == "n":  # If the user cancels
                print("Transaction canceled.")  # Display cancellation message
                break  # Exit the loop
            else:  # Handle invalid confirmation input
                print("Invalid confirmation. Transaction aborted.")  # Display an error message
                break  # Exit the loop
        else:  # If the phone number is invalid
            print("Invalid phone number. Please try again.")  # Prompt the user to enter a valid phone number

# Start the program
if __name__ == "__main__":
    main_menu()  # Call the main menu to start the program
