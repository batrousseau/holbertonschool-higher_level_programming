#!/usr/bin/python3

"""Basic Security Implementation for Flask API (Task 05).

This module demonstrates the implementation of two-layer authentication:
1. HTTP Basic Authentication using flask_httpauth for initial access control.
2. JWT Token-based Authentication using flask_jwt_extended for protected routes,
   with role-based authorization checks (Admin vs User roles).

Features implemented:
- Password hashing and verification via werkzeug.security.
- Custom token creation based on user roles ('admin' or 'user').
- Error handlers for missing tokens and invalid JWTs.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, decode_token
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuration for the secret key used to sign and verify tokens.
app.config["JWT_SECRET_KEY"] = "this_is_bandolero_wannabe"
jwt = JWTManager(app=app)


# In-memory user database with hashed passwords.
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for HTTP Basic Auth.

    Checks if the username exists in the users dictionary and validates 
    the provided password against the stored hash. Returns the username 
    on success or None on failure."""
    
    # Check if username exists in our database keys
    if username not in users.keys():
        return None

    user_data = users.get(username)
    # Verify password hash matches the input password
    if not check_password_hash(user_data.get("password"), password):
        return None

    return (username)


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Endpoint protected by HTTP Basic Authentication.

    Only accessible after successful login with valid username/password."""
    
    return ("Basic Auth: Access Granted"), 200


@app.post("/login")
def loggin():
    """Handle user login and generate JWT tokens based on role.

    Accepts JSON body with 'username' and 'password'. 
    Returns a token for the authenticated user or an error if credentials fail."""
    
    # Verify credentials using our custom function (note: this bypasses auth.login_required here)
    username = verify_password(request.json.get("username"), request.json.get("password"))

    if not username:
        return (401)

    role = users.get(username).get("role")

    # Create token with specific claims based on user's role
    if role == "admin":
        token = create_access_token(identity=username,additional_claims={"role": "admin"})
    else:
        token = create_access_token(identity=username, additional_claims={"role": "user"})

    return {"access_token" : token}, 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Endpoint protected by JWT Token.

    Requires a valid access token in the Authorization header."""
    
    return ("JWT Auth: Access Granted"), 200


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Admin-specific endpoint requiring elevated privileges.

    Checks if the current user (from JWT identity) has 'admin' role.
    Returns 403 Forbidden for non-admin users."""
    
    token = get_jwt_identity()
    # Verify that the logged-in user is an administrator
    if users.get(token).get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return ("Admin Access: Granted"), 200


@jwt.unauthorized_loader
def missing_token(reason):
    """Custom error handler for unauthorized requests (missing token)."""
    
    return jsonify({"error": "Token missing"}), 401


@jwt.invalid_token_loader
def invalid_token(reason):
    """Custom error handler for invalid or malformed tokens."""
    
    return jsonify({"error": "Invalid token"}), 401

if __name__ == "__main__":
    app.run(debug=True)
