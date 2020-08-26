from application import db
#db is teamdb
#export DATABASE_URI=mysql+pymysql://root:root@(sql ip):3306/teamdb
#export SECRET_KEY=afgjkajfbajkbcwabkfhjgakjhfkjahckjabwuhgfbiuawgf

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    slogan = db.Column(db.String(5000), nullable=False)