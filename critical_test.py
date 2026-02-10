import os
from flask import Flask, request
import sqlite3

app = Flask(__name__)

# 🔴 CRITICAL: SQL Injection vulnerability
@app.route("/user")
def get_user():
    user_id = request.args.get("id")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ Dangerous string concatenation
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()

    return {"data": result}


# 🔴 CRITICAL: Command Injection vulnerability
@app.route("/ping")
def ping():
    host = request.args.get("host")

    # ❌ Direct system execution with user input
    os.system("ping -c 1 " + host)

    return {"status": "done"}


if __name__ == "__main__":
    app.run(debug=True)
