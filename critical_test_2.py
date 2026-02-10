from flask import Flask

app = Flask(__name__)

# 🟠 HIGH: Hardcoded secret (security smell, not injection)
SECRET_KEY = "temporary_dev_secret_key"

# 🟢 LOW: Debug mode enabled (often WARNING)
if __name__ == "__main__":
    app.run(debug=True)


# 🟢 LOW: Weak password check example
def check_password(password):
    # Weak validation logic (not critical, but poor practice)
    if len(password) < 4:
        return False
    return True
