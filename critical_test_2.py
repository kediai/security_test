from flask import Flask

app = Flask(__name__)




# 🟢 LOW: Weak password check example
def check_password(password):
    # Weak validation logic (not critical, but poor practice)
    if len(password) < 4:
        return False
    return True
