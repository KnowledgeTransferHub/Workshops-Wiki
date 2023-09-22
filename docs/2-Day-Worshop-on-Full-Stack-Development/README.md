# 2 Day Workshop on Full Stack Development with Flask, HTML, CSS, JS, and Postgres

Welcome to the 2 Day Full Stack Development Workshop by KTHub! This workshop will equip you with the skills to build a full-stack web application using Python Flask for the backend, HTML, CSS, and JavaScript for the frontend, and PostgreSQL as the database.

## Workshop Schedule

## Day 1: Fundamentals and Backend Development

### Session 1: Introduction and Setup (30 minutes)

- Welcome participants and introduce the workshop's objectives.
- Provide an overview of the technologies covered.
- Help attendees set up their development environment, including Python and Flask installation.

### Session 2: Python Flask - Sample GET/POST/PUT/DELETE (2.5 hours)

- Dive into Python Flask, a powerful web framework.
- Explore the fundamental concepts of web development and RESTful APIs.
- Hands-on exercises:
  - Create a Flask application.
  - Implement sample CRUD operations: GET, POST, PUT, DELETE.
  - Test API endpoints using tools like Postman.

### Session 3: HTML (1.5 hours)

- Introduction to HTML (Hypertext Markup Language).
- Understand the structure and syntax of HTML.
- Hands-on practice:
  - Create a basic HTML webpage.
  - Add elements like headings, paragraphs, lists, and links.

### Session 4: HTML/CSS Integration (1.5 hours)

- Discuss the importance of CSS (Cascading Style Sheets) in web design.
- Create a more visually appealing webpage by integrating CSS.
- Hands-on practice:
  - Link an external CSS stylesheet to the HTML page.
  - Apply CSS rules to style elements.
  - Explore CSS selectors, properties, and values.

## Day 2: Frontend and Database Integration

### Session 5: HTML/CSS/JS (1.5 hours)

- Combine HTML, CSS, and JavaScript to create interactive web pages.
- Hands-on practice:
  - Create a web page with HTML structure.
  - Apply CSS styles for improved presentation.
  - Implement JavaScript to add interactivity.

### Session 6: Storing Data (JSON in File) (1.5 hours)

- Discuss data storage options for web applications.
- Implement data storage using JSON (JavaScript Object Notation) in a local file.
- Hands-on practice:
  - Create, read, update, and delete data entries in a JSON file.

### Session 7: PostgreSQL and Database Integration (1 hour)

- Introduce PostgreSQL, an open-source relational database.
- Discuss the advantages of using a database for data management.
- Hands-on practice:
  - Set up a PostgreSQL database.
  - Integrate PostgreSQL with Flask for data storage and retrieval.
  - Perform CRUD operations on a real database.

## Getting Started

1. Clone or download this repository to your local machine.
2. Follow the instructions in the respective session directories for hands-on exercises and code samples.

## Prerequisites

- Basic knowledge of Python, HTML, CSS, JS and SQL is recommended.
- Bring your enthusiasm and a laptop with your preferred code editor installed.

## Workshop Objectives

- Build a full-stack web application from scratch.
- Learn backend development with Python Flask.
- Create dynamic web pages using HTML, CSS, and JavaScript.
- Integrate a PostgreSQL database into your application.
- Understand how to handle API requests and store data in JSON files.

## Project Highlights

As part of this workshop, you will create a full-stack web application that includes the following features:

- User registration and login functionality.
- API endpoints for user registration and authentication.
- Frontend web pages for user interaction.
- Integration with a PostgreSQL database.
- Secure storage of user credentials in a JSON file.

## Contributions

If you find issues or have suggestions for improvements in the workshop materials, please feel free to create pull requests or issues in this repository.

## License

This workshop content is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or need assistance, please create an issue in this repository.

Happy coding and enjoy the workshop!

## Application

This is a simple Python Flask app that provides two routes:

- `/register`: This route allows users to register for an account.
- `/login`: This route allows users to log in to their account.

### Requirements

- Python 3.6 or higher
- Flask
- Flask-CORS
- psycopg2

### Installation

To install the app, clone this repository and run the following command:

```bash
pip install -r requirements.txt
```

### Usage

To start the app, run the following command:

```bash
flask run
```

### Registering for an account

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

### Logging in to an account

To log in to an account, send a GET request to the `/login` route with the following query parameters:

- `username`: Your username
- `password`: Your password

If the login is successful, the app will return a JSON response with the following message:

```json
{
  "message": "Login successful"
}
```

You can now test the user registration endpoint using a tool such as Postman:

#### POST <http://localhost:5000/register>

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

    ```python
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
