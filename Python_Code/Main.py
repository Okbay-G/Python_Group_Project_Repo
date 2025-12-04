from JsonInputProcessor import processJSON
from ConsoleInputProcessor import processConsoleInput

def main():
    while (userChoice := input("Do you have your input as JSON file or do you want type the input in the console? (JSON/CONSOLE): ").strip().lower()) not in ['json', 'console']:
        print("Invalid input. Please enter 'JSON' or 'CONSOLE'.")

    if userChoice == 'json':
        processJSON()
    else:
        processConsoleInput()

if __name__ == "__main__":
    main()
    

