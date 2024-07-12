# app.py
from flask import Flask, render_template, send_file, abort, request
from io import BytesIO

from flask_babel import Babel

from models import db, Product, Store, ProductImage

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BABEL_DEFAULT_LOCALE'] = 'ar'
babel = Babel(app)
db.init_app(app)


# @app.route('/')
# @app.route('/<int:merchant_id>')
def home(merchant_id=None):
    if merchant_id is None:
        products = Product.query.all()
        categories = db.session.query(Product.category).distinct().all()
        data = {"products": products, "merchant_id": '', "store_name": 'سوق المكلا الالكتروني',
                "categories": categories}
        return render_template('index.html', data=data)

    store_name = get_store_name(merchant_id)
    section = request.args.get('section', '')
    if section == "":
        products = Product.query.filter_by(merchant_id=merchant_id)
    else:
        products = Product.query.filter_by(category=section, merchant_id=merchant_id)

    categories = db.session.query(Product.category).filter_by(merchant_id=merchant_id).distinct().all()
    print(categories)
    data = {"products": products, "merchant_id": merchant_id, "store_name": store_name, "categories": categories}

    return render_template('index.html', data=data)


def get_store_name(merchant_id):
    print("Looking for merchant #", merchant_id)
    store = Store.query.filter_by(merchant_id=merchant_id).first()
    if not store or not store.name:
        abort(404)
    return store.name


@app.route('/product_image/<int:product_id>/<int:merchant_id>')
def product_image(product_id, merchant_id):
    print("Looking for product #", product_id)
    product = ProductImage.query.filter_by(product_id=product_id, merchant_id=merchant_id).first()
    print(product)
    if not product or not product.image_data:
        abort(404)
    return send_file(BytesIO(product.image_data), mimetype='image/jpeg')


@app.route('/store_image/<int:merchant_id>')
def store_image(merchant_id):
    print("Looking for merchant #", merchant_id)
    store = Store.query.filter_by(merchant_id=merchant_id).first()
    if not store or not store.image:
        abort(404)
    return send_file(BytesIO(store.image), mimetype='image/jpeg')


app.add_url_rule('/', 'home', home)
app.add_url_rule('/<int:merchant_id>', 'home', home)


@app.route('/item_page/<int:merchant_id>/<int:item_id>')
def item_page(merchant_id, item_id):
    imgs = ProductImage.query.filter_by(product_id=item_id, merchant_id=1)
    product = Product.query.filter_by(item_id=item_id, merchant_id=merchant_id).first()
    imgs = list(imgs)
    data = {"imgs": imgs, "len":len(imgs),  "item_id": item_id, "product": product, "merchant_id": merchant_id}
    return render_template('item.html', data=data)


@app.route('/product_imgs_stack/<int:product_id>/<int:img_id>')
def product_imgs_stack(product_id, img_id):
    print("Looking for image #", img_id)
    product = ProductImage.query.filter_by(id=img_id, product_id=product_id).first()

    if not product or not product.image_data:
        abort(404)
    return send_file(BytesIO(product.image_data), mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
