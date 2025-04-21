from flask import Blueprint, request, jsonify
from db.queries import get_animals  # adjust the import based on your structure

animals_bp = Blueprint('animals', __name__)

@animals_bp.route('/get_animals', methods=['GET'])
def get_animals_route():
    age = request.args.get('age')
    name = request.args.get('name')
    
    try:
        results = get_animals(age=age, name=name)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
