from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from firebase_admin import  auth
from dotenv import load_dotenv
import os

# Additional Security Considerations:
# TODO  Input Validation: Ensure that all user inputs are validated and sanitized.
# TODO  Error Handling: Implement robust error handling to prevent sensitive information from being exposed.
# TODO  HTTPS: Ensure that all communications with the server are encrypted using HTTPS.
# TODO Rate Limiting: Implement rate limiting to prevent abuse of your API.
# TODO  CSRF Protection: Use CSRF tokens if you're handling forms or other POST requests.

load_dotenv()

# ====== APP SET UP ===== #
app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

SECRET_KEY = os.getenv("MY_SERVER_STAMP")


# ===== SECURITY OF THE SERVER ===== #
app.secret_key = SECRET_KEY
app.config["SESSION_USE_SIGNER"] = True # apply the stamp to the session
app.config["SESSION_TYPE"] = "filesystem" # storage of the session (proto = server)
app.config["SESSION_PERMANENT"] = False # when browser is closed then the session disappear
app.config["SESSION_COOKIE_HTTPONLY"] = True # prevent XSS
app.config["SESSION_COOKIE_SAMESITE"] = "Lax" # prevent CSRF

Session(app)

# ===== SECURITY OF THE CLIENT (HEADER) ===== #
@app.after_request
def header_security_definition(response):
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self' https://cdnjs.cloudflare.com https://fonts.googleapis.com; "
        "font-src 'self' https://fonts.gstatic.com https://cdnjs.cloudflare.com; "
        "img-src 'self' data:; "
        "object-src 'none'; "
        "base-uri 'self';"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    return response

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
        session["user"] = 1
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True, port=5500, host="0.0.0.0")