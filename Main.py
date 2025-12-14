from JsonInputProcessor import processJSON
from ConsoleInputProcessor import processConsoleInput

def main():
    """Prompt user to choose input method and process accordingly.
    
    Repeatedly prompts the user to select between JSON file input or console input
    until a valid choice is made. Then executes the appropriate processing function
    based on the user's selection.
    The function will continue to ask for input if the user enters anything other
    than 'json' or 'console' (case-insensitive).
    """
    while (userChoice := input("Do you have your input as JSON file or do you want type the input in the console? (JSON/CONSOLE): ").strip().lower()) not in ['json', 'console']:
        print("Invalid input. Please enter 'JSON' or 'CONSOLE'.")

    if userChoice == 'json':
        processJSON()
    else:
        processConsoleInput()

if __name__ == "__main__":
    main()
