from application import db
from application.models import Team

db.drop_all()
db.create_all()