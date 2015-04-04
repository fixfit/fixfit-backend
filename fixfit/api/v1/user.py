from flask import Blueprint, jsonify, request
from flask.ext.jwt import current_user, jwt_required
from fixfit.models.user import User
from fixfit import db
import json

bp = Blueprint('user', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = json.loads(request.data)
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict())

@bp.route('/users/<id>', methods=['DELETE', 'GET'])
def user(id):
    user = User.query.filter_by(id=id).first_or_404()
    if request.method == 'GET':
        return jsonify(user.to_dict())
    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return jsonify({'status': 'ok'})

@bp.route('/me', methods=['GET'])
@jwt_required()
def get_user():
    return jsonify(current_user.to_dict())
