from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True  
    
   
    db.init_app(app)
    migrate.init_app(app, db)
    
    
    register_blueprints(app)
    
  
    register_error_handlers(app)
    
    return app

def register_blueprints(app):
    from server.controllers.restaurant_controller import restaurants_bp
    from server.controllers.pizza_controller import pizzas_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizzas_bp
    
    app.register_blueprint(restaurants_bp)
    app.register_blueprint(pizzas_bp)
    app.register_blueprint(restaurant_pizzas_bp)

def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request(e):
        return jsonify(error=str(e)), 400
        
    @app.errorhandler(404)
    def not_found(e):
        return jsonify(error=str(e)), 404
        
    @app.errorhandler(500)
    def server_error(e):
        db.session.rollback()
        return jsonify(error="Internal server error"), 500