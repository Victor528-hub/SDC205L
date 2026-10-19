from datetime import datetime

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
if choice == "1" or choice == "2" or choice == "3":
    print(f"You selected option {choice} at {current_time}")
else:
    print("Error: Invalid choice selected.")
