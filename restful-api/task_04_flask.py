#!/usr/bin/python3

"""Flask RESTful API for User Management (Task 04).

This module provides endpoints to manage users in an in-memory dictionary:
- GET / : Welcome message.
- GET /data : List of all usernames.
- GET /status : Health check status.
- GET /users/<username> : Retrieve a specific user by username.
- POST /add_user : Add a new user to the system.

Note: The `users` dictionary is currently commented out in this file. 
Ensure it is uncommented or defined before running if data persistence is needed,
or handle potential NameError exceptions gracefully depending on requirements."""

from flask import Flask, jsonify, request

app = Flask(__name__)

users: dict = {}
@app.route("/")
def home():
    return ("Welcome to the Flask API!", 200)


# Endpoint: Home page with welcome message.
@app.route("/data")
def data():
    user_list: list = []
    for key in users.keys():
        user_list.append(key)
    return (jsonify(user_list), 200)

# Endpoint: Health check returning "OK".
@app.route("/status")
def status():
    return ("OK", 200)


# Endpoint: Retrieve a specific user by username. Returns 404 if not found.
@app.route("/users/<username>")
def get_specific_user(username: str):
    for key, value in users.items():
        if key == username:
            return (jsonify(value), 200)
    return({"error": "User not found"}, 404)


# Endpoint: Add a new user. Validates input and checks for existing usernames.
@app.post("/add_user")
def add_user():
    new_user: dict = request.get_json(silent=True)
    print(f"{new_user}, Type is : {type(new_user)}")

    if not isinstance(new_user, dict):
        return (jsonify({"error":"Invalid JSON"}), 400)
    
    valid_username_field = new_user.get("username")
    if not valid_username_field:
        return (jsonify({"error":"Username is required"}), 400)


    new_username = new_user.get("username")
    print(f"{new_username}")
    for keys in users.keys():
        if keys == new_username:
            return(jsonify({"error":"Username already exists"}), 409)
    new_user.pop("username")
    rebuild_user: dict = {new_username : new_user}
    print(rebuild_user)
    users.update(rebuild_user)
    return(jsonify(f"User created, values {new_user}"), 200)


if __name__ == "__main__": app.run()
