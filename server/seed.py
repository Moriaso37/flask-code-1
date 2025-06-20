from server import create_app
from server.models import db, Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    
    db.drop_all()
    db.create_all()

    
    restaurants = [
        Restaurant(name="Pizza Palace", address="123 Main St"),
        Restaurant(name="Italian Bistro", address="456 Oak Ave"),
        Restaurant(name="Slice of Heaven", address="789 Pine Blvd")
    ]
    db.session.add_all(restaurants)

    
    pizzas = [
        Pizza(name="Margherita", ingredients="Tomato sauce, mozzarella, basil"),
        Pizza(name="Pepperoni", ingredients="Tomato sauce, mozzarella, pepperoni"),
        Pizza(name="Vegetarian", ingredients="Tomato sauce, mozzarella, bell peppers, mushrooms, onions")
    ]
    db.session.add_all(pizzas)

    db.session.commit()

  
    restaurant_pizzas = [
        RestaurantPizza(price=10, pizza_id=1, restaurant_id=1),
        RestaurantPizza(price=12, pizza_id=2, restaurant_id=1),
        RestaurantPizza(price=15, pizza_id=3, restaurant_id=2),
        RestaurantPizza(price=11, pizza_id=1, restaurant_id=3),
        RestaurantPizza(price=13, pizza_id=2, restaurant_id=3)
    ]
    db.session.add_all(restaurant_pizzas)

    db.session.commit()

    print("Database seeded successfully!")