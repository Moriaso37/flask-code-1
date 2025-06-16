from flask import Blueprint, jsonify, request
from server.models import db
from server.models.restaurant import Restaurant

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([r.to_dict() for r in restaurants]), 200

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    pizzas = [rp.pizza.to_dict() for rp in restaurant.restaurant_pizzas]
    response = restaurant.to_dict()
    response['pizzas'] = pizzas
    return jsonify(response), 200

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204