from server import create_app
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant
from server.models.restaurant_pizza import RestaurantPizza
from server import db

app = create_app()

with app.app_context():
    # Clear existing data
    db.session.query(RestaurantPizza).delete()
    db.session.query(Pizza).delete()
    db.session.query(Restaurant).delete()
    
    # Create pizzas
    cheese = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pepperoni = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
    veggie = Pizza(name='Veggie', ingredients='Dough, Tomato Sauce, Cheese, Vegetables')
    
    # Create restaurants
    dominos = Restaurant(name='Dominos', address='123 Main St')
    pizza_hut = Restaurant(name='Pizza Hut', address='456 Oak Ave')
    little_caesars = Restaurant(name='Little Caesars', address='789 Pine Rd')
    
    # Add to session
    db.session.add_all([cheese, pepperoni, veggie])
    db.session.add_all([dominos, pizza_hut, little_caesars])
    db.session.commit()
    
    # Create restaurant pizzas
    rp1 = RestaurantPizza(price=10, pizza_id=cheese.id, restaurant_id=dominos.id)
    rp2 = RestaurantPizza(price=12, pizza_id=pepperoni.id, restaurant_id=dominos.id)
    rp3 = RestaurantPizza(price=15, pizza_id=veggie.id, restaurant_id=pizza_hut.id)
    rp4 = RestaurantPizza(price=8, pizza_id=cheese.id, restaurant_id=little_caesars.id)
    
    db.session.add_all([rp1, rp2, rp3, rp4])
    db.session.commit()
    
    print("Database seeded successfully!")