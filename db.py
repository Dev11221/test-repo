from flask import Flask, request, jsonify
import sqlite3
import subprocess
import pickle
import os

app = Flask(__name__)

DB = "users.db"
API_KEY = "dev-secret-123"

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    db = get_db()

    # Looks normal, but user input is inserted directly into SQL.
    query = (
        "SELECT * FROM users "
        f"WHERE username = '{username}' "
        f"AND password = '{password}'"
    )

    user = db.execute(query).fetchone()

    if user:
        return jsonify({"logged_in": True, "user": user["username"]})

    return jsonify({"logged_in": False}), 401


@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")

    # User-controlled input reaches a shell command.
    result = subprocess.check_output(
        f"ping -c 1 {host}",
        shell=True,
        text=True
    )

    return jsonify({"result": result})


@app.route("/profile")
def profile():
    filename = request.args.get("file", "profile.pkl")

    # The application assumes the requested file is safe.
    with open(os.path.join("profiles", filename), "rb") as f:
        profile = pickle.load(f)

    return jsonify(profile)


@app.route("/admin")
def admin():
    supplied_key = request.headers.get("X-API-Key")

    if supplied_key == API_KEY:
        return jsonify({
            "admin": True,
            "message": "Sensitive administration area"
        })

    return jsonify({"admin": False}), 403


@app.route("/debug")
def debug():
    # Debug information is exposed to anyone who requests this endpoint.
    return jsonify({
        "database": DB,
        "environment": dict(os.environ),
        "api_key": API_KEY
    })


if __name__ == "__main__":
    app.run(debug=True)
