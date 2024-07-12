from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    merchant_id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    images = db.relationship('ProductImage', backref='product', lazy=True)
    category = db.Column(db.String(50), nullable=False)


class ProductImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.item_id'), nullable=False)
    merchant_id = db.Column(db.Integer, db.ForeignKey('store.merchant_id'), nullable=False)
    image_data = db.Column(db.LargeBinary, nullable=False)


class Store(db.Model):
    merchant_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.LargeBinary, nullable=True)
