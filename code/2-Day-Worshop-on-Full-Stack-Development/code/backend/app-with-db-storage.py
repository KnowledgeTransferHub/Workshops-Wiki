from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Configure your PostgreSQL database connection
db_config = {
    'host': '192.168.0.117',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
}

# Function to establish a database connection


def get_db_connection():
    connection = psycopg2.connect(**db_config)
    return connection

# Route for user registration


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    # Check if the username is already taken
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cursor.fetchone()
    if existing_user:
        cursor.close()
        connection.close()
        return jsonify({'message': 'Username already exists'}), 400

    # Insert the new user into the database
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    connection.commit()

    cursor.close()
    connection.close()
    return jsonify({'message': 'Registration successful'}), 201

# Route for user login


@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    connection = get_db_connection()
    cursor = connection.cursor()

    # Find the user by username
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user is None or user[2] != password:
        cursor.close()
        connection.close()
        return jsonify({'message': 'Invalid credentials'}), 401

    cursor.close()
    connection.close()
    return jsonify({'message': 'Login successful'}), 200


if __name__ == '__main__':
    app.run(debug=True)
