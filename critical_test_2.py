import os
import subprocess
from flask import Flask, request

app = Flask(__name__)

# 🔴 CRITICAL 1: Command Injection via subprocess
@app.route("/run")
def run_command():
    cmd = request.args.get("cmd")

    # ❌ Dangerous: user input directly passed to shell
    result = subprocess.check_output(cmd, shell=True)

    return {"output": result.decode()}


# 🔴 CRITICAL 2: Hardcoded Secret
SECRET_KEY = "super_secret_production_key_12345"


# 🔴 CRITICAL 3: Insecure Debug Mode
if __name__ == "__main__":
    app.run(debug=True)


# 🔴 CRITICAL 4: eval() usage (Code Injection)
def unsafe_eval(user_input):
    return eval(user_input)
