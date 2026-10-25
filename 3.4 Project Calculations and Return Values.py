from datetime import datetime
# Converts data based on the selected report type
def convertData(data, conversionType):

    if conversionType == "1":       # Temperature (F to C)
        return (data - 32) * 5/9
    elif conversionType == "2":     # Weight (lbs to kg)
        return data / 2.205
    elif conversionType == "3":     # Dimensions (in to cm)
        return data * 2.54 
    else:
        print("Invalid conversion type.")
        return None
# Gets user input
def getInput(conversionType):
    entries = int(input("How many entries are being entered? "))

    for i in range(entries):

        dateEntered = input("Enter the date: ")
        valueEntered = float(input("Enter a value: "))
# Call convertData and pass the value entered by the user. The function returns the converted value.

        convertedValue = convertData(valueEntered, conversionType)
        print(f'\nThe following was saved at {datetime.now()}:')
        print(f'Date: {dateEntered}')
        print(f'Original Value: {valueEntered}')
        print(f'Converted Value: {convertedValue:.2f}')
        
            

# Display the application title
print("Stealb9443's Excel Spreadsheet Automation Menu")
print("Choose a number from the following options")

# Store menu options in a list
menu_options = [
    "1. Input Data",
    "2. View Current Data",
    "3. Generate Report"
]

# Display menu options using a for loop
for option in menu_options:
    print(option)

# Get user's menu selection
choice = input("Enter your choice: ")

# Get current date and time
current_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")

# Validate the user's choice
if choice == "1": 
    print(f"You selected option {choice} at {current_time}")
    print("\nWhat type of data are you entering? ")
    print("1. Temperature")
    print("2. Weight")
    print("3. Dimensions")

    conversionType = input("Select an option: ")
    getInput(conversionType)
    
elif choice == "2":
    print("Error: The chosen functionality is not implemented yet")

elif choice == "3":

    print("\nGenerate Report")
    print("1. Temperature Report")
    print("2. Weight Report")
    print("3. Dimension Report")

    reportChoice = input("Select a report: ")

    if reportChoice == "1":
        print("Generating Temperature Report")

    elif reportChoice == "2":
        print("Generating Weight Report")

    elif reportChoice == "3":
        print("Generating Dimension Report")

    else:
        print("Error: Invalid report selection.")
else:
    print("Error: The chosen functionality is not implemented yet")


