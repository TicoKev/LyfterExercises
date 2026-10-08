from flask import Flask
from .lyfter_car_rental_API_endpoints.users_endpoint import users_bp
from .lyfter_car_rental_API_endpoints.cars_endpoint import cars_bp
from .lyfter_car_rental_API_endpoints.rents_endpoint import rents_bp


app = Flask(__name__)
app.register_blueprint(users_bp)
app.register_blueprint(cars_bp)
app.register_blueprint(rents_bp)

if __name__ == '__main__':
    app.run('localhost', debug=True)
