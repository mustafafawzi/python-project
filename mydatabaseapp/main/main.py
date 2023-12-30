
import os
import sys
import datetime
from pathlib import Path  # Import Path from pathlib for handling paths
from colorama import Fore, Style, init


# from mydatabaseapp.database import Database
from mydatabaseapp.database.database import Database
from mydatabaseapp.report_generator.report_generator import ReportGenerator


# Initialize colorama for colored output
init(autoreset=True)

def print_welcome_message():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print(f"\n{Fore.BLUE}Welcome to the Command-Line Database Application!{Style.RESET_ALL}")
    print("\nBasic Instructions:")
    print("- Enter the command number to perform an action.")
    print("- Type '-h' or '--help' to display the help message.")
    print("- Follow on-screen prompts for additional inputs.")
    print("- Use '6' to execute custom SQL queries.")
    print("- Use '8' to generate reports in CSV or Excel format.")
    print("- Type '9' to exit the program.\n")
    
    # Example for custom queries
    print("Example for Custom Query (Command 6):")
    print("You can enter SQL queries to retrieve specific data from the database.")
    print("For example, you can try the following query:")
    print(f"{Fore.GREEN}SELECT * FROM users WHERE email LIKE '%gmail.com%';{Style.RESET_ALL}")
    print("This query fetches all users with email addresses containing 'gmail.com'.\n")


def print_commands():
    print(f"\n{Fore.BLUE}Available Commands:{Style.RESET_ALL}")
    print(f"1. {Fore.CYAN}Fetch all users{Style.RESET_ALL}")
    print(f"2. {Fore.CYAN}Insert a new user{Style.RESET_ALL}")
    print(f"3. {Fore.CYAN}Update user email{Style.RESET_ALL}")
    print(f"4. {Fore.CYAN}Delete a user{Style.RESET_ALL}")
    print(f"5. {Fore.CYAN}Fetch orders by user{Style.RESET_ALL}")
    print(f"6. {Fore.RED}Execute custom query{Style.RESET_ALL}")
    print(f"7. {Fore.RED}Display Application Info{Style.RESET_ALL}")
    print(f"8. {Fore.CYAN}Generator Report {Style.RESET_ALL}")
    print(f"9. {Fore.RED}Exit{Style.RESET_ALL}")

def execute_custom_query(db):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("\nTables:")
    tables = db.get_table_names()
    for table in tables:
        print(f"{table}")

    user_query = input(f"\nEnter your custom SQL query:{Fore.GREEN} ")
    result = db.execute_custom_query(user_query)
    
    if result is not None:
        print(f"\n{Fore.BLUE}Query Result:{Style.RESET_ALL}")
        for row in result:
            print(row)

    input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

def generate_report(db, format):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen

    if format not in ['csv', 'xlsx']:
        print(f"\n{Fore.RED}Invalid report format. Please choose 'csv' or 'excel'.{Style.RESET_ALL}")
        return

    tables = db.get_table_names()
    print("\nTables:")
    for table in tables:
        print(f"{table}")

    table_name = input(f"\nEnter the table name for the report:{Fore.GREEN} ")
    
    if table_name not in tables:
        print(f"\n{Fore.RED}Invalid table name. Please choose a valid table.{Style.RESET_ALL}")
        return

    # Create a 'report' folder if it doesn't exist
    report_folder = Path("report")
    report_folder.mkdir(exist_ok=True)

    # Include current datetime in the filename for uniqueness
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = report_folder / f"report_{table_name}_{current_datetime}.{format}"

    if format == 'csv':
        data = db.fetch_all(table_name)
        ReportGenerator.generate_csv(data, filename)
        print(f"\n{Fore.GREEN}CSV report generated successfully!{Style.RESET_ALL}")
    elif format == 'excel' or format == 'xlsx':
        data = db.fetch_all(table_name)
        ReportGenerator.generate_excel(data, filename)
        print(f"\n{Fore.GREEN}Excel report generated successfully!{Style.RESET_ALL}")

    input("\nPress Enter to continue...")  # Wait for user input before clearing the screen
