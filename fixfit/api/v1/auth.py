from flask import Blueprint

from fixfit import jwt
from fixfit.api.v1.user import User

bp = Blueprint('auth', __name__)

@jwt.authentication_handler
def authenticate(username, password):
    user = User.query.filter_by(email=username).first()
    if user and user.password == password:
        return user

@jwt.user_handler
def load_user(payload):
    user = User.query.get(payload['user_id'])
    return user
