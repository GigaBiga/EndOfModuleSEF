import os

def constructTable():
    headers =("Reference","Title", "Description", "Category", "Status", "Group Assigned", "Priority", "Environment", "Requestor") 
    headerSizes = (11,14,54,16, 15, 18, 12, 15, 25)
    table = "|"
    for i in range(len(headers)):
        space = int((headerSizes[i] - len(headers[i]))/2)
        table += (" " * space) + headers[i] + (" " * space)+"|"
    return table

# Function used to clear the console. Checks what operating system user is using and uses appropiate clear command
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clearConsole()
    print(constructTable())
    # Main menu options stored in variable
    mainMenu = ""
    # Creates a boolean variable to store whether the user wants to exit the program or not
    exit = False
    # If the exit variable is false (User has not typed in exit as a command) the appliaction will keep running
    while exit == False:
        #Takes the command from the user
        command = str(input("- "))
        #Checks if the command is exit and if it is sets exit to true, ending the loop
        if command.lower() == "exit":
            exit = True

if __name__ == '__main__':
    main()