def display_info(db):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    tables = db.get_table_names()
    operations = 6  # Update this count if more operations are added in the future
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    info_text = f" Application Information:\n Number of Tables: {len(tables)}\n Number of Operations: {operations}\n Date and Time: {date_time} "
    
    box_width = max(len(line) for line in info_text.splitlines()) + 4
    separator = "+" + "-" * (box_width - 2) + "+"

    print(f"\n{Fore.BLUE}{separator}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}|{Style.RESET_ALL}{info_text.center(box_width - 2)}{Fore.BLUE}|{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{separator}{Style.RESET_ALL}")

    input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

def display_help():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print(f"\n{Fore.BLUE}Command-Line Database Application Help:{Style.RESET_ALL}")
    print("\nUsage:")
    print("python main.py [options]")
    print("\nOptions:")
    print("-h, --help    : Display this help message")
    print("\nCommands:")
    print_commands()

# Instantiate the Database class
db_path = os.path.join("data", "app.db")
db = Database(db_path)

if len(sys.argv) > 1:
    if sys.argv[1] in ['-h', '--help']:
        display_help()






# Display welcome message
print_welcome_message()


while True:
    # os.system('cls' if os.name == 'nt' else 'clear')  # Do not clear screen here
    # print_commands()

    user_input = input(f"\n{Fore.GREEN}Enter the command number (or type '-h' for help):{Style.RESET_ALL} ")

    if user_input in ['-h', '--help']:
        display_help()
        continue

    if user_input == "1":
        users = db.fetch_all("users")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(f"\n{Fore.BLUE}All Users:{Style.RESET_ALL}")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    # ... (rest of the commands)
    elif user_input == "2":
        name = input(f"{Fore.GREEN}Enter user name:{Style.RESET_ALL} ")
        email = input(f"{Fore.GREEN}Enter user email:{Style.RESET_ALL} ")
        db.insert_user(name, email)
        print(f"\n{Fore.GREEN}User inserted successfully!{Style.RESET_ALL}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    elif user_input == "3":
        user_id = input(f"{Fore.GREEN}Enter user ID:{Style.RESET_ALL} ")
        new_email = input(f"{Fore.GREEN}Enter new email:{Style.RESET_ALL} ")
        db.update_user_email(user_id, new_email)
        print(f"\n{Fore.GREEN}User email updated successfully!{Style.RESET_ALL}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    elif user_input == "4":
        user_id = input(f"{Fore.GREEN}Enter user ID to delete:{Style.RESET_ALL} ")
        db.delete_user(user_id)
        print(f"\n{Fore.GREEN}User deleted successfully!{Style.RESET_ALL}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    elif user_input == "5":
        user_id = input(f"{Fore.GREEN}Enter user ID to fetch orders:{Style.RESET_ALL} ")
        orders = db.fetch_orders_by_user(user_id)
        print(f"\n{Fore.BLUE}Orders for User:{Style.RESET_ALL}")
        for order in orders:
            print(f"Order ID: {order[0]}, Product: {order[2]}, Quantity: {order[3]}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    elif user_input == "6":
        execute_custom_query(db)

    elif user_input == "7":
        display_info(db)

    elif user_input == "8":
        format = input(f"\n{Fore.GREEN}Enter report format (csv or xlsx for excel):{Style.RESET_ALL} ")
        generate_report(db, format)

    elif user_input == "9":
        print(f"\n{Fore.RED}Exiting the program. Goodbye!{Style.RESET_ALL}")
        break

    else:
        print(f"\n{Fore.RED}Invalid command. Please enter a valid command number.{Style.RESET_ALL}")

    # os.system('cls' if os.name == 'nt' else 'clear')  # Do not clear screen here
    
sys.exit(1)