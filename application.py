from flask import Flask, request, jsonify, make_response
from src.chatgpt import ChatGPT
import os
from src.jwt_tools import create_token, token_required

app = Flask(__name__)


@app.route("/")
def hello():
    return 'hello world'

@app.route("/login", methods=["POST"])
def login():
    request_data = request.json
    print(request_data)
    if request_data["user"] == os.getenv("USER") and request_data[
        "password"
    ] == os.getenv("PASSWORD"):
        return jsonify(create_token(request_data["user"]))
    else:
        return make_response(
            "Unable to verify",
            403,
            {"WWW-Authenticate": 'Basic realm: "Authentication Failed "'},
        )

@app.route("/chatgpt", methods=["POST"])
@token_required
def messageToChatGpt():
    request_data = request.json
    chatgpt = ChatGPT()
    response = chatgpt.send_message(request_data["message"])
    return response


if __name__ == "__main__":
    app.run()
