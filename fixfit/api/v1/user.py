from flask import Blueprint, jsonify, request
from flask.ext.jwt import current_user, jwt_required
from fixfit.models.user import User

import json

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    user = User(**data)
    return jsonify(user.to_dict())

@bp.route('/me', methods=['GET'])
@jwt_required()
def get_user():
    return jsonify(current_user.to_dict())