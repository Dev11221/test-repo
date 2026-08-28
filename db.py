from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('app.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/users/search', methods=['GET'])
def search_users():
    username = request.args.get('username', '')
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT id, username, email FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    results = cursor.fetchall()

    conn.close()
    return jsonify([dict(row) for row in results])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, username, email FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(dict(user))

if __name__ == '__main__':
    app.run(debug=True)
