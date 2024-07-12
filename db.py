from app import app
from models import db

app.config.from_object('config.Config')
db.init_app(app)

with app.app_context():
    db.create_all()
