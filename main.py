from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///service.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)

# SERVICE
class ProductService:

    @staticmethod
    def get_expensive_products(price):
        return Product.query.filter(Product.price > price).all()

@app.route('/expensive')
def expensive():
    products = ProductService.get_expensive_products(500)

    return jsonify([p.name for p in products])

with app.app_context():
    db.create_all()
