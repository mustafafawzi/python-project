# main.py

from database import Database
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

def print_commands():
    print(f"\n{Fore.BLUE}Available Commands:{Style.RESET_ALL}")
    print(f"1. {Fore.CYAN}Fetch all users{Style.RESET_ALL}")
    print(f"2. {Fore.CYAN}Insert a new user{Style.RESET_ALL}")
    print(f"3. {Fore.CYAN}Update user email{Style.RESET_ALL}")
    print(f"4. {Fore.CYAN}Delete a user{Style.RESET_ALL}")
    print(f"5. {Fore.CYAN}Fetch orders by user{Style.RESET_ALL}")
    print(f"6. {Fore.RED}Execute custom query{Style.RESET_ALL}")
    print(f"7. {Fore.RED}Exit{Style.RESET_ALL}")

def execute_custom_query(db):
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

# Instantiate the Database class
db = Database("app.db")

while True:
    print_commands()

    user_input = input(f"\n{Fore.GREEN}Enter the command number:{Style.RESET_ALL} ")

    if user_input == "1":
        users = db.fetch_all("users")
        print(f"\n{Fore.BLUE}All Users:{Style.RESET_ALL}")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    elif user_input == "2":
        name = input(f"{Fore.GREEN}Enter user name:{Style.RESET_ALL} ")
        email = input(f"{Fore.GREEN}Enter user email:{Style.RESET_ALL} ")
        db.insert_user(name, email)
        print(f"\n{Fore.GREEN}User inserted successfully!{Style.RESET_ALL}")

    elif user_input == "3":
        user_id = input(f"{Fore.GREEN}Enter user ID:{Style.RESET_ALL} ")
        new_email = input(f"{Fore.GREEN}Enter new email:{Style.RESET_ALL} ")
        db.update_user_email(user_id, new_email)
        print(f"\n{Fore.GREEN}User email updated successfully!{Style.RESET_ALL}")

    elif user_input == "4":
        user_id = input(f"{Fore.GREEN}Enter user ID to delete:{Style.RESET_ALL} ")
        db.delete_user(user_id)
        print(f"\n{Fore.GREEN}User deleted successfully!{Style.RESET_ALL}")

    elif user_input == "5":
        user_id = input(f"{Fore.GREEN}Enter user ID to fetch orders:{Style.RESET_ALL} ")
        orders = db.fetch_orders_by_user(user_id)
        print(f"\n{Fore.BLUE}Orders for User:{Style.RESET_ALL}")
        for order in orders:
            print(f"Order ID: {order[0]}, Product: {order[2]}, Quantity: {order[3]}")

    elif user_input == "6":
        execute_custom_query(db)

    elif user_input == "7":
        print(f"\n{Fore.RED}Exiting the program. Goodbye!{Style.RESET_ALL}")
        break

    else:
        print(f"\n{Fore.RED}Invalid command. Please enter a valid command number.{Style.RESET_ALL}")
