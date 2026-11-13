from flask import Flask
import os

app = Flask(__name__)
APP_NAME = os.getenv("APP_NAME", "demo-app")
SECRET_MSG = os.getenv("SECRET_MSG", "default message")

@app.route("/")
def index():
    return f"""
    <h1>Hello {APP_NAME}</h1>
    <p>Secret: {SECRET_MSG}</p>
    <p>New feature tip: this is from feature branch!</p>
    """

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
