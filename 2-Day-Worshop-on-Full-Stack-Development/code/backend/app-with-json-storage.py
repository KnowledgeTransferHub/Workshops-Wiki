from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import json

app = Flask(__name__)
CORS(app)

# File to store user data (create this file if it doesn't exist)
USER_DATA_FILE = 'user_data.json'

# Initialize the user data from the file or create an empty list
try:
    with open(USER_DATA_FILE, 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    users = []

# Save user data to the file


def save_user_data():
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

# Route for user registration


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    # Check if the username is already taken
    if any(user['username'] == username for user in users):
        return jsonify({'message': 'Username already exists'}), 400

    # Add the user to the list and save to the file
    users.append({'username': username, 'password': password})
    save_user_data()
    return jsonify({'message': 'Registration successful'}), 201

# Route for user login


@app.route('/login', methods=['GET'])
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    # Find the user by username
    user = next((user for user in users if user['username'] == username), None)

    if user is None or user['password'] != password:
        return jsonify({'message': 'Invalid credentials'}), 401

    return jsonify({'message': 'Login successful'}), 200


if __name__ == '__main__':
    app.run(debug=True)
