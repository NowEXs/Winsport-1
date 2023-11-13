from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    pic = db.Column(db.String(250))
    favorites = db.relationship('Favorite', backref='user', lazy=True)

    def toggle_favorite(self, item_id):
        favorite = Favorite.query.filter_by(user_id=self.id, item_id=item_id).first()

        if favorite:
            db.session.delete(favorite)
        else:
            new_favorite = Favorite(user_id=self.id, item_id=item_id)
            db.session.add(new_favorite)

    def get_favorite_list(self):
        return [fav.item_id for fav in self.favorites]

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    item_id = db.Column(db.Integer)
    