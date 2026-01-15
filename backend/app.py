from flask import Flask, render_template, request, redirect, url_for, session
from firebase_admin import  auth
from dotenv import load_dotenv
import os

load_dotenv()

# ====== APP SET UP ===== #
app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

SECRET_KEY = os.getenv("MY_SERVER_STAMP")
app.secret_key = SECRET_KEY

# ===== SECURITY OF THE SERVER ===== #

# ===== SECURITY OF THE CLIENT (HEADER) ===== #
@app.before_request
def header_definition():
    pass
# ===== ROUTES ===== #
# Home page
@app.route("/")
def index():
    return redirect(url_for("login"))


#login page
@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/check-credentials", methods=["POST"])
def check_credentials():
    if request.method == "POST":
        # if logged in then session["user"] = user_id
        
        pass

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=5500, host="0.0.0.0")