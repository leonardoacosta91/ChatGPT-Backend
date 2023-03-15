from flask import request, jsonify
import jwt
from datetime import datetime, timedelta
import os
from functools import wraps

JWT_SECRET = os.getenv("SECRET")
JWT_ALGORITHM = os.getenv("ALGORITHM")


def create_token(username):
    token = jwt.encode(
        {
            "user": username,
            "expiration": str(datetime.utcnow() + timedelta(seconds=600)),
        },
        JWT_SECRET,
        algorithm=JWT_ALGORITHM,
    )
    return {"token": token}


def token_required(func):
    # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return jsonify({"Message": "Token is missing!"}), 401
        try:
            data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
        # You can use the JWT errors in exception
        # except jwt.InvalidTokenError:
        #     return 'Invalid token. Please log in again.'
        except Exception as e:
            return jsonify({"Message": "Invalid token"}), 403
        return func(*args, **kwargs)

    return decorated
