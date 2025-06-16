from flask import Blueprint, request, jsonify
from models import db
from models.restaurant_pizza import RestaurantPizza

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    try:
        rp = RestaurantPizza(
            price=price,
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(rp)
        db.session.commit()
        return jsonify(rp.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400

