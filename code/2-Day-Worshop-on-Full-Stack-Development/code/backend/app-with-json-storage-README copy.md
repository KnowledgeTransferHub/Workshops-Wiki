# App with Local JSON file as Storage

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
