from flask import Blueprint, jsonify

bp = Blueprint('activity', __name__)

@bp.route('/activities', methods=['GET'])
def get_activities():
    return jsonify({
        'activities': [
            {
                'name': 'Strength'
            },
            {
                'name': 'Mountain Climbing'
            },
            {
                'name': 'Cycling'
            },
            {
                'name': 'Running'
            },
            {
                'name': 'Swimming'
            },
        ]
    })
