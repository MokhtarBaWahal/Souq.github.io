

from app import app, db
from models import Product, Store, ProductImage


def read_image(file_path):
    """Reads an image file and returns its binary data."""
    with open(file_path, 'rb') as file:
        return file.read()


app.app_context().push()
db.create_all()

# Create products
imgs = [
    ProductImage(id=1, product_id=1, merchant_id=1, image_data=read_image("static/images/1.jpg")),
    ProductImage(id=2, product_id=1, merchant_id=1, image_data=read_image("static/images/2.jpg")),
    ProductImage(id=3, product_id=2, merchant_id=1, image_data=read_image("static/images/3.jpg")),
    ProductImage(id=4, product_id=2, merchant_id=1, image_data=read_image("static/images/4.jpg")),
    ProductImage(id=5, product_id=3, merchant_id=1, image_data=read_image("static/images/5.jpg")),
    ProductImage(id=6, product_id=4, merchant_id=1, image_data=read_image("static/images/6.jpg")),
    ProductImage(id=7, product_id=5, merchant_id=1, image_data=read_image("static/images/2.jpg")),
    ProductImage(id=8, product_id=6, merchant_id=1, image_data=read_image("static/images/9.jpg")),
    ProductImage(id=9, product_id=7, merchant_id=1, image_data=read_image("static/images/7.jpg")),
    ProductImage(id=10, product_id=8, merchant_id=1, image_data=read_image("static/images/5.jpg"))
]





db.session.bulk_save_objects(imgs)
db.session.commit()
stores = [
    Store(merchant_id=1, name="متجر اميليا للملابس", image=read_image("static/images/store_1.jpg")),
    Store(merchant_id=2, name="متجر سماء للملابس", image=read_image("static/images/store_1.jpg"))
]

db.session.bulk_save_objects(stores)
db.session.commit()

products = [
    Product(merchant_id=1, item_id=1, name="بلوزة قطنية للأطفال",
            description="بلوزة ناعمة ومريحة مصنوعة من القطن العضوي، تصميم ملون برسوم كرتونية.", price=10, quantity=50,
            category="ملابس"),
    Product(merchant_id=1, item_id=2, name="بنطلون جينز للأطفال",
            description="بنطلون جينز متين بتصميم عصري، متوفر بألوان مختلفة.", price=15, quantity=30, category="ملابس"),
    Product(merchant_id=1, item_id=3, name="فستان صيفي للأطفال",
            description="فستان خفيف وناعم مصنوع من القطن، بألوان زاهية ونقوش زهرية.", price=20, quantity=25, category="ملابس"),
    Product(merchant_id=1, item_id=4, name="سترة شتوية للأطفال",
            description="سترة صوفية دافئة، مناسبة لفصل الشتاء، متوفرة بألوان متعددة.", price=25, quantity=20, category="ملابس"),
    Product(merchant_id=1, item_id=5, name="بيجاما للأطفال",
            description="بيجاما ناعمة ومريحة مصنوعة من القطن، تصميم برسوم كرتونية محببة للأطفال.", price=12,quantity=20, category="ملابس"),
    Product(merchant_id=1, item_id=6, name="قبعة شمس للأطفال",
            description="قبعة شمسية بألوان زاهية، مصنوعة من القطن، توفر حماية من أشعة الشمس.", price=8, quantity=60,  category="ملابس"),
    Product(merchant_id=1, item_id=7, name="حذاء رياضي للأطفال",
            description="حذاء رياضي مريح وداعم، مثالي للأنشطة اليومية، متوفر بأحجام وألوان مختلفة.", price=18,
            quantity=35, category="ملابس"),
    Product(merchant_id=1, item_id=8, name="جوارب قطنية للأطفال",
            description="جوارب ناعمة ومريحة مصنوعة من القطن، بألوان وتصاميم مختلفة.", price=5, quantity=100,  category="أحذية")
]

db.session.bulk_save_objects(products)
db.session.commit()
