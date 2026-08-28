import sqlite3
import os
import subprocess
import pickle
import hashlib

def get_user(username):
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username='" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def ping_host(hostname):
    os.system("ping -c 1 " + hostname)

def list_directory(path):
    subprocess.call("ls " + path, shell=True)

def load_data(serialized_data):
    return pickle.loads(serialized_data)

DB_PASSWORD = "admin123"
API_KEY = "sk-hardcoded-secret-key-12345"

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def calculate(expression):
    return eval(expression)

def read_file(filename):
    path = "./uploads/" + filename
    with open(path, 'r') as f:
        return f.read()
