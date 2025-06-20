# server/controllers/restaurant_controller.py
from flask import Blueprint, jsonify, request
from server import db
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza

restaurants_bp = Blueprint('restaurants', __name__)

@restaurants_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    try:
        restaurants = Restaurant.query.all()
        return jsonify([{
            'id': r.id,
            'name': r.name,
            'address': r.address
        } for r in restaurants])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@restaurants_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404
            
        pizzas = [{
            'id': rp.pizza.id,
            'name': rp.pizza.name,
            'ingredients': rp.pizza.ingredients
        } for rp in restaurant.pizzas]
        
        return jsonify({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': pizzas
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@restaurants_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    try:
        restaurant = Restaurant.query.get(id)
        if not restaurant:
            return jsonify({'error': 'Restaurant not found'}), 404
            

        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500