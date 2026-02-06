

def show_main_menu():
    print("\nWelcome to the Timebox Creator!")
    print("Please select an option:")
    print("(1) Create a new timebox")
    print("(2) Create a new template")
    print("(3) Load a template")
    print("(4) Exit")
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
    return choice
