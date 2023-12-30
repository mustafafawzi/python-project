# main.py
from database import Database

db = Database("app.db")

# Create tables or perform other database initialization steps

while True:
    user_input = input("Enter a command: ")

    if user_input.lower() == "select_all_users":
        users = db.select_all_users()
        for user in users:
            print(user)

    # Add other command handling as needed

    elif user_input.lower() == "exit":
        break