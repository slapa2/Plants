from plants import db


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    polish_name = db.Column(db.String(50), unique=True)
    latin_name = db.Column(db.String(50))
    light_level = db.Column(db.Integer)
    water_level = db.Column(db.Integer)
    spray = db.Column(db.Boolean)
    light_description = db.Column(db.Text)
    water_description = db.Column(db.Text)
    temperature = db.Column(db.Text)
    soil = db.Column(db.Text)
    fertilizing = db.Column(db.Text)
    transplanting = db.Column(db.Text)
    multiplication = db.Column(db.Text)
    image = db.Column(db.Text, nullable=False, default="../static/img/plant.png")

    def __repr__(self):
        return f'Plant {self.polish_name} {self.latin_name}'
