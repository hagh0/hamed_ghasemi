# Declare a 2D array to store the options and sub-options
options = [
    ["1", "1.1", "0"],
    ["2", "2.1", "1"],
    ["3", "3.1", "1"],
    ["4", "4.1", "2"],
]

# Display the main menu
print("Main Menu:")
for i in range(len(options)):
    print(f"{i + 1}. {options[i][0]}")
print("0. Exit")

# Get the user's choice
choice = int(input("Enter your choice: "))

# Handle the user's choice
while choice != 0:
    # If the user's choice is valid, display the sub-options for the chosen option
    if 1 <= choice <= len(options):
        print(f"Sub-Menu for {options[choice - 1][0]}:")
        for j in range(1, len(options[choice - 1])):
            print(f"{j}. {options[choice - 1][j]}")

        # Get the user's choice for the sub-options
        sub_choice = int(input("Enter your choice: "))

        # If the user's choice for the sub-options is valid, display the sub-sub-options for the chosen sub-option
        if 1 <= sub_choice <= len(options[choice - 1]) - 1:
            print(f"Sub-Sub-Menu for {options[choice - 1][sub_choice]}:")
            for k in range(1, len(options[choice - 1])):
                print(f"{k}. {options[choice - 1][k + sub_choice]}")

            # Get the user's choice for the sub-sub-options
            sub_sub_choice = int(input("Enter your choice: "))

            # If the user's choice for the sub-sub-options is valid, print the chosen sub-sub-option
            if 1 <= sub_sub_choice <= len(options[choice - 1]) - 1:
                print(f"You have chosen {options[choice - 1][k + sub_sub_choice]}")
            else:
                print("Invalid choice")

        else:
            print("Invalid choice")

    else:
        print("Invalid choice")

    # Get the user's choice again
    choice = int(input("Enter your choice: "))

# Exit the program
print("Goodbye!")