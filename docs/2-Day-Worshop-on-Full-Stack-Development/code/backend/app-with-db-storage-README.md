# App with Postgres as Storage

This is a simple Python Flask app that provides two routes:

* `/register`: This route allows users to register for an account.
* `/login`: This route allows users to log in to their account.

## Requirements

* Python 3.6 or higher
* Flask
* Flask-CORS
* psycopg2

## Installation

To install the app, clone this repository and run the following command:

```bash
pip install -r requirements.txt
```

## Usage

To start the app, run the following command:

```bash
flask run
```

## Registering for an account

To register for an account, send a POST request to the /register route with the following JSON body:

```json
{
"username": "your_username",
"password": "your_password"
}
```

If the registration is successful, the app will return a JSON response with the following message:

```json
{
  "message": "Registration successful"
}
```

## Logging in to an account

To log in to an account, send a GET request to the `/login` route with the following query parameters:

* `username`: Your username
* `password`: Your password

If the login is successful, the app will return a JSON response with the following message:

```json
{
  "message": "Login successful"
}
```

### To add PostgreSQL connectivity to your Flask app, you can follow these steps

1. Install the psycopg2 library:

    ```bash
    pip install psycopg2
    ```

2. Create a database connection string:

    ```python
    db_config = {
        'host': 'localhost',
        'database': 'postgres',
        'user': 'postgres',
        'password': 'postgres',
    }
    ```

3. Create a function to establish a database connection:

    ```Python
    def get_db_connection():
        connection = psycopg2.connect(**db_config)
        return connection
    ```

4. Update your app.py file to use the database connection function:

    ```Python
    from flask import Flask, request, jsonify
    from flask_cors import CORS
    import psycopg2

    app = Flask(__name__)
    CORS(app)

    # Get a database connection

    connection = get_db_connection()

    # Route for user registration

    @app.route('/register', methods=['POST'])
    def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    cursor = connection.cursor()

    # Check if the username is already taken
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        cursor.close()
        return jsonify({'message': 'Username already exists'}), 400

    # Insert the new user into the database
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    connection.commit()

    cursor.close()
    return jsonify({'message': 'Registration successful'}), 201
    ```

5. Create your database schema (DDL) using a SQL client such as pgAdmin or DBeaver. The DDL you provided is for a table called users with three columns: id, username, and password.

    ```sql
    CREATE TABLE users (
        id serial PRIMARY KEY,
        username VARCHAR (80) UNIQUE NOT NULL,
        password VARCHAR (80) NOT NULL
    );
    ```

6. Start your Flask app:

    ```bash
    flask run
    ```

You can now test the user registration endpoint using a tool such as Postman:

### POST <http://localhost:5000/register>

```json
Content-Type: application/json

{
  "username": "johndoe",
  "password": "password123"
}
```

If the registration is successful, Postman will return a JSON response with the following message:

```JSON
{
  "message": "Registration successful"
}
```

It is similar for login as well.

## Deployment

To deploy the app, run the below command

```bash
python3 app-with-db-storage.py
```
