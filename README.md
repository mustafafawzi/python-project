#Application Setup  # MyDatabaseApp

This is a command-line database application.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mustafafawzi/python-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd python-project
    ```

3. Create a virtual env (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual env:

    On Windows:

    ```bash
    .\venv\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source venv/bin/activate
    ```

5. Install dependencies:

    ```bash
    pip install .
    ```

## Usage

1. Run the application:

    ```bash
    mydatabaseapp
    ```

    This will execute the main functionality of the application.

## Uninstallation

1. Deactivate the virtual environment (if used):

    ```bash
    deactivate
    ```

2. Optionally, remove the virtual environment and the cloned repository.

## Notes

- Make sure you have Python 3.x installed.

#Not Required but if you want to work on your own sqlite
--------------------------------------------------------------------------
# Install if not installed sqlite3
  pip3 install --upgrade sqlite3 

if you want to have your own database from step 1 then follow following

  # Command
      sqlite3 app.db
     
     -- Create users table
     CREATE TABLE users (
         id INTEGER PRIMARY KEY,
         name TEXT,
         email TEXT
     );
     
     -- Insert sample users
     INSERT INTO users (name, email) VALUES
         ('John Doe', 'john.doe@example.com'),
         ('Jane Smith', 'jane.smith@example.com'),
         ('Bob Johnson', 'bob.johnson@example.com');
     
     -- Create orders table
     CREATE TABLE orders (
         id INTEGER PRIMARY KEY,
         user_id INTEGER,
         product TEXT,
         quantity INTEGER,
         FOREIGN KEY (user_id) REFERENCES users(id)
     );
     
     -- Insert sample orders
     INSERT INTO orders (user_id, product, quantity) VALUES
         (1, 'Product A', 2),
         (2, 'Product B', 1),
         (1, 'Product C', 3),
         (3, 'Product D', 5);


--------------------------------------------------------------------------
