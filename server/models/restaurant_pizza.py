# server/models/restaurant_pizza.py
from server import db

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    
    restaurant_id = db.Column(db.Integer, 
                            db.ForeignKey('restaurants.id', ondelete='CASCADE'),
                            nullable=False)
    pizza_id = db.Column(db.Integer, 
                        db.ForeignKey('pizzas.id'),
                        nullable=False)
    
    restaurant = db.relationship('Restaurant', back_populates='pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurants')
    
    __table_args__ = (
        db.CheckConstraint('price >= 1 AND price <= 30', name='price_range'),
    